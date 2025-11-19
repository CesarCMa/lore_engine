# Lore Engine Monorepo

Fantasy worldbuilding tool for generating factions and quests for tabletop RPGs.

## Project Structure

- `backend/` - FastAPI Python backend with LangChain agents
- `frontend/` - React JavaScript frontend (coming soon)
- `docs/` - Documentation and style guides (coming soon)

## Quick Start

### Backend

```bash
cd backend
poetry install
cp .env.example .env
# Edit .env and add your OpenAI API key
make run
```

The API will be available at `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Features

- **Faction Generator**: Create rich, detailed factions with symbols, values, and soundtrack vibes
- **Quest Generator**: Generate engaging quests standalone or based on existing factions
- **MCP Integration**: Powered by Model Context Protocol for enhanced AI capabilities

## Environment Variables

See `backend/.env.example` for required configuration.

## Development

Each subdirectory has its own README with detailed setup and development instructions.

- Backend: See `backend/README.md`
- Frontend: See `frontend/README.md` (coming soon)

## Tech Stack

**Backend:**
- FastAPI
- Python 3.10+
- LangChain + OpenAI
- Poetry

**Frontend:**
- React 18
- Vite
- Tailwind CSS
- Axios

## License

MIT
