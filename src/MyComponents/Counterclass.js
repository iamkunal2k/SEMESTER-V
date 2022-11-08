import React from "react"; 
 class Counterclass extends React.Component{     
    constructor(props){         
        super(props);         
        this.state={             
            count: 0 
        } 
    }  
    
    increment = () => {         
        this.setState({
            count: this.state.count + 1
        });     
    }  
    decrement = () => {         
        this.setState({count: this.state.count - 1
        });     
    }      
    render(){         
        return( 
            <div> 
                <button onClick={this.increment} className="counter">+</button> 
                <button onClick={this.decrement} className="counter"></button> 
                <h1>{this.state.count}</h1> 
            </div> 
        ); 
    } 
}  
export default Counterclass; 
