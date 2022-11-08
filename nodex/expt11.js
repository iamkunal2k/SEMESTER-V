const http = require('http');
const fs = require ("fs");
const port = 3000;
const server = http.createServer (function (req, res) {
    res.writeHead(200, {"content-type" : "text/html"})

    fs.readFile("page.html", function (err, data) {
        if(err) {
            res.write(404)
            res.write("Error!! file not Found");
        }

        else {
            res.write(data);
        }

        res.end();
    })
});

server.listen(port , function (err) {
    if(err) {
        console.log("Something went wrong", err);
    }

    else {
        console.log("server is listening on port " + port )
    }
});