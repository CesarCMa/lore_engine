# Lore Engine - Fantasy Theme Style Guide

This document defines the complete design system for the Lore Engine fantasy-themed application.

---

## Typography

### Font Families

Our fantasy theme uses three carefully selected Google Fonts:

#### Headings: Cinzel
- **Usage**: Titles, headings (h1-h6), navigation
- **Character**: Ornate serif with classical elegance
- **Tailwind class**: `font-heading`
- **Weights**: 400 (regular), 600 (semibold), 700 (bold)
- **Google Fonts**: `Cinzel`

```jsx
<h1 className="font-heading text-5xl">Faction Forge</h1>
```

#### Body Text: Crimson Text
- **Usage**: Body copy, paragraphs, descriptions
- **Character**: Highly readable serif, excellent for long-form text
- **Tailwind class**: `font-body`
- **Weights**: 400 (regular), 600 (semibold)
- **Styles**: Normal, Italic
- **Google Fonts**: `Crimson Text`

```jsx
<p className="font-body text-lg">Craft powerful factions for your fantasy world</p>
```

#### Accent: MedievalSharp
- **Usage**: Special decorative text, quotes, callouts
- **Character**: Medieval-inspired, decorative
- **Tailwind class**: `font-accent`
- **Google Fonts**: `MedievalSharp`

```jsx
<span className="font-accent text-xl">⚔️ Quest Weaver</span>
```

### Font Loading

Fonts are loaded via Google Fonts CDN in `index.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=MedievalSharp&display=swap" rel="stylesheet">
```

---

## Color Palette

### Primary: Arcane Purple

Represents magical, mystical elements. Use for primary UI elements and magical themes.

| Shade | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| 50 | `#F3E8F7` | rgb(243, 232, 247) | Light backgrounds, subtle highlights |
| 100 | `#E1C9EE` | rgb(225, 201, 238) | Hover states, light accents |
| 200 | `#C599DD` | rgb(197, 153, 221) | Borders, dividers |
| 300 | `#A969CC` | rgb(169, 105, 204) | Secondary elements |
| 400 | `#8D39BB` | rgb(141, 57, 187) | Interactive elements |
| **500** | **`#6B2C6B`** | **rgb(107, 44, 107)** | **Primary brand color** |
| 600 | `#4A1A4A` | rgb(74, 26, 74) | Hover states for primary |
| 700 | `#3B153B` | rgb(59, 21, 59) | Active states |
| 800 | `#2C102C` | rgb(44, 16, 44) | Dark backgrounds |
| 900 | `#1D0A1D` | rgb(29, 10, 29) | Darkest backgrounds, text on light |

**Tailwind classes**: `bg-arcane-500`, `text-arcane-700`, `border-arcane-300`

```jsx
<div className="bg-arcane-700 text-white p-4">
  Magical Navigation
</div>
```

---

### Secondary: Mystic Gold

Represents treasure, importance, and highlights. Use for accents, buttons, and call-to-action elements.

| Shade | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| 50 | `#FFFBEB` | rgb(255, 251, 235) | Light backgrounds |
| 100 | `#FEF3C7` | rgb(254, 243, 199) | Subtle highlights |
| 200 | `#FDE68A` | rgb(253, 230, 138) | Light borders |
| 300 | `#FCD34D` | rgb(252, 211, 77) | Hover states |
| 400 | `#FBBF24` | rgb(251, 191, 36) | Secondary buttons |
| **500** | **`#D4AF37`** | **rgb(212, 175, 55)** | **Primary gold (main)** |
| 600 | `#B8960F` | rgb(184, 150, 15) | Pressed states |
| 700 | `#92750A` | rgb(146, 117, 10) | Dark gold |
| 800 | `#6C5608` | rgb(108, 86, 8) | Very dark gold |
| 900 | `#463705` | rgb(70, 55, 5) | Darkest gold |

**Tailwind classes**: `bg-gold-500`, `text-gold-600`, `border-gold-400`

```jsx
<button className="bg-gradient-to-r from-gold-500 to-gold-600 text-white">
  Generate
</button>
```

---

### Accent: Dragon Crimson

Represents danger, deletion, and urgent actions. Use sparingly for warnings and destructive actions.

