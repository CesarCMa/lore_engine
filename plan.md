# Monorepo Refactoring & Fantasy Frontend Implementation Plan

## Overview
Refactor the lore_engine repository into a simple monorepo with `backend/` and `frontend/` folders, then build a polished fantasy-themed React frontend using Vite, JavaScript, and Tailwind CSS.

---

## Phase 1: Monorepo Restructuring

### 1.1 Create New Directory Structure
```
lore_engine/
├── backend/                    # Move all Python code here
│   ├── src/lore_engine/       # Existing source code
│   ├── tests/                 # Existing tests
│   ├── pyproject.toml         # Move from root
│   ├── poetry.lock            # Move from root
│   ├── Makefile               # Move from root
│   ├── .env.example           # Move from root
│   └── README.md              # Backend-specific docs
│
├── frontend/                   # New frontend application
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── .eslintrc.cjs
│   └── README.md
│
├── .github/                    # CI/CD workflows (optional)
├── docs/                       # Shared documentation
│   └── STYLE_GUIDE.md         # Fantasy theme style guide
├── .gitignore                 # Root gitignore
├── README.md                  # Monorepo overview
```

### 1.2 Move Backend Files
- Move `src/`, `tests/`, `pyproject.toml`, `poetry.lock`, `Makefile` to `backend/`
- Move `.env.example` to `backend/`
- Update `backend/Makefile` paths if needed
- Update `backend/.env.example` to add `FRONTEND_URL=http://localhost:5173`
- Keep `.git/` at root (preserve history)

### 1.3 Update Backend Configuration
- Update CORS in `backend/src/lore_engine/api/app.py`:
  - Change `allow_origins=["*"]` to `allow_origins=["http://localhost:5173", "http://localhost:8000"]` for development
  - Add production frontend URL to allowed origins
- Update `backend/README.md` with new paths and setup instructions
- Ensure all import paths still work correctly

### 1.4 Root-Level Configuration
- Create root `README.md` with monorepo overview and quickstart
- Create root `.gitignore` combining Python and Node patterns

---

## Phase 2: Frontend Scaffolding

### 2.1 Initialize Vite + React Project (JavaScript)
```bash
cd frontend
npm create vite@latest . -- --template react
npm install
```

### 2.2 Install Dependencies
**Core:**
- `react`, `react-dom` (from template)
- `axios` (API calls)

**UI/Styling:**
- `tailwindcss`, `postcss`, `autoprefixer`
- `@tailwindcss/typography` (for rich text)
- `lucide-react` (fantasy-friendly icons)

**Utilities:**
- `clsx` (conditional classes)
- `react-hot-toast` (notifications)

**Dev:**
- `eslint`, `eslint-plugin-react` (linting)

### 2.3 Configure Tailwind CSS
- Initialize: `npx tailwindcss init -p`
- Configure `tailwind.config.js` with:
  - Custom fantasy color palette (deep purples, golds, crimsons)
  - Custom font families (serif for headings, fantasy fonts)
  - Extended shadows and border utilities
  - Content paths: `content: ["./index.html", "./src/**/*.{js,jsx}"]`
- Create `src/index.css` with Tailwind directives and custom base styles

### 2.4 Setup Project Structure
```
frontend/src/
├── main.jsx                   # Entry point
├── App.jsx                    # Root component
├── index.css                  # Tailwind imports + global styles
│
├── components/                # Reusable UI components
│   ├── ui/                    # Base UI components
│   │   ├── Button.jsx
│   │   ├── Card.jsx
│   │   ├── Input.jsx
│   │   ├── Select.jsx
│   │   └── LoadingSpinner.jsx
│   │
│   ├── FactionCard.jsx        # Display faction with fantasy styling
│   ├── QuestCard.jsx          # Display quest details
│   ├── FactionList.jsx        # Grid of faction cards
│   ├── QuestDisplay.jsx       # Quest details with NPCs
│   └── GeneratorControls.jsx  # Count selector, generate buttons
│
├── pages/                     # Page components
│   ├── FactionsPage.jsx       # Faction generator page
│   ├── QuestsPage.jsx         # Quest generator page
│   └── HomePage.jsx           # Landing/intro page (optional)
│
├── services/                  # API integration
│   └── api.js                 # Axios setup + API functions
│
├── utils/                     # Utility functions
│   ├── export.js              # Export to JSON/Markdown
│   └── clipboard.js           # Copy to clipboard helpers
│
└── styles/                    # Additional styles
    └── fantasy-theme.css      # Custom fantasy decorations
```

