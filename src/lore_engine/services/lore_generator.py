"""LoreGenerator service for generating factions and quests using LangChain and MCP tools."""

import json
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from lore_engine.core.config import settings
from lore_engine.core.logging import logger
from lore_engine.mcp_client.client import MCPClient


class LoreGenerator:
    """Generates worldbuilding lore (factions, quests) using LLM with MCP tools."""

    def __init__(self, mcp_client: MCPClient):
        """Initialize the LoreGenerator with an MCP client.

        Args:
            mcp_client: Connected MCP client instance for tool access
        """
        self.mcp_client = mcp_client
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            temperature=0.9,
            api_key=settings.openai_api_key,
        )
        logger.info(f"Initialized LoreGenerator with model: {settings.openai_model}")

    async def _get_langchain_tools(self) -> list[StructuredTool]:
        """Discover MCP tools and convert them to LangChain tools.

        Returns:
            List of LangChain StructuredTool instances
        """
        mcp_tools = await self.mcp_client.list_tools()
        langchain_tools = []

        for tool in mcp_tools:
            tool_name = tool["name"]
            tool_description = tool.get("description") or f"Tool: {tool_name}"

            input_schema = tool.get("inputSchema")

            if input_schema and "properties" in input_schema:
                fields = {}
                for prop_name, prop_info in input_schema.get("properties", {}).items():
                    field_type = str
                    field_description = prop_info.get("description", "")
                    fields[prop_name] = (
                        field_type,
                        Field(description=field_description),
                    )

                ToolInput = type(f"{tool_name}Input", (BaseModel,), {"__annotations__": fields})  # noqa: N806
            else:
                ToolInput = type(f"{tool_name}Input", (BaseModel,), {})  # noqa: N806

            async def tool_func(*args, **kwargs) -> str:
                """Execute the MCP tool."""
                # Capture tool_name in closure
                current_tool_name = tool_name
                result = await self.mcp_client.call_tool(current_tool_name, kwargs)
                return str(result)

            langchain_tool = StructuredTool(
                name=tool_name,
                description=tool_description,
                args_schema=ToolInput,
                func=lambda **kwargs: None,  # Sync version (not used)
                coroutine=tool_func,
            )

            langchain_tools.append(langchain_tool)
            logger.debug(f"Converted MCP tool '{tool_name}' to LangChain tool")

        logger.info(f"Converted {len(langchain_tools)} MCP tools to LangChain tools")
        return langchain_tools

    async def _build_system_prompt(self) -> str:
        """Build system prompt with tool information.

        Returns:
            System prompt string describing the LLM's purpose and available tools
        """
        tools = await self._get_langchain_tools()
        tool_descriptions = "\n".join([f"- {tool.name}: {tool.description}" for tool in tools])

        prompt = f"""
You are a creative worldbuilding assistant specialized in generating factions and quests for
tabletop RPGs.

Your purpose is to create rich, detailed, and imaginative content for game masters and world
builders.

Available tools:
{tool_descriptions}

Guidelines:
- Use the available tools as the main seed for you creativity
- Generate creative, original content with vivid details
- For factions: include name, symbol, core values, and soundtrack vibe
- For quests: include title, brief, NPCs, conflict, and location
- Always respond with valid JSON matching the requested format
- Be creative and surprising in your generation"""

        return prompt

    async def _execute_tool_calls(self, messages: list[Any], tool_calls: list[Any]) -> list[Any]:
        """Execute tool calls and add results to messages.

        Args:
            messages: Current conversation messages
            tool_calls: List of tool calls from LLM response

        Returns:
            Updated messages list with tool results
        """
        for tool_call in tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_call_id = tool_call.get("id", "")

            logger.info(f"Executing tool call: {tool_name} with args: {tool_args}")

            try:
                result = await self.mcp_client.call_tool(tool_name, tool_args)
                result_content = str(result)
            except Exception as e:
                logger.error(f"Tool call failed for {tool_name}: {e}")
                result_content = f"Error: {str(e)}"

            messages.append(
                ToolMessage(
                    content=result_content,
                    tool_call_id=tool_call_id,
                    name=tool_name,
                )
            )

        return messages

    async def generate_faction(self, count: int = 1) -> list[dict[str, Any]]:
        """Generate faction(s) for worldbuilding.

        Args:
            count: Number of factions to generate (1-10)

        Returns:
            List of faction dictionaries with structure:
            {
                "name": str,
                "symbol": str,
                "values": str,
                "soundtrack_vibe": str
            }
        """
        logger.info(f"Generating {count} faction(s)")

        system_prompt = await self._build_system_prompt()
        langchain_tools = await self._get_langchain_tools()

        faction_word = "faction" if count == 1 else "factions"
        user_message = f"""Generate {count} unique {faction_word} for a fantasy world.

Each faction should have:
- name: A creative faction name
- symbol: Description of their symbol or emblem
- values: Core beliefs and values (2-3 sentences)
- soundtrack_vibe: Musical genre/style that represents them

All the faction info should be based on a random genre or theme you can get by using the
fetch_genre tool. You are ONLY allowed to use that tool to get inspiration for the factions. You
perform  a UNIQUE call to the fetch_genre tool for EACH faction you generate.

Respond with ONLY a JSON array of faction objects, no additional text.
Format: [{{"name": "...", "symbol": "...", "values": "...", "soundtrack_vibe": "..."}}]"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_message),
        ]
        llm_with_tools = self.llm.bind_tools(langchain_tools)

        max_iterations = 10
        for iteration in range(max_iterations):
            logger.debug(f"LLM invocation iteration {iteration + 1}")
            response = await llm_with_tools.ainvoke(messages)

            messages.append(response)

            if hasattr(response, "tool_calls") and response.tool_calls:
                logger.info(f"LLM requested {len(response.tool_calls)} tool call(s)")
                messages = await self._execute_tool_calls(messages, response.tool_calls)
            else:
                # No more tool calls, this should be the final response
                logger.info("LLM returned final response (no tool calls)")
                if response.content:
                    break
                else:
                    logger.warning("Response has no content, continuing...")
        else:
            logger.warning(f"Max iterations ({max_iterations}) reached")

        final_content = response.content
        logger.info(f"Final content length: {len(final_content) if final_content else 0}")
        logger.debug(f"Final content preview: {final_content[:500] if final_content else 'EMPTY'}")

        if not final_content or not final_content.strip():
            raise ValueError("LLM returned empty response after all iterations")

        try:
            # Try to extract JSON if it's wrapped in markdown code blocks
            content_to_parse = final_content.strip()
            if content_to_parse.startswith("```"):
                # Extract content between ```json and ``` or ``` and ```
                lines = content_to_parse.split("\n")
                content_to_parse = "\n".join(lines[1:-1])  # Remove first and last lines

            factions = json.loads(content_to_parse)
            if not isinstance(factions, list):
                factions = [factions]

            logger.info(f"Successfully generated {len(factions)} faction(s)")
            return factions

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            logger.error(f"Response content: {final_content}")
            raise ValueError(f"LLM did not return valid JSON: {e}")

    async def generate_quest(self) -> dict[str, Any]:
        """Generate a quest for worldbuilding.

        Returns:
            Quest dictionary with structure:
            {
                "title": str,
                "quest_brief": str,
                "npcs": str,
                "conflict": str,
                "location": str
            }
        """
        logger.info("Generating quest")

        system_prompt = await self._build_system_prompt()
        langchain_tools = await self._get_langchain_tools()

        user_message = """Generate a unique quest for a tabletop RPG.