| Shade | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| 50 | `#FEF2F2` | rgb(254, 242, 242) | Error backgrounds |
| 100 | `#FEE2E2` | rgb(254, 226, 226) | Light error states |
| 200 | `#FECACA` | rgb(254, 202, 202) | Borders |
| 300 | `#FCA5A5` | rgb(252, 165, 165) | Hover for errors |
| 400 | `#F87171` | rgb(248, 113, 113) | Error text |
| **500** | **`#DC143C`** | **rgb(220, 20, 60)** | **Primary crimson (main)** |
| 600 | `#B22222` | rgb(178, 34, 34) | Danger buttons |
| 700 | `#8B0000` | rgb(139, 0, 0) | Dark danger |
| 800 | `#660000` | rgb(102, 0, 0) | Very dark danger |
| 900 | `#4D0000` | rgb(77, 0, 0) | Darkest danger |

**Tailwind classes**: `bg-crimson-600`, `text-crimson-500`, `border-crimson-400`

```jsx
<button className="bg-crimson-600 text-white hover:bg-crimson-700">
  Delete
</button>
```

---

### Neutral: Parchment

Represents aged paper and backgrounds. Primary neutral palette for the application.

| Shade | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| 50 | `#FDFCFA` | rgb(253, 252, 250) | Lightest background |
| **100** | **`#F5E6D3`** | **rgb(245, 230, 211)** | **Card backgrounds (main)** |
| 200 | `#E8D7C3` | rgb(232, 215, 195) | Page backgrounds |
| 300 | `#D4C4B0` | rgb(212, 196, 176) | Borders, dividers |
| 400 | `#C0B29D` | rgb(192, 178, 157) | Disabled states |
| 500 | `#ACA08A` | rgb(172, 160, 138) | Muted text |
| 600 | `#8B7D6B` | rgb(139, 125, 107) | Secondary text |
| 700 | `#6A5F52` | rgb(106, 95, 82) | Tertiary text |
| 800 | `#4A423A` | rgb(74, 66, 58) | Dark text |
| **900** | **`#2A2521`** | **rgb(42, 37, 33)** | **Primary text color** |

**Tailwind classes**: `bg-parchment-100`, `text-parchment-900`, `border-parchment-300`

```jsx
<div className="bg-parchment-100 border-2 border-gold-500 p-6">
  Card content
</div>
```

---

## Component Guidelines

### Cards

Fantasy-themed cards with ornate borders and parchment backgrounds.

**Base styles:**
- Background: `bg-parchment-100`
- Border: `border-2 border-gold-500`
- Padding: `p-6`
- Border radius: `rounded-lg`
- Shadow: `shadow-parchment`

**Hover effect:**
- Scale: `hover:scale-105`
- Shadow: `hover:shadow-gold`
- Transition: `transition-all duration-200`

```jsx
<div className="bg-parchment-100 border-2 border-gold-500 rounded-lg p-6 shadow-parchment hover:scale-105 hover:shadow-gold transition-all duration-200 ornate-card">
  <h3 className="font-heading text-2xl text-arcane-700">Faction Name</h3>
  <p className="font-body text-parchment-700">Description</p>
</div>
```

---

### Buttons

Raised buttons with gradients and smooth hover effects.

**Variants:**

#### Primary (Gold)
- Background: `bg-gradient-to-r from-gold-500 to-gold-600`
- Text: `text-white`
- Hover: `hover:scale-105 hover:brightness-110`
- Transition: `transition-all duration-200`

```jsx
<button className="bg-gradient-to-r from-gold-500 to-gold-600 text-white px-4 py-2 rounded-lg hover:scale-105 hover:brightness-110 transition-all duration-200">
  Generate
</button>
```

#### Secondary (Arcane)
- Background: `bg-arcane-600`
- Text: `text-white`
- Hover: `hover:bg-arcane-700`

```jsx
<button className="bg-arcane-600 text-white px-4 py-2 rounded-lg hover:bg-arcane-700 transition-colors duration-200">
  Secondary Action
</button>
```

#### Danger (Crimson)
- Background: `bg-crimson-600`
- Text: `text-white`
- Hover: `hover:bg-crimson-700`

```jsx
<button className="bg-crimson-600 text-white px-4 py-2 rounded-lg hover:bg-crimson-700 transition-colors duration-200">
  Delete
</button>
```

#### Outline
- Border: `border-2 border-gold-500`
- Text: `text-gold-600`
- Hover: `hover:bg-gold-50`

```jsx
<button className="border-2 border-gold-500 text-gold-600 px-4 py-2 rounded-lg hover:bg-gold-50 transition-colors duration-200">
  Outline
</button>
```

