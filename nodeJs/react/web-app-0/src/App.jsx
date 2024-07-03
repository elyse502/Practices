import { useEffect, useState } from 'react'
import { MainApp } from './styled';

const App = () => {
  
  const storageKeyName = "count";
  
  const retrieveCountValue = () => Number(localStorage.getItem(storageKeyName) || 0);

  const [count, setCount] = useState(retrieveCountValue());
  const addNumber = (count) => setCount(Number(count) + 1);
  
    useEffect(() => {
        localStorage.setItem(storageKeyName, String(count));
    }, [count]);

  return (
      <MainApp>
        Count Me

        <button onClick={() => addNumber(count)}>
          Count is {count}
        </button>
      </MainApp>
  )
}

export default App;