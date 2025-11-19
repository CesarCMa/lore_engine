# Lore Engine Backend

Fantasy worldbuilding API for generating factions and quests for tabletop RPGs.

## Tech Stack

- FastAPI
- Python 3.10+
- LangChain + OpenAI
- Poetry for dependency management

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

3. Run the server:
```bash
make run
```

The API will be available at `http://localhost:8000`

## Development

Run tests:
```bash
make unit-tests
```

Run with logging:
```bash
make run-logs
```

## API Endpoints

- `GET /factions/{count}` - Generate N factions (1-10)
- `POST /quests/` - Generate a quest (optionally based on provided factions)
- `GET /docs` - Interactive API documentation

## Project Structure

```
backend/
├── src/lore_engine/       # Source code
│   ├── api/              # FastAPI application
│   ├── agents/           # LangChain agents
│   └── models/           # Pydantic models
├── tests/                # Test suite
├── pyproject.toml        # Dependencies
└── Makefile              # Common commands
```