---

## Phase 3: Fantasy Theme Style Guide & Design System

### 3.1 Create `docs/STYLE_GUIDE.md`

**Typography:**
- **Headings:** "Cinzel" (Google Font) - ornate serif for titles
- **Body:** "Crimson Text" (Google Font) - readable serif
- **Accent:** "MedievalSharp" (Google Font) - for special decorative text
- Load via Google Fonts CDN in `index.html`

**Color Palette:**
```javascript
// Primary (Arcane Purple)
arcane: {
  50: '#F3E8F7',
  100: '#E1C9EE',
  200: '#C599DD',
  300: '#A969CC',
  400: '#8D39BB',
  500: '#6B2C6B',  // Main
  600: '#4A1A4A',
  700: '#3B153B',
  800: '#2C102C',
  900: '#1D0A1D',
}

// Secondary (Mystic Gold)
gold: {
  50: '#FFFBEB',
  100: '#FEF3C7',
  200: '#FDE68A',
  300: '#FCD34D',
  400: '#FBBF24',
  500: '#D4AF37',  // Main
  600: '#B8960F',
  700: '#92750A',
  800: '#6C5608',
  900: '#463705',
}

// Accent (Dragon Crimson)
crimson: {
  50: '#FEF2F2',
  100: '#FEE2E2',
  200: '#FECACA',
  300: '#FCA5A5',
  400: '#F87171',
  500: '#DC143C',  // Main
  600: '#B22222',
  700: '#8B0000',
  800: '#660000',
  900: '#4D0000',
}

// Neutral (Parchment)
parchment: {
  50: '#FDFCFA',
  100: '#F5E6D3',
  200: '#E8D7C3',
  300: '#D4C4B0',
  400: '#C0B29D',
  500: '#ACA08A',
  600: '#8B7D6B',
  700: '#6A5F52',
  800: '#4A423A',
  900: '#2A2521',
}
```

**Component Guidelines:**
- **Cards:** Parchment background (#F5E6D3) with ornate borders (2px gold), subtle box shadows
- **Buttons:** Raised effect with gold/crimson gradients, hover scale transform (1.02), transition duration 200ms
- **Inputs:** 2px border with focus ring (arcane purple), rounded-lg, parchment background
- **Icons:** lucide-react icons, colored with theme colors (gold for actions, crimson for delete, purple for magic)
- **Decorations:** CSS pseudo-elements for corner flourishes, SVG dividers with scroll patterns

**Visual Effects:**
- Paper texture background: subtle noise or parchment image overlay
- Glow effects: `box-shadow: 0 0 20px rgba(107, 44, 107, 0.3)`
- Fade-in animations: `animate-fadeIn` custom Tailwind animation
- Hover transforms: `hover:scale-105 transition-transform duration-200`

### 3.2 Implement Design Tokens in Tailwind Config
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        arcane: { /* ... */ },
        gold: { /* ... */ },
        crimson: { /* ... */ },
        parchment: { /* ... */ },
      },
      fontFamily: {
        heading: ['Cinzel', 'serif'],
        body: ['Crimson Text', 'serif'],
        accent: ['MedievalSharp', 'cursive'],
      },
      boxShadow: {
        'arcane': '0 0 20px rgba(107, 44, 107, 0.3)',
        'gold': '0 0 15px rgba(212, 175, 55, 0.4)',
        'parchment': '0 4px 6px rgba(0, 0, 0, 0.1)',
      },
      animation: {
        'fadeIn': 'fadeIn 0.5s ease-in-out',
        'slideUp': 'slideUp 0.4s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
}
```

---

## Phase 4: Frontend Implementation

### 4.1 API Integration (`services/api.js`)
```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: { 'Content-Type': 'application/json' }
});

