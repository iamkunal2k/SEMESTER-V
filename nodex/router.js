const express = require ("express");
var app = express();
var port  = 9000;

var router1 = express.Router();
var router2 = express.Router();
var router3 = express.Router();


router1.get("/user", function (re1, res, next) {
    console.log("user router working");
    res.end();
});

router2.get("/student", function (re1, res, next) {
    console.log("Student Router");
    res.end();
});

router1.get("/admin", function (re1, res, next) {
    console.log("Admin router");
    res.end();
});

app.use(router1);
app.use(router2);
app.use(router3);

app.listen(port, function (err) {
    if(err) console.log(err);
    console.log("Server on port ", port);
});


