import react, { useEffect, useState } from 'react';
function App() {
  const [backData, setBackData] = useState([{}])
  useEffect(()=>{
    fetch("/api").then(
      response => response.json()
    ).then(data =>{setBackData(data)})
  }, [])
  
  return(
    <div>
      {(typeof backData.users === 'undefined') ? (
        <p>Loading.....</p>
      ):(
        backData.users.map((user,i ) => {
          <p key = {i}>{user}</p>
        })
      )}
    </div>
  )

}
export default App;