export const generateFactions = async (count) => {
  const response = await api.get(`/factions/${count}`);
  return response.data;
};

export const generateQuest = async (factions = null) => {
  const response = await api.post('/quests/', 
    factions ? { factions } : {}
  );
  return response.data;
};
```

### 4.2 Core Components

**FactionCard.jsx:**
- Props: `faction` object, `onCopy` callback
- Display faction name as ornate heading (font-heading)
- Show symbol with scroll icon from lucide-react
- Render values with quote styling
- Display soundtrack vibe with music note icon
- Copy button with clipboard icon
- Fantasy-themed card: parchment background, gold border, shadow-parchment
- Hover effect: scale-105, shadow-gold

**QuestCard.jsx:**
- Props: `quest` object, `onCopy` callback
- Quest title with dramatic typography (text-3xl font-heading)
- Brief in story format (font-body, italic)
- NPCs section with character icons (parse string or array)
- Conflict highlighted with swords icon and crimson accent
- Location with map-pin icon
- Copy/export buttons (styled with Button component)

**GeneratorControls.jsx:**
- Props: `onGenerate` callback, `isLoading` boolean, `count` state, `setCount` function
- Count selector: Input with +/- buttons (1-10 range validation)
- Generate button: primary gold gradient, loading spinner when active
- Clear/reset button: secondary style
- Disabled state when loading

**FactionList.jsx:**
- Props: `factions` array, `onCopyFaction` callback, `onSelectFaction` callback (optional)
- Responsive grid: grid-cols-1 md:grid-cols-2 lg:grid-cols-3
- Map over factions, render FactionCard for each
- Empty state: centered message with scroll icon
- Animate children with stagger effect (slideUp animation)

**QuestDisplay.jsx:**
- Props: `quest` object, `onCopy` callback
- Full-width QuestCard with enhanced styling
- If quest has faction-based NPCs, show faction badges
- Highlight conflict section with decorative borders
- "Generate Another" button

### 4.3 UI Components Library

**Button.jsx:**
- Props: `children`, `variant`, `size`, `isLoading`, `disabled`, `onClick`
- Variants:
  - `primary`: bg-gradient-to-r from-gold-500 to-gold-600, text-white
  - `secondary`: bg-arcane-600, text-white
  - `danger`: bg-crimson-600, text-white
  - `outline`: border-2 border-gold-500, text-gold-600
- Sizes: `sm` (px-3 py-1.5), `md` (px-4 py-2), `lg` (px-6 py-3)
- Loading state: show LoadingSpinner, disable button
- Hover: scale-105, brightness-110, transition-all duration-200
- Disabled: opacity-50, cursor-not-allowed

**Card.jsx:**
- Props: `children`, `className`, `title`, `footer`
- Base: bg-parchment-100, border-2 border-gold-500, rounded-lg, p-6, shadow-parchment
- Optional title section: border-b border-gold-300, pb-3, mb-4
- Optional footer section: border-t border-gold-300, pt-3, mt-4
- Merge custom className with clsx

**Input.jsx:**
- Props: `type`, `value`, `onChange`, `placeholder`, `error`
- Base: bg-parchment-50, border-2 border-gold-400, rounded-lg, px-4 py-2, font-body
- Focus: ring-2 ring-arcane-500, border-arcane-500
- Error state: border-crimson-500, ring-crimson-500
- Error message: text-crimson-600, text-sm, mt-1

**Select.jsx:**
- Props: `value`, `onChange`, `options`, `placeholder`
- Styled select: bg-parchment-50, border-2 border-gold-400, rounded-lg, px-4 py-2
- Custom arrow icon (chevron-down from lucide-react)
- Focus state: ring-2 ring-arcane-500

**LoadingSpinner.jsx:**
- Rotating compass or arcane circle SVG
- Purple-to-gold gradient animation
- Size variants: sm (w-4 h-4), md (w-8 h-8), lg (w-12 h-12)
- Smooth rotation: animate-spin

---

## Phase 5: Pages Implementation

### 5.1 FactionsPage.jsx
```javascript
import { useState } from 'react';
import { generateFactions } from '../services/api';
import GeneratorControls from '../components/GeneratorControls';
import FactionList from '../components/FactionList';
import Button from '../components/ui/Button';
import { exportToJSON, exportToMarkdown } from '../utils/export';
import { copyToClipboard } from '../utils/clipboard';
import toast from 'react-hot-toast';

