const express = require('express');
const app = express()
const PORT = 5000;
const bcrypt = require('bcrypt');

app.use(express.json())

const currentUser = {};
app.post('/api/signup',(req,res)=>{
    const {name,email,password} = req.body;
    const hashPassword = bcrypt.hashSync(password,bcrypt.genSaltSync(12));
    currentUser['name'] = name
    currentUser['email']= email
    currentUser['password'] = hashPassword
    console.log(currentUser);
    res.send("Signup Successfully")
})

app.post('/api/login',(req,res)=>{
    const {email,password} = req.body;
    const checkUser = currentUser['email'].toString() === email.toString()
    if(checkUser){
        const checkPassword = bcrypt.compareSync(password,currentUser['password']);
        if(checkPassword){
            res.status(200).json({
            userName:currentUser['name']
            })
        }
        else{
            res.status(401).send("Password is Incorrect")
        }
    }
    else{
        res.status(500).send("User Not Found")
    }
})

app.listen(PORT,()=>{
    console.log(`http://localhost:${PORT}`);
})