const express = require("express")
const session = require('express-session')
const app = express()

var PORT = process.env.port || 3000

app.use(session({
    secret: "your_secret_key",

    resave: true,

    saveUninitialized: true
}))

app.get("/", function(req, res){
    req.session.name = "R_SESSION"
    return res.send("Session Set")
})

app.get("/session", function(req,res){
    // var name = req.session.name
    // return res.send(name)

    //to destroy
    req.session.destroy(function(error){
        console.log("session destroyed")
    })
})

app.listen(PORT, function(error){
    if(error) throw error
    console.log("Server created successfully on PORT :", PORT)
})

