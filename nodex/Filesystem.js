const fs = require("fs");
const path = require("path")
const dirpath = path.join(__dirname,"curd");
const filepath = `${dirpath}/Sample.txt`;

fs.writeFileSync(filepath, "This is sample text");

fs.readFile(filepath,"utf-8", (err,item) => {
    console.log(item);
}) 

fs.appendFile(filepath, " To read and append something on these file", (err) => {
    if(!err) console.log("sample.txt file is created");
});

fs.rename(filepath, `${dirpath}/example.txt`, (err) => {
   if(!err) console.log ("Filename is updated");
});

fs.unlinkSync(`${dirpath}/example.txt`, (del) => {
    if(del) console.log("file is unlinked")
});