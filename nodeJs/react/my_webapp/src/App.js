import './App.css';
import Navbar from './Navbar';
import Home from './Home';

function App() {
  const title = "Welcome to the Web APP";
  const visits = 50;
  // const employee = {name: 'James', age: 25}; // Objects and Booleans are not allowed in JSX
  const link = 'http://www.google.com';
  return (
    <div className="App">
      <Navbar/>
      <div className="content">
        <Home/> <br />
        <h1>{title}</h1>
        <p>Visited {visits} times</p>
        {/* <p>{employee}</p> */}
        <p>{10}</p>
        <p>{ "Hello Coder" }</p>
        <p>{ [1,2,3,4,5] }</p>
        <p>{Math.random() * 10}</p>
        <a href='http://www.google.com'>Google Site</a><br />
        <a href= {link}>Google Site</a>




      </div>
    </div>
  );
}

export default App;