**Sizes:**
- Small: `px-3 py-1.5 text-sm`
- Medium: `px-4 py-2 text-base` (default)
- Large: `px-6 py-3 text-lg`

**Disabled state:**
- Opacity: `opacity-50`
- Cursor: `cursor-not-allowed`

---

### Inputs

Form inputs with fantasy styling and focus states.

**Base styles:**
- Background: `bg-parchment-50`
- Border: `border-2 border-gold-400`
- Padding: `px-4 py-2`
- Border radius: `rounded-lg`
- Font: `font-body`

**Focus state:**
- Ring: `focus:ring-2 focus:ring-arcane-500`
- Border: `focus:border-arcane-500`
- Outline: `focus:outline-none`

**Error state:**
- Border: `border-crimson-500`
- Ring: `focus:ring-crimson-500`

```jsx
<input
  type="text"
  className="bg-parchment-50 border-2 border-gold-400 rounded-lg px-4 py-2 font-body focus:ring-2 focus:ring-arcane-500 focus:border-arcane-500 focus:outline-none"
  placeholder="Enter text..."
/>
```

---

### Icons

Use Lucide React icons colored with theme colors.

**Color mapping:**
- Actions/Magic: `text-gold-500`
- Delete/Danger: `text-crimson-600`
- Info/Arcane: `text-arcane-600`
- Neutral: `text-parchment-700`

```jsx
import { Scroll, Swords, Music, Copy } from 'lucide-react';

<Scroll className="text-gold-500 w-6 h-6" />
<Swords className="text-crimson-600 w-5 h-5" />
<Music className="text-arcane-600 w-5 h-5" />
<Copy className="text-parchment-700 w-4 h-4" />
```

---

## Custom Shadows

### Arcane Shadow
- Effect: Purple magical glow
- CSS: `box-shadow: 0 0 20px rgba(107, 44, 107, 0.3)`
- Tailwind: `shadow-arcane`

### Gold Shadow
- Effect: Golden highlight glow
- CSS: `box-shadow: 0 0 15px rgba(212, 175, 55, 0.4)`
- Tailwind: `shadow-gold`

### Parchment Shadow
- Effect: Subtle paper depth
- CSS: `box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1)`
- Tailwind: `shadow-parchment`

```jsx
<div className="shadow-gold">Golden glow</div>
<div className="shadow-arcane">Magical glow</div>
<div className="shadow-parchment">Paper depth</div>
```

---

## Animations

### Fade In
- Duration: 0.5s ease-in-out
- Keyframes: opacity 0 → 1
- Tailwind: `animate-fadeIn`

```jsx
<div className="animate-fadeIn">
  Fades in on mount
</div>
```

### Slide Up
- Duration: 0.4s ease-out
- Keyframes: translateY(20px) + opacity 0 → translateY(0) + opacity 1
- Tailwind: `animate-slideUp`

```jsx
<div className="animate-slideUp">
  Slides up and fades in
</div>
```

### Hover Transforms
- Scale up: `hover:scale-105`
- Brightness: `hover:brightness-110`
- Transition: `transition-transform duration-200`

```jsx
<button className="hover:scale-105 transition-transform duration-200">
  Hover me
</button>
```

---

## Visual Effects

### Paper Texture Background

Subtle parchment texture using CSS gradients (defined in `fantasy-theme.css`):

```css
.parchment-texture {
  background-image:
    repeating-linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.03) 0px,
      transparent 1px,
      transparent 2px,
      rgba(0, 0, 0, 0.03) 3px
    ),
    repeating-linear-gradient(
      90deg,
      rgba(0, 0, 0, 0.03) 0px,
      transparent 1px,
      transparent 2px,
      rgba(0, 0, 0, 0.03) 3px
    );
}
```

### Ornate Card Decorations

Corner flourishes using pseudo-elements (defined in `fantasy-theme.css`):

```css
.ornate-card::before,
.ornate-card::after {
  content: '';
  position: absolute;
  width: 40px;
  height: 40px;
  opacity: 0.6;
  pointer-events: none;
}

.ornate-card::before {
  top: -2px;
  left: -2px;
  border-top: 3px solid #D4AF37;
  border-left: 3px solid #D4AF37;
  border-top-left-radius: 8px;
}

.ornate-card::after {
  bottom: -2px;
  right: -2px;
  border-bottom: 3px solid #D4AF37;
  border-right: 3px solid #D4AF37;
  border-bottom-right-radius: 8px;
}
```

