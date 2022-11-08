// const express = require ("express");
// var app = express();


// app.get('/', function (req,res) {
//     res.send("hello");
// });


const express = require ("express");

var app = express();

app.get('/', (req, res) => {
    res.send('Hello World!')
  })

app.post('/', (req, res) => {
    res.send('Got a POST request')
    console.log("post request");
})

  app.delete('/user', (req, res) => {
    res.send('Got a DELETE request at /user')
  })

  app.listen(1337, function(){
    console.log("listening at port 1337");
});
