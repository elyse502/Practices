import Todo from "./Components/Todo";

const App = () => {
  return (
    <div>
      <Todo />
      <footer>
        <p style={{ textAlign: "center", color: "white" }}>
          Made with ❤️ by{" "}
          <a
            target="_blank"
            style={{ color: "#ff6739", textDecoration: "underline" }}
            href="https://elyse502.github.io/Elysee-Portfolio/"
          >
            ElyséeDev
          </a>
        </p>
      </footer>
    </div>
  );
};

export default App;