The quest should have:
- title: A compelling quest title
- quest_brief: Brief description of the quest (2-3 sentences)
- npcs: Key NPCs involved in the quest
- conflict: The main conflict or challenge
- location: Where the quest takes place

You should use ONLY the fetch_story tool to get random story elements to inspire your quest.

Respond with ONLY a JSON object, no additional text.
Format:
    {"title": "...", "quest_brief": "...", "npcs": "...", "conflict": "...", "location": "..."}
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_message),
        ]

        llm_with_tools = self.llm.bind_tools(langchain_tools)

        max_iterations = 10
        for iteration in range(max_iterations):
            logger.debug(f"LLM invocation iteration {iteration + 1}")
            response = await llm_with_tools.ainvoke(messages)

            messages.append(response)

            if hasattr(response, "tool_calls") and response.tool_calls:
                logger.info(f"LLM requested {len(response.tool_calls)} tool call(s)")
                messages = await self._execute_tool_calls(messages, response.tool_calls)
                # Continue loop to get final response after tool execution
            else:
                # No more tool calls, this should be the final response
                logger.info("LLM returned final response (no tool calls)")
                if response.content:
                    break
                else:
                    logger.warning("Response has no content, continuing...")
        else:
            logger.warning(f"Max iterations ({max_iterations}) reached")

        final_content = response.content
        logger.info(f"Final content length: {len(final_content) if final_content else 0}")
        logger.debug(f"Final content preview: {final_content[:500] if final_content else 'EMPTY'}")

        if not final_content or not final_content.strip():
            raise ValueError("LLM returned empty response after all iterations")

        try:
            # Try to extract JSON if it's wrapped in markdown code blocks
            content_to_parse = final_content.strip()
            if content_to_parse.startswith("```"):
                # Extract content between ```json and ``` or ``` and ```
                lines = content_to_parse.split("\n")
                content_to_parse = "\n".join(lines[1:-1])  # Remove first and last lines

            quest = json.loads(content_to_parse)

            logger.info("Successfully generated quest")
            return quest

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            logger.error(f"Response content: {final_content}")
            raise ValueError(f"LLM did not return valid JSON: {e}")


async def create_lore_generator(mcp_client: MCPClient) -> LoreGenerator:
    """Factory function to create a LoreGenerator instance.

    Args:
        mcp_client: Connected MCP client instance

    Returns:
        LoreGenerator instance ready for use
    """
    return LoreGenerator(mcp_client)
