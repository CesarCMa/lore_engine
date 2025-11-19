/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        arcane: {
          50: '#F3E8F7',
          100: '#E1C9EE',
          200: '#C599DD',
          300: '#A969CC',
          400: '#8D39BB',
          500: '#6B2C6B',
          600: '#4A1A4A',
          700: '#3B153B',
          800: '#2C102C',
          900: '#1D0A1D',
        },
        gold: {
          50: '#FFFBEB',
          100: '#FEF3C7',
          200: '#FDE68A',
          300: '#FCD34D',
          400: '#FBBF24',
          500: '#D4AF37',
          600: '#B8960F',
          700: '#92750A',
          800: '#6C5608',
          900: '#463705',
        },
        crimson: {
          50: '#FEF2F2',
          100: '#FEE2E2',
          200: '#FECACA',
          300: '#FCA5A5',
          400: '#F87171',
          500: '#DC143C',
          600: '#B22222',
          700: '#8B0000',
          800: '#660000',
          900: '#4D0000',
        },
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
        },
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
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
