import { useState } from "react"
import FirstComponent from "./components/FirstComponent";

const App = () => {

  const [x, setX] = useState(0);

  const btnClick = () => {
    console.log("clicked");
    setX(x + 1);
    console.log(x);
  }

  return (
    <div>
      <h1>React Props</h1>
      <button onClick={() => btnClick()}>Click me</button>
      <FirstComponent data={x} fn={setX}/>
    </div>
  )
}

export default App