export default function FactionsPage() {
  const [factions, setFactions] = useState([]);
  const [count, setCount] = useState(3);
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerate = async () => {
    setIsLoading(true);
    try {
      const data = await generateFactions(count);
      setFactions(data.factions);
      toast.success(`Generated ${count} factions!`);
    } catch (error) {
      toast.error('Failed to generate factions');
    } finally {
      setIsLoading(false);
    }
  };

  const handleCopyFaction = (faction) => {
    copyToClipboard(JSON.stringify(faction, null, 2));
    toast.success('Faction copied to clipboard!');
  };

  const handleExportAll = (format) => {
    const content = format === 'json' 
      ? exportToJSON(factions) 
      : exportToMarkdown(factions, 'faction');
    copyToClipboard(content);
    toast.success(`Exported as ${format.toUpperCase()}!`);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="text-center mb-12">
        <h1 className="text-5xl font-heading text-arcane-700 mb-4">
          Faction Forge
        </h1>
        <p className="text-xl font-body text-parchment-700">
          Craft powerful factions for your fantasy world
        </p>
      </header>

      <GeneratorControls
        count={count}
        setCount={setCount}
        onGenerate={handleGenerate}
        isLoading={isLoading}
      />

      {factions.length > 0 && (
        <div className="flex gap-4 justify-center mb-8">
          <Button onClick={() => handleExportAll('json')}>
            Export JSON
          </Button>
          <Button variant="outline" onClick={() => handleExportAll('markdown')}>
            Export Markdown
          </Button>
        </div>
      )}

      <FactionList
        factions={factions}
        onCopyFaction={handleCopyFaction}
      />
    </div>
  );
}
```

### 5.2 QuestsPage.jsx
```javascript
import { useState } from 'react';
import { generateQuest } from '../services/api';
import Button from '../components/ui/Button';
import QuestDisplay from '../components/QuestDisplay';
import FactionList from '../components/FactionList';
import { copyToClipboard } from '../utils/clipboard';
import toast from 'react-hot-toast';

