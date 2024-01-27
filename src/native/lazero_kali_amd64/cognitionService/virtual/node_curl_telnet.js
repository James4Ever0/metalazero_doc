const process = require("./processes")
const cp = require("child_process")
function log(a) {console.log(a)}

const { StringDecoder } = require('string_decoder');

const decoder = new StringDecoder('utf8');

function dc(a){return decoder.write(a)}

var serverprocess = cp.spawn("curl",["--trace","-","telnet://localhost:10000"],{shell:true})
serverprocess.stderr.on("data",d=>{log("stderr\n"+dc(d))})
serverprocess.stdout.on("data",d=>{log("stdout\n"+dc(d))})
/*serverprocess.stdin.write=(data)=>{
	log("stdin\n"+data)
	serverprocess.stdin.prototype.write(data)}*/
setInterval(()=>{serverprocess.stdin.write("hello\n")},1000)
