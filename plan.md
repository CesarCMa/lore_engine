# Lore Engine - Detailed Development Plan

## Overview
Build a Python FastAPI backend for worldbuilding with MCP server integration, LangChain-powered LLM generation, using Poetry, Ruff, pytest, and Docker.

---

## **PHASE 1: Project Foundation (8 tasks)**

### Task 1.1: Initialize Poetry project ✓ COMPLETED
- Run `poetry init` in project root
- Configure: name="lore-engine", version="0.1.0", description="Worldbuilding lore generation API"
- Set Python version to "^3.13"

### Task 1.2: Add core dependencies ✓ COMPLETED
- Run `poetry add fastapi uvicorn[standard] python-dotenv pydantic-settings`
- Run `poetry add langchain langchain-openai openai`
- Run `poetry add mcp httpx`

### Task 1.3: Add development dependencies ✓ COMPLETED
- Run `poetry add --group dev ruff pytest pytest-asyncio pytest-cov httpx`
- Run `poetry add --group dev pre-commit`

### Task 1.4: Create project directory structure ✓ COMPLETED
- Create `src/lore_engine/` (main package)
- Create `src/lore_engine/api/` (FastAPI endpoints)
- Create `src/lore_engine/services/` (business logic)
- Create `src/lore_engine/mcp_server/` (MCP server code)
- Create `src/lore_engine/mcp_client/` (MCP client wrapper)
- Create `src/lore_engine/models/` (Pydantic models)
- Create `src/lore_engine/core/` (config, logging)
- Create `tests/` with subdirectories matching src structure

### Task 1.5: Configure Ruff in pyproject.toml ✓ COMPLETED
- Add `[tool.ruff]` section
- Set `line-length = 100`
- Configure `select = ["E", "F", "I", "N", "W"]` (rules)
- Add `exclude = [".git", "__pycache__", ".venv"]`

### Task 1.6: Create .pre-commit-config.yaml ✓ COMPLETED
- Add ruff linter hook (`ruff check --fix`)
- Add ruff formatter hook (`ruff format`)
- Set default_language_version to python3.13

### Task 1.7: Create comprehensive .gitignore ✓ COMPLETED
- Add Python patterns: `__pycache__/`, `*.py[cod]`, `.venv/`, `*.egg-info/`
- Add env files: `.env`, `.env.local`
- Add IDE: `.vscode/`, `.idea/`
- Add Docker: `docker-compose.override.yml`
- Add pytest: `.pytest_cache/`, `.coverage`

### Task 1.8: Initialize project files ✓ COMPLETED
- Create `src/lore_engine/__init__.py` (empty)
- Create `src/lore_engine/__main__.py` (entry point placeholder)
- Install pre-commit: `poetry run pre-commit install`

---

## **PHASE 2: Core Configuration (5 tasks)**

### Task 2.1: Create environment variable template ✓ COMPLETED
- Create `.env.example` with:
  - `OPENAI_API_KEY=your_key_here`
  - `MCP_SERVER_SCRIPT_PATH=src/lore_engine/mcp_server/server.py`
  - `LOG_LEVEL=INFO`

### Task 2.2: Create settings configuration ✓ COMPLETED
- Create `src/lore_engine/core/config.py`
- Define `Settings` class using `pydantic_settings.BaseSettings`
- Add fields: `openai_api_key`, `mcp_server_script_path`, `log_level`, `openai_model` (default="gpt-4o-mini")
- Add default for `mcp_server_script_path`: `"src/lore_engine/mcp_server/server.py"`
- Add `model_config = SettingsConfigDict(env_file=".env")`

### Task 2.3: Create settings instance ✓ COMPLETED
- In `src/lore_engine/core/config.py`, create `settings = Settings()`
- Export for use across app

### Task 2.4: Set up logging configuration ✓ COMPLETED
- Create `src/lore_engine/core/logging.py`
- Configure `logging.basicConfig()` with format, level from settings
- Create logger instance: `logger = logging.getLogger("lore_engine")`

### Task 2.5: Create core __init__.py ✓ COMPLETED
- Create `src/lore_engine/core/__init__.py`
- Export `settings` and `logger` for easy imports

---

## **PHASE 3: MCP Server Development (7 tasks)**

### Task 3.1: Create MCP server structure ✓ COMPLETED
- Create `src/lore_engine/mcp_server/__init__.py`
- Create `src/lore_engine/mcp_server/server.py`
- Import `FastMCP` from `mcp.server.fastmcp`
- Import `httpx` for HTTP requests

### Task 3.2: Initialize FastMCP server instance ✓ COMPLETED
- In `server.py`, create `mcp = FastMCP("lore-engine-mcp")`
- Add basic server configuration

