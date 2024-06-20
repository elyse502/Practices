// import './Card.css';
import { useState } from 'react';
const Home = () => {

    // let name = "John Doe";
    const [name, setName] = useState("John Doe");

    const handleClick = () => {
        // name = "Jane Doe";
        // console.log(name);
        setName("Jane Doe");
    }

    return ( 
        <div className="Home">
            <h2> Homepage</h2><br />
            {/* <Example/> */}
            <Example name="John" age="23" job="Front-End Dev"/>
            <Example name="Emily" age="22" job="Back-End Dev"/>
            <Example name="Jack" age="25" job="Full-Stack Dev"/><br /><br />
            
            
            <Library Title="To kill The Mockingbird"
            Author="Harper Lee" Description="A classic novel about racial injustice in deep south" Date="2021-01-01" />
            <Library Title="The Great Gatsby" Author="F. Scott Fitzgerald" Description="A novel about the American Dream's corruption" Date="2022-01-01" />
            <Library Title="The Catcher in the Rye" Author="J.D. Salinger" Description="A novel about the consequences of the Great Depression" Date="2023-01-01" /><br /><br />


            <p>{name}</p>
            <button onClick={handleClick}>Click me</button>
        </div>
     );
}

{/* const Example = () => {
    return ( 
        <div>
            <div>
                <h3>Name: John</h3><br />
                <h3>Age: 23</h3><br />
                <h3>Job: Front-End Dev</h3><br /><hr />
            </div>

            <div>
                <h3>Name: Emily</h3><br />
                <h3>Age: 22</h3><br />
                <h3>Job: Back-End Dev</h3><br /><hr />
            </div>

            <div>
                <h3>Name: Jack</h3><br />
                <h3>Age: 25</h3><br />
                <h3>Job: Full-Stack Dev</h3><br /><hr />
            </div>
        </div>
     );
}
*/}

const Example = (props) => {
    return ( 
        <div>
            <h3>Name: {props.name}</h3><br />
            <h3>Age: {props.age}</h3><br />
            <h3>Job: {props.job}</h3><br /><hr />
        </div>
     );
}

// Props Project Challenge

const Library = (props) => {
    return ( 
        <div className="Card">
            <h2>{props.Title}</h2> <hr />
            <h3>{props.Author}</h3> <hr />
            <p>{props.Description}</p> <hr />
            <p>{props.Date}</p>

        </div>
     );
}
 
export default Home;