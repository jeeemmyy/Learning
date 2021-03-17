// CHALLENGE
// Requiring built in NODE.JS MODULE named "fs" full name FileSystem

const fs = require("fs");

// Make a directory
// Create a file
// Append (write below) the already existing data
// Read a file and the convert returned data from buffer to string type
// Rename a file (OldPath & Name), (NewPath & Name)
// Delete newly created "FILE"
// Deleting newly created "directory"

fs.mkdirSync("Thapa");
fs.writeFileSync("Thapa/bio.txt", "chuss")
fs.appendFileSync("Thapa/bio.txt", "\n\nUpdated text")
let readFileText = fs.readFileSync("Thapa/bio.txt")
    console.log(readFileText.toString())
fs.renameSync("Thapa/bio.txt", "Thapa/mybio.txt")
fs.unlinkSync("Thapa/mybio.txt")
fs.rmdirSync("Thapa")