### Task 3.3: Implement genre tool ✓ COMPLETED
- Create async function `fetch_genre()` in `server.py`
- Use `httpx.AsyncClient()` to GET `https://binaryjazz.us/wp-json/genrenator/v1/genre/`
- Parse JSON response, return genre string
- Decorate with `@mcp.tool()` decorator
- Add tool description: "Fetches a random genre from the Genrenator API"

### Task 3.4: Implement story tool ✓ COMPLETED
- Create async function `fetch_story()` in `server.py`
- Use `httpx.AsyncClient()` to GET `https://binaryjazz.us/wp-json/genrenator/v1/story/`
- Parse JSON response, return story string
- Decorate with `@mcp.tool()` decorator
- Add tool description: "Fetches a random story from the Genrenator API"

### Task 3.5: Add error handling to tools ✓ COMPLETED
- Wrap HTTP calls in try/except for `httpx.HTTPError`
- Return descriptive error messages
- Log errors using logger from core

### Task 3.6: Create MCP server main function ✓ COMPLETED
- Create `def main()` function in `server.py` (not async)
- Use `mcp.run(transport='stdio')` to run server
- Add proper error handling and logging

### Task 3.7: Create MCP server entry point ✓ COMPLETED
- In `server.py`, add `if __name__ == "__main__":` guard at bottom
- Call `main()` from the guard
- Alternatively, create `src/lore_engine/mcp_server/__main__.py` that imports and runs `main()` from `server.py`

---

## **PHASE 4: MCP Client Development (6 tasks)**

### Task 4.1: Create MCP client wrapper class ✓ COMPLETED
- Create `src/lore_engine/mcp_client/client.py`
- Define `MCPClient` class
- Import `ClientSession`, `StdioServerParameters` from `mcp`
- Import `stdio_client` from `mcp.client.stdio`
- Import `AsyncExitStack` from `contextlib`
- Add `__init__` to initialize session, exit_stack, and connection state

### Task 4.2: Implement client connection logic ✓ COMPLETED
- Add `async def connect(server_script_path: str)` method
- Create `StdioServerParameters` with command="poetry" and args=["run", "python", "-m", server_script_path]
- Use `AsyncExitStack` to manage stdio_client context
- Store `ClientSession` as instance variable after initialization
- Call `await session.initialize()`
- Add connection error handling and logging

### Task 4.3: Implement tool listing method ✓ COMPLETED
- Add `async def list_tools()` method to `MCPClient`
- Call `await self.session.list_tools()`
- Return list of available tools with names, descriptions, and input schemas
- Add error handling and logging

### Task 4.4: Implement generic tool calling method ✓ COMPLETED
- Add `async def call_tool(tool_name: str, arguments: dict)` method to `MCPClient`
- Call `await self.session.call_tool(tool_name, arguments)`
- Return tool result content
- Add error handling and logging

### Task 4.5: Add cleanup and retry logic ✓ COMPLETED
- Add `async def cleanup()` method to close `AsyncExitStack`
- Install `tenacity` library: `poetry add tenacity` ✓
- Decorate connection method with `@retry(stop=stop_after_attempt(3), wait=wait_exponential())` ✓
- Handle connection failures gracefully

### Task 4.6: Create client factory function ✓ COMPLETED
- Create `src/lore_engine/mcp_client/__init__.py`
- Add `async def get_mcp_client(server_script_path: str)` factory function
- Create `MCPClient` instance, call `connect()`, return connected instance
- Use server script path from settings or configuration

---

## **PHASE 5: LangChain & LLM Integration (8 tasks)**

### Task 5.1: Create LLM service structure
- Create `src/lore_engine/services/__init__.py`
- Create `src/lore_engine/services/lore_generator.py`

### Task 5.2: Initialize LangChain OpenAI LLM with MCP client
- In `lore_generator.py`, import `ChatOpenAI` from `langchain_openai`
- Import `StructuredTool` from `langchain_core.tools`
- Create `LoreGenerator` class with `__init__(mcp_client)`
- Store MCP client as instance variable
- Initialize `ChatOpenAI` with model from settings (gpt-4o-mini)
- Store LLM as instance variable

### Task 5.3: Create tool discovery and conversion method
- Add `async def _get_langchain_tools()` method to `LoreGenerator`
- Call `await self.mcp_client.list_tools()` to get available tools
- Convert each MCP tool to LangChain `StructuredTool` with:
  - Tool name and description from MCP tool
  - Input schema from MCP tool's `inputSchema`
  - Async function that calls `self.mcp_client.call_tool()`
- Return list of LangChain tools

### Task 5.4: Create system prompt with tool information
- Add `async def _build_system_prompt()` method
- Get available tools using `_get_langchain_tools()`
- Build system prompt that describes:
  - Purpose: generate factions and quests for worldbuilding
  - Available tools and their descriptions
  - Instructions to use tools when needed (e.g., fetch genres/stories)
