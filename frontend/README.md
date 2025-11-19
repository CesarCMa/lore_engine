# Lore Engine Frontend

Fantasy-themed React application for generating factions and quests.

## Tech Stack

- React 18
- Vite
- JavaScript
- Tailwind CSS
- Axios
- Lucide React (icons)
- React Hot Toast (notifications)

## Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment variables:
```bash
# Create .env file
echo "VITE_API_URL=http://localhost:8000" > .env
```

3. Start development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Development

```bash
npm run dev      # Start dev server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

## Features

- Generate 1-10 factions with fantasy theming
- Generate quests standalone or based on factions
- Copy individual items or export all as JSON/Markdown
- Polished fantasy UI with custom fonts and colors

## Fantasy Theme

The application uses a custom fantasy theme with:

- **Fonts:**
  - Cinzel (headings) - ornate serif
  - Crimson Text (body) - readable serif
  - MedievalSharp (accent) - decorative text

- **Color Palette:**
  - Arcane Purple - primary magical theme
  - Mystic Gold - secondary highlights
  - Dragon Crimson - accent/danger states
  - Parchment - neutral backgrounds

## Project Structure

```
frontend/src/
├── main.jsx                   # Entry point
├── App.jsx                    # Root component
├── index.css                  # Tailwind imports + global styles
│
├── components/                # Reusable UI components
│   ├── ui/                    # Base UI components
│   ├── FactionCard.jsx
│   ├── QuestCard.jsx
│   ├── FactionList.jsx
│   ├── QuestDisplay.jsx
│   └── GeneratorControls.jsx
│
├── pages/                     # Page components
│   ├── FactionsPage.jsx
│   └── QuestsPage.jsx
│
├── services/                  # API integration
│   └── api.js
│
├── utils/                     # Utility functions
│   ├── export.js
│   └── clipboard.js
│
└── styles/                    # Additional styles
    └── fantasy-theme.css
```

## Environment Variables

- `VITE_API_URL` - Backend API URL (default: http://localhost:8000)
