/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Ensure all your template files are scanned for classes
    './templates/**/*.html',
    './app.py',
    './content.json',
  ],
  theme: {
    extend: {
      fontFamily: {
        // Sets 'Inter' as the default font for the entire site (font-sans)
        sans: ['Inter', 'sans-serif'], 
      },
      colors: {
        // Define your primary brand red color for consistent use (e.g., border-primary-red)
        'primary-red': '#E74C3C', 
      }
    },
  },
  plugins: [],
}