- Store prompt template as instance variable

### Task 5.5: Implement tool calling handler
- Add `async def _execute_tool_calls(tool_calls, messages)` method
- Process LLM tool calls from response
- For each tool call, execute via MCP client
- Add tool results as messages to conversation
- Return updated messages list

### Task 5.6: Implement generate_faction method
- Add `async def generate_faction(count: int = 1)` to `LoreGenerator`
- Get system prompt with tools
- Create user message requesting faction generation
- Bind tools to LLM using `llm.bind_tools(langchain_tools)`
- Invoke LLM and handle tool calls (fetch genres) if needed
- Continue conversation until LLM returns final JSON response
- Parse JSON response into dict with structure: name, symbol, values, soundtrack_vibe
- If `count > 1`, generate multiple factions
- Add error handling for malformed JSON

### Task 5.7: Implement generate_quest method
- Add `async def generate_quest()` to `LoreGenerator`
- Get system prompt with tools
- Create user message requesting quest generation
- Bind tools to LLM
- Invoke LLM and handle tool calls (fetch story) if needed
- Continue conversation until LLM returns final JSON response
- Parse JSON response into dict with structure: title, quest_brief, npcs, conflict, location
- Add error handling

### Task 5.8: Create service initialization
- In `services/__init__.py`, create async factory function `async def create_lore_generator(mcp_client)`
- Return `LoreGenerator` instance with connected MCP client
- Export factory function for use in API endpoints

---

## **PHASE 6: FastAPI Application (11 tasks)**

### Task 6.1: Create Pydantic models
- Create `src/lore_engine/models/responses.py`
- Define `FactionResponse` model: name, symbol, values, soundtrack_vibe
- Define `QuestResponse` model: title, quest_brief, npcs, conflict, location
- Define `FactionsResponse` model: factions (list of FactionResponse)

### Task 6.2: Create FastAPI app instance
- Create `src/lore_engine/api/app.py`
- Initialize `app = FastAPI(title="Lore Engine", version="0.1.0")`
- Add description with API purpose

### Task 6.3: Set up dependency injection for MCP client
- Create dependency function `async def get_mcp_client()`
- Use `get_mcp_client()` factory from `mcp_client` module
- Get server script path from settings
- Return connected MCP client instance
- Use FastAPI's `Depends()` for dependency injection in routes

### Task 6.4: Add CORS middleware
- Import `CORSMiddleware` from `fastapi.middleware.cors`
- Configure to allow all origins (or specify allowed origins)
- Add to app with `app.add_middleware()`

### Task 6.5: Create health check endpoint
- In `app.py`, add `@app.get("/health")`
- Return `{"status": "healthy", "timestamp": datetime.now()}`
- Add response model: `dict[str, Any]`

### Task 6.6: Create factions endpoint structure
- Create `src/lore_engine/api/routes/factions.py`
- Create `router = APIRouter(prefix="/factions", tags=["factions"])`

### Task 6.7: Implement factions endpoint logic
- Add `@router.get("/{count}", response_model=FactionsResponse)`
- Parameter: `count: int = Path(ge=1, le=10)` (1-10 factions)
- Get MCP client instance via `Depends(get_mcp_client)`
- Create `LoreGenerator` instance with MCP client using `create_lore_generator()`
- Call `await lore_generator.generate_faction(count=count)`
- Return `FactionsResponse` with generated factions
- Add error handling and logging

### Task 6.8: Create quests endpoint structure
- Create `src/lore_engine/api/routes/quests.py`
- Create `router = APIRouter(prefix="/quests", tags=["quests"])`

### Task 6.9: Implement quest endpoint logic
- Add `@router.get("/", response_model=QuestResponse)`
- Get MCP client instance via `Depends(get_mcp_client)`
- Create `LoreGenerator` instance with MCP client using `create_lore_generator()`
- Call `await lore_generator.generate_quest()`
- Return `QuestResponse` with generated quest
- Add error handling and logging

### Task 6.10: Register routers in main app
- In `app.py`, import routers from `routes.factions` and `routes.quests`
- Add with `app.include_router(factions_router)`
- Add with `app.include_router(quests_router)`

### Task 6.11: Create app entry point
- Update `src/lore_engine/__main__.py`
- Add uvicorn run: `uvicorn.run("lore_engine.api.app:app", host="0.0.0.0", port=8000, reload=True)`

---

## **PHASE 7: Testing (9 tasks)**

### Task 7.1: Configure pytest
- Create `pyproject.toml` section `[tool.pytest.ini_options]`
- Set `testpaths = ["tests"]`
- Set `python_files = ["test_*.py"]`
- Add `asyncio_mode = "auto"`

### Task 7.2: Create test fixtures
- Create `tests/conftest.py`
- Add fixture `mock_mcp_client()` returning mock MCP client
- Add fixture `mock_lore_generator()` returning mock generator
- Add fixture `test_client()` returning FastAPI `TestClient`

