import React, {useState} from "react";
const Hookusestate=()=>{
    const [counter,setCounter] = useState(0);

    const increment=()=> {
        setCounter(counter+1)
    };

    return(
        <div>
            {counter}
            <br></br>
            <button onClick={increment}>Increment</button>
        </div>
    );
}
export default Hookusestate;