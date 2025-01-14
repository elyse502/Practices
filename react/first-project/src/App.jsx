import { useRef, useState } from "react"
import FirstComponent from "./components/FirstComponent";

const App = () => {

  const [x, setX] = useState(0);

  const [data, setData] = useState([]);
  const inputRef = useRef(null);

  const btnClick = () => {
    console.log("clicked");
    setX(x + 1);
    console.log(x);
  }

  return (
    <div>
      <h1>React Props, State and Ref</h1>
      <button onClick={() => btnClick()}>Click me</button>
      <FirstComponent data={x} fn={setX}/>
      
      <br /><hr /><br />

      <input ref={inputRef} type="text" />
      <button onClick={()=>{setData([...data, inputRef.current.value])}}>Submit</button>
      {data.map((item, index)=>{return <h2 key={index}>{item}</h2>})}
    </div>
  )
}

export default App
