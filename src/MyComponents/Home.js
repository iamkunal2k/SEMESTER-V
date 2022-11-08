import React from 'react';
import { Link } from 'react-router-dom';
function Home (){

    return <div><nav>  
        <ul>  
            <li> <Link to="/">Home</Link></li>  
            <li> <Link to="/about">About</Link>  </li>  
            <li> <Link to="/Users">Users</Link> </li>
            <li> <Link to="/Counter">Count</Link></li>  
    
        </ul>  
    </nav>  
    </div>
}
  
export default Home;