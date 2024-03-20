/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./search/templates/**/*.html",
    "./home/templates/**/*.html",
    "./Wagtail_Blog/templates/**/*.html",
    "./Wagtail_Blog/base/templates/**/*.html",
    "./Wagtail_Blog/blog/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("daisyui"),
    require("preline/plugin"),
  ],
  daisyui: {
    themes: [
      "light",
      "dark",
      "cupcake",
      "business",
      "cyberpunk",
      "valentine",
      "forest",
      "aqua",
      "black",
      "nord"
    ],
  },
};
