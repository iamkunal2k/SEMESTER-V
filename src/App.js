import logo from './logo.svg';
import './App.css';
// import Myfunction from './MyComponents/Myfunction';
// import Classcomp from './MyComponents/Classcomp';
import Hookusestate from './MyComponents/Hookusestate';
import Counterclass from './MyComponents/Counterclass';

function App() {
  return (
    <div className="App">
      {/* <Myfunction/>
      <Classcomp/> */}
      <Hookusestate/>
      {/* <Counterclass/> */}
    </div>
  );
}

export default App;


// import React, { Component } from 'react';
// import Home from './MyComponents/Home';
// import About from './MyComponents/About'
// import Users from './MyComponents/Users'
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import Hookusestate from './MyComponents/Hookusestate';


// class App extends Component {
//   render() {
//     return (
//       <>
//     <Router>
//         <Routes>
//           <Route path="/" element={<Home />} />
//           <Route path="/about" element={<About />}/>
//           <Route path="/users" element={<Users />}/>
//           <Route path="/Counter" element={<Hookusestate />}/>
//         </Routes>
//     </Router>
//        </>
//    );
//   }
// }
// export default App;
