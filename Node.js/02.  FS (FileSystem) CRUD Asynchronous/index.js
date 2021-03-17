const fs = require("fs")

fs.mkdir("Thapa", (err) => {console.log(err)})

fs.writeFile("Thapa/bio.txt", "chuss", (err) => {console.log(err)})

fs.appendFile("Thapa/bio.txt", "\n\nUpdated text", (err) => {console.log(err)})

fs.readFile("Thapa/bio.txt", "UTF-8", (err,data) => {console.log(data)})

fs.rename("Thapa/bio.txt", "Thapa/mybio.txt", (err) => {console.log(err)})

fs.unlink("Thapa/mybio.txt", (err) => {console.log(err)})

fs.rmdir("Thapa", (err) => {console.log(err)})