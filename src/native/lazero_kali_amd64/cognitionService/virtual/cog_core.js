m="ism"
console.log(m.includes('is'))

const util = require("util")
const inspect = util.inspect

function print(a){console.log(a)}

print(Object.getOwnPropertyNames(m.__proto__))

print("newline")
//console.dir(m.__proto__)
