const node_1 = require("vscode-languageserver-protocol/node")
const process = require("./processes") 
const cp = require("child_process")

function dir(a) {console.dir(a)}
function log(a) {console.log(a)}
// something else?
var serverProcess = cp.spawn("bash-language-server",["start"])
// does this really matter? can we write into the stdin?
// no don't you think about this.
var client = {reader:new node_1.StreamMessageReader(serverProcess.stdout)
,writer:new node_1.StreamMessageWriter(serverProcess.stdin)}

// shall be resolved.
//dir(client.reader)
function inspect(a) {return Object.getOwnPropertyNames(a)}
log(client.reader.readable.stream)
log(inspect(client.reader.readable.stream.__proto__))
log(inspect(client.reader.readable.stream.__proto__.__proto__))
log(inspect(client.reader.readable.stream))
log(client.reader.buffer)
// great, now what to write?
log(client.reader.readable.stream._read(1))
log("_____________________WRITER_____________________")
dir(client.writer)
dir(client.writer.writable.__proto__)
dir(client.writer.writable.__proto__.__proto__)
log(client.writer.write)
log(client.reader.read) //got nothing.
log(client.reader.write) //got nothing.
var m = {method:"echo",params:["hello world?"]}; // this semicolon.
(async () =>{
let ml = JSON.stringify(m);
await client.writer.write(ml);
log(client.reader);
setInterval(()=>{log(client.reader.buffer);},1000);
})();

// semicolons. always?
