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
      colors: {
        'primary-red': '#E74C3C',
      },
    },
  },
  plugins: [],
}