### Task 7.3: Write MCP server tool tests ✓ COMPLETED
- Create `tests/mcp_server/test_server.py` ✓
- Test `fetch_genre()` returns string ✓
- Test `fetch_story()` returns string ✓

### Task 7.4: Write MCP client tests
- Create `tests/mcp_client/test_client.py`
- Test `connect()` establishes connection and initializes session
- Test `list_tools()` returns list of available tools
- Test `call_tool()` executes tool calls and returns results
- Test `cleanup()` properly closes connections
- Test retry logic on connection failures
- Mock `ClientSession` and `stdio_client` for testing

### Task 7.5: Write LoreGenerator unit tests
- Create `tests/services/test_lore_generator.py`
- Mock MCP client with `list_tools()` and `call_tool()` methods
- Test `_get_langchain_tools()` converts MCP tools to LangChain tools
- Test `generate_faction()` with mock LLM that calls tools (e.g., fetch_genre)
- Test `generate_quest()` with mock LLM that calls tools (e.g., fetch_story)
- Test tool calling flow: LLM request → tool call → tool result → final response
- Verify JSON parsing works correctly
- Test error handling for tool call failures

### Task 7.6: Write factions endpoint tests
- Create `tests/api/test_factions.py`
- Test GET `/factions/3` returns 3 factions
- Test validation: count < 1 returns 422
- Test validation: count > 10 returns 422

### Task 7.7: Write quests endpoint tests
- Create `tests/api/test_quests.py`
- Test GET `/quests/` returns valid quest
- Mock MCP client and LLM responses

### Task 7.8: Add integration test
- Create `tests/integration/test_full_flow.py`
- Test end-to-end: API call → MCP client → LLM → response
- Use real MCP server (or containerized mock)

### Task 7.9: Add test coverage reporting
- Run `poetry run pytest --cov=src/lore_engine --cov-report=html`
- Verify coverage > 80%
- Add coverage badge to README (optional)

---

## **PHASE 8: Docker & Deployment (6 tasks)**

### Task 8.1: Create Dockerfile
- Create `Dockerfile` in project root
- Base: `FROM python:3.13-slim` (match Python version from project)
- Install Poetry: `pip install poetry`
- Set working directory
- Copy `pyproject.toml` and `poetry.lock` (if exists)
- Install dependencies with `poetry install --no-dev`
- Copy source code: `COPY src/ src/`
- Set Python path to include `src/`
- EXPOSE 8000
- CMD: run uvicorn with app
- Note: MCP server code is included in the same image and runs as subprocess

### Task 8.2: Create docker-compose.yaml
- Define single service: `api`
- `api`: build from Dockerfile, ports 8000:8000
- Note: MCP server runs as subprocess via stdio within the same container
- Add shared network (if needed for future services)

### Task 8.3: Add environment variables to compose
- Create `env_file` directive in docker-compose
- Mount `.env` file to container
- Ensure `MCP_SERVER_SCRIPT_PATH` points to correct path in container (e.g., `src/lore_engine/mcp_server/server.py`)
- Optionally override script path for containerized environment

### Task 8.4: Create .dockerignore
- Add: `.git`, `__pycache__`, `.venv`, `.pytest_cache`
- Add: `.env` (use .env.example instead)
- Add: `tests/`, `*.md`
- Add: `.dockerignore`, `docker-compose.yaml`

### Task 8.5: Test Docker build
- Run `docker-compose build`
- Verify image builds successfully
- Check for any missing dependencies
- Verify MCP server code is included in image

### Task 8.6: Test Docker deployment
- Run `docker-compose up`
- Test health endpoint: `curl http://localhost:8000/health`
- Test factions endpoint: `curl http://localhost:8000/factions/1`
- Verify MCP server subprocess spawns correctly when tools are called

---

## **PHASE 9: Documentation & Polish (6 tasks)**

### Task 9.1: Update README with project overview
- Add project description, features list
- Add architecture diagram (text-based)
- List technologies used

### Task 9.2: Add setup instructions to README
- Document Poetry installation
- Document `.env` setup with API keys
- Document `poetry install` and `poetry run` commands

### Task 9.3: Add API usage examples
- Document `/factions/{count}` endpoint with curl example
- Document `/quests/` endpoint with curl example
- Show example responses

### Task 9.4: Add Docker instructions
- Document Docker Compose setup
- Document environment variable configuration
- Add troubleshooting section

### Task 9.5: Add code documentation
- Add docstrings to all classes and public methods
- Use Google-style docstrings
- Document parameters and return types

### Task 9.6: Create development guide
- Document how to run tests
- Document pre-commit setup
- Document code formatting with Ruff
- Add contributing guidelines
