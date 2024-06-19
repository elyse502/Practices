const Home = () => {
    return ( 
        <div className="Home">
            <h2> Homepage</h2><br />
            {/* <Example/> */}
            <Example name="John" age="23" job="Front-End Dev"/>
            <Example name="Emily" age="22" job="Back-End Dev"/>
            <Example name="Jack" age="25" job="Full-Stack Dev"/>
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
 
export default Home;