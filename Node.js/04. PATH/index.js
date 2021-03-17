const path = require('path')

console.log("")
console.log("Path is: " + path.dirname("D:/13 - WebDevelopment/Node.js/4. PATH/index.js"))
console.log("File Extension is: " + path.extname("D:/13 - WebDevelopment/Node.js/4. PATH/index.js"))
console.log("File fullName is: " + path.basename("D:/13 - WebDevelopment/Node.js/4. PATH/index.js"))

console.log("")
// This technique requires "PATH" only once || Much easier then techniques above
const path1 = path.parse("D:/13 - WebDevelopment/Node.js/4. PATH/index.js")
console.log(path1.name)
console.log(path1.base)
console.log(path1.dir)
console.log(path1.root)
console.log("")