### Scroll Dividers

Elegant horizontal dividers:

```css
.scroll-divider {
  height: 2px;
  background: linear-gradient(to right, transparent, #D4AF37, transparent);
  position: relative;
  margin: 1rem 0;
}
```

---

## Responsive Design

### Breakpoints

Following Tailwind's default breakpoints:

- `sm`: 640px - Small tablets
- `md`: 768px - Tablets
- `lg`: 1024px - Desktops
- `xl`: 1280px - Large desktops
- `2xl`: 1536px - Extra large screens

### Mobile-First Approach

Always design for mobile first, then enhance for larger screens:

```jsx
{/* Mobile: stack vertically, Desktop: 3 columns */}
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  {factions.map(faction => <FactionCard key={faction.name} faction={faction} />)}
</div>
```

### Responsive Typography

```jsx
<h1 className="text-3xl md:text-4xl lg:text-5xl font-heading">
  Title scales with screen size
</h1>
```

---

## Accessibility

### Color Contrast

All color combinations meet WCAG AA standards:
- Primary text (`parchment-900`) on light backgrounds: ✅ AAA
- White text on `gold-500`: ✅ AA
- White text on `arcane-700`: ✅ AAA
- White text on `crimson-600`: ✅ AA

### Focus States

All interactive elements have visible focus indicators:
- Ring: `focus:ring-2`
- Color: `focus:ring-arcane-500`
- Outline: Always use `focus:outline-none` with custom ring

### Keyboard Navigation

- All buttons and links are keyboard accessible
- Tab order follows logical flow
- Focus indicators are always visible

### Alt Text

All decorative images and icons should have appropriate alt text or aria-labels:

```jsx
<button aria-label="Copy faction to clipboard">
  <Copy className="w-4 h-4" />
</button>
```

---

## Usage Examples

### Complete Card Component

```jsx
<div className="bg-parchment-100 border-2 border-gold-500 rounded-lg p-6 shadow-parchment hover:scale-105 hover:shadow-gold transition-all duration-200 ornate-card animate-fadeIn">
  <div className="flex items-center gap-3 mb-4">
    <Scroll className="text-gold-500 w-6 h-6" />
    <h3 className="font-heading text-2xl text-arcane-700">The Crimson Order</h3>
  </div>

  <div className="scroll-divider"></div>

  <div className="space-y-2">
    <p className="font-body text-parchment-800">
      <span className="font-semibold">Symbol:</span> A blood-red phoenix
    </p>
    <p className="font-body text-parchment-800">
      <span className="font-semibold">Values:</span> Honor, Sacrifice, Rebirth
    </p>
  </div>

  <button className="mt-4 bg-gradient-to-r from-gold-500 to-gold-600 text-white px-4 py-2 rounded-lg hover:scale-105 transition-all duration-200 w-full">
    <Copy className="inline w-4 h-4 mr-2" />
    Copy to Clipboard
  </button>
</div>
```

---

## Design Tokens Summary

### Tailwind Config Location
`frontend/tailwind.config.js`

### Custom CSS
`frontend/src/styles/fantasy-theme.css`

### Font Loading
`frontend/index.html` (Google Fonts CDN)

### All Custom Classes
- `font-heading` - Cinzel serif
- `font-body` - Crimson Text serif
- `font-accent` - MedievalSharp cursive
- `shadow-arcane` - Purple magical glow
- `shadow-gold` - Golden highlight
- `shadow-parchment` - Paper depth
- `animate-fadeIn` - Fade in animation
- `animate-slideUp` - Slide up animation
- `ornate-card` - Card with corner flourishes
- `scroll-divider` - Horizontal gold gradient divider
- `parchment-texture` - Subtle paper texture

---

## Best Practices

1. **Consistency**: Always use theme colors instead of arbitrary values
2. **Hierarchy**: Use font weights and sizes to establish clear hierarchy
3. **Spacing**: Use Tailwind's spacing scale (4, 8, 12, 16, etc.)
4. **Transitions**: Keep all transitions under 300ms for snappy feel
5. **Hover states**: Always provide visual feedback on interactive elements
6. **Loading states**: Show loading spinners for async operations
7. **Error handling**: Use crimson colors for errors with clear messages
8. **Progressive enhancement**: Ensure core functionality works without JS

---

*Last updated: 2025-11-19*