export default function QuestsPage() {
  const [quest, setQuest] = useState(null);
  const [mode, setMode] = useState('fresh'); // 'fresh' or 'factions'
  const [selectedFactions, setSelectedFactions] = useState([]);
  const [availableFactions, setAvailableFactions] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleGenerate = async () => {
    setIsLoading(true);
    try {
      const factionInput = mode === 'factions' ? selectedFactions : null;
      const data = await generateQuest(factionInput);
      setQuest(data);
      toast.success('Quest generated!');
    } catch (error) {
      toast.error('Failed to generate quest');
    } finally {
      setIsLoading(false);
    }
  };

  const handleCopyQuest = () => {
    copyToClipboard(JSON.stringify(quest, null, 2));
    toast.success('Quest copied to clipboard!');
  };

  const toggleFactionSelection = (faction) => {
    setSelectedFactions(prev => 
      prev.find(f => f.name === faction.name)
        ? prev.filter(f => f.name !== faction.name)
        : [...prev, faction]
    );
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <header className="text-center mb-12">
        <h1 className="text-5xl font-heading text-arcane-700 mb-4">
          Quest Weaver
        </h1>
        <p className="text-xl font-body text-parchment-700">
          Weave epic adventures for your tabletop campaigns
        </p>
      </header>

      <div className="flex justify-center gap-4 mb-8">
        <Button
          variant={mode === 'fresh' ? 'primary' : 'outline'}
          onClick={() => setMode('fresh')}
        >
          Generate Fresh Quest
        </Button>
        <Button
          variant={mode === 'factions' ? 'primary' : 'outline'}
          onClick={() => setMode('factions')}
        >
          Use Factions
        </Button>
      </div>

      {mode === 'factions' && (
        <div className="mb-8">
          {/* Faction selection UI */}
          <p className="text-center font-body mb-4">
            Select factions to base your quest on:
          </p>
          <FactionList
            factions={availableFactions}
            onSelectFaction={toggleFactionSelection}
            selectedFactions={selectedFactions}
          />
        </div>
      )}

      <div className="flex justify-center mb-8">
        <Button
          size="lg"
          onClick={handleGenerate}
          isLoading={isLoading}
        >
          Generate Quest
        </Button>
      </div>

      {quest && (
        <QuestDisplay quest={quest} onCopy={handleCopyQuest} />
      )}
    </div>
  );
}
```

### 5.3 App.jsx (Simple Navigation)
```javascript
import { useState } from 'react';
import { Toaster } from 'react-hot-toast';
import FactionsPage from './pages/FactionsPage';
import QuestsPage from './pages/QuestsPage';
import Button from './components/ui/Button';

function App() {
  const [currentPage, setCurrentPage] = useState('factions');

  return (
    <div className="min-h-screen bg-gradient-to-b from-parchment-200 to-parchment-100">
      <nav className="bg-arcane-700 text-white shadow-lg">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-heading">Lore Engine</h1>
          <div className="flex gap-4">
            <Button
              variant={currentPage === 'factions' ? 'primary' : 'outline'}
              onClick={() => setCurrentPage('factions')}
            >
              Factions
            </Button>
            <Button
              variant={currentPage === 'quests' ? 'primary' : 'outline'}
              onClick={() => setCurrentPage('quests')}
            >
              Quests
            </Button>
          </div>
        </div>
      </nav>

      <main>
        {currentPage === 'factions' ? <FactionsPage /> : <QuestsPage />}
      </main>

      <Toaster position="bottom-right" />
    </div>
  );
}

export default App;
```

---

## Phase 6: Utility Functions

### 6.1 Export Utils (`utils/export.js`)
```javascript
export const exportToJSON = (data) => {
  return JSON.stringify(data, null, 2);
};

export const exportToMarkdown = (items, type) => {
  if (type === 'faction') {
    return items.map(f => `
## ${f.name}

**Symbol:** ${f.symbol}

**Values:** ${f.values}

**Soundtrack:** ${f.soundtrack_vibe}

---
    `).join('\n');
  }
  
  // Similar for quest type
};
```

### 6.2 Clipboard Utils (`utils/clipboard.js`)
```javascript
export const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    // Fallback for older browsers
    const textArea = document.createElement('textarea');
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    return true;
  }
};
```

---

## Phase 7: Polish & Finalization

### 7.1 Add Paper Texture Background
- Download or create subtle parchment texture image
- Add to `public/textures/parchment.png`
- Apply in `index.css`:
```css
body {
  background-image: url('/textures/parchment.png');
  background-repeat: repeat;
}
```

### 7.2 Custom CSS Decorations (`styles/fantasy-theme.css`)
```css
/* Corner flourishes using pseudo-elements */
.ornate-card::before,
.ornate-card::after {
  content: '';
  position: absolute;
  width: 40px;
  height: 40px;
  background-image: url('/icons/corner-flourish.svg');
  background-size: contain;
}

