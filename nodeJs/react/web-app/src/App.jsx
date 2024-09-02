import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const storageKeyName = "myotherkey";
  
  const retrieveCountValue = () => Number(localStorage.getItem(storageKeyName) || 0);

  const [count, setCount] = useState(retrieveCountValue());
  
  const addNumber = (count) => setCount(Number(count) + 1);
  

    useEffect(() => {
        localStorage.setItem(storageKeyName, String(count));
    }, [count]);

  return (
    <>
      <div className='App'>
        Hello World!
        <button onClick={() => addNumber(count)}>Count is {count}</button>
      </div>
    </>
  )
}

export default App
