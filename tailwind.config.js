/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    // If you use Tailwind classes in JS:
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      // Defining the primary red color
      colors: {
        'primary-red': '#E74C3C',
        'dark-red': '#C0392B', // Added a darker shade for hover/shadow contrast
      },
    },
  },
  // Ensure dynamic classes are generated (Crucial for hovers and custom utilities)
  safelist: [
    {
      // Safelist commonly used classes with our custom colors
      pattern: /bg-(primary-red|dark-red)/,
    },
    {
      pattern: /text-(primary-red)/,
    }
  ],
  plugins: [],
}