.ornate-card::before {
  top: -2px;
  left: -2px;
}

.ornate-card::after {
  bottom: -2px;
  right: -2px;
  transform: rotate(180deg);
}

/* Scroll dividers */
.scroll-divider {
  height: 2px;
  background: linear-gradient(to right, transparent, #D4AF37, transparent);
  position: relative;
}
```

### 7.3 Responsive Design
- Mobile-first approach
- Breakpoints: sm (640px), md (768px), lg (1024px)
- Stack navigation buttons vertically on mobile
- Single column grid for cards on mobile
- Adjust font sizes for smaller screens

### 7.4 Accessibility
- All buttons have descriptive aria-labels
- Keyboard navigation with visible focus states
- Color contrast ratios meet WCAG AA standards
- Alt text for all decorative images

### 7.5 Error Handling
- Network error toast: "Failed to connect to server. Please try again."
- Validation errors for count input (1-10)
- Loading states prevent duplicate requests
- Graceful degradation if fonts don't load

---

## Phase 8: Documentation

### 8.1 Root README.md
```markdown
# Lore Engine Monorepo

Fantasy worldbuilding tool for generating factions and quests for tabletop RPGs.

## Project Structure
- `backend/` - FastAPI Python backend
- `frontend/` - React JavaScript frontend
- `docs/` - Documentation and style guides

## Quick Start

### Backend
cd backend
poetry install
poetry run python -m lore_engine

### Frontend
cd frontend
npm install
npm run dev

## Environment Variables
See `backend/.env.example` for required configuration.
```

### 8.2 Frontend README.md
```markdown
# Lore Engine Frontend

Fantasy-themed React application for generating factions and quests.

## Tech Stack
- React 18
- Vite
- Tailwind CSS
- Axios
- Lucide React (icons)

## Development
npm run dev      # Start dev server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint

## Features
- Generate 1-10 factions with fantasy theming
- Generate quests standalone or based on factions
- Copy individual items or export all as JSON/Markdown
- Polished fantasy UI with custom fonts and colors
```

### 8.3 Style Guide (`docs/STYLE_GUIDE.md`)
Complete documentation with:
- Color palette with hex codes
- Typography specimens
- Component examples with code snippets
- Usage guidelines
- Accessibility notes

---

## Phase 9: Final Integration & Testing

### 9.1 Environment Configuration
- Create `frontend/.env`:
```
VITE_API_URL=http://localhost:8000
```
- Update `backend/.env` CORS settings

### 9.2 Integration Testing
- Start backend: `cd backend && make run`
- Start frontend: `cd frontend && npm run dev`
- Test all features end-to-end:
  - Generate factions (various counts)
  - Copy individual factions
  - Export all factions
  - Generate fresh quest
  - Generate quest from factions
  - Copy quest
  - Error handling (stop backend, try generating)

### 9.3 Cross-Browser Testing
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

### 9.4 Mobile Testing
- Responsive design on mobile devices
- Touch interactions work correctly
- No horizontal scrolling

---

## Deliverables

1. ✅ **Restructured monorepo** with `backend/` and `frontend/` folders
2. ✅ **Frontend application** with Vite + React (JavaScript) + Tailwind CSS
3. ✅ **Polished fantasy theme** with custom fonts (Cinzel, Crimson Text), colors, and components
4. ✅ **Full feature set:** Generate factions (1-10 count), generate quests (standalone and from factions), copy/export
5. ✅ **Style guide** (`docs/STYLE_GUIDE.md`) with complete design system
6. ✅ **Updated documentation** (root README, backend README, frontend README)
7. ✅ **Working integration** between backend and frontend with CORS configured
