module.exports = {
  darkMode: "class",
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./layouts/**/*.{js,ts,jsx,tsx}",
    "./screens/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        primary: "Oswald",
      },
      fontSize: {
        xxs: "0.5rem",
      },
      colors: {
        default: "#101729",
        card: "#17223B",
      },
      screens: {
        pc: "1200px",
      },
    },
  },
  plugins: [],
};

//
