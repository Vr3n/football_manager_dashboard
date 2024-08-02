const withMT = require("@material-tailwind/html/utils/withMT");

/** @type {import('tailwindcss').Config} */
module.exports = withMT({
  content: [
    './templates/**/*.html',
    './templates/**/**/*.html',
    './templates/**/**/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
});
