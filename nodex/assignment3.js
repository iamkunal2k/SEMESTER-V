const express = require ("express");

var app = express();
app.get('/', (req, res) => {
    res.send('Hello World!')
  })

app.post('/', (req, res) => {
    res.send('Got a POST request')
})

  app.delete('/user', (req, res) => {
    res.send('Got a DELETE request at /user')
  })