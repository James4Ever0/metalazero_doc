const node_1 = require("vscode-languageserver-protocol/node")
const process = require("./processes") 
const cp = require("child_process")

function dir(a) {console.dir(a)}
function log(a) {console.log(a)}
function inspect(a) {return Object.getOwnPropertyNames(a)}
// something else?
//var serverProcess = cp.spawn("node",["vscode_lsp.js"])

const bls = "E:\\nodejs\\node_global\\bash-language-server.cmd"
var serverProcess = cp.spawn(bls,["start"])
var python = "D:\\Programs\\Python\\Python36\\python36.exe"
// process.cwd()
var spyProcess = cp.spawn(python,["spy_process.py"]) // they use pipe as the communication tool on windows. mostly for node_ipc or c#.
// var spyProcess = cp.spawn(bls,["start"]) // must be some magic shit.
// must be full-path?
//var serverProcess = cp.spawn("python3",["recv.py"])
//var serverProcess = cp.spawn("bash")// this shit does not properly respond to us.

const { StringDecoder } = require('string_decoder');
const decoder = new StringDecoder('utf8');

function dc(a){return decoder.write(a)}
//(type, ...args) <- way to hide these things.
serverProcess.stderr.on("data",d=>{log("\nSERVER_STDERR_START\n"+dc(d)+"\nSERVER_STDERR_END\n")})
serverProcess.stdout.on("data",d=>{log("\nSERVER_STDOUT_START\n"+dc(d)+"\nSERVER_STDOUT_END\n")})// it is included.
// spyProcess.stdout.on("data",d=>{log("\nSERVER_STDIN_START\n"+dc(d)+"\nSERVER_STDIN_END\n");serverProcess.stdin.write(d)})// it is included.
// override this shit.
// spyProcess.stdin.write = (data) => {log("\nSERVER_STDIN_START\n"+dc(data)+"\nSERVER_STDIN_END\n");serverProcess.stdin.write(data);serverProcess.stdin.end()}
var node_writer = new node_1.StreamMessageWriter(serverProcess.stdin)
// dir(node_writer)
var spy_writer = new node_1.StreamMessageWriter(spyProcess.stdin)
spy_writer.write = (d)=>{console.log("SERVER_STDIN_START");console.log(d);console.log("SERVER_STDIN_END");node_writer.write(d)}
// alter the function. fuck it.
// dir(spyProcess.stdin.end())

// serverProcess.stdin.on("data",d=>{log("\nSERVER_")})
// this is buffer, decode it first.
// does this really matter? can we write into the stdin?
// no don't you think about this.
var client = {reader:new node_1.StreamMessageReader(serverProcess.stdout)
,writer:spy_writer}
// replace this shit with another shit.

let conn = node_1.createMessageConnection(client.reader,client.writer)

let note = new node_1.RequestType('testNotification');
//let note = new node_1.NotificationType('testNotification');

conn.listen()
//setInterval(()=>{conn.sendRequest("Hello World")},1000)
//setInterval(()=>{conn.sendRequest(note,"Hello World")},1000)
log("made it?")
//dir(node_1.createMessageConnection)
uri = "file:///Users/dirkb/sample/test.ts"
td = "textDocument/didOpen"
// dir(conn)
// method, params?
const proto = require("vscode-languageserver-protocol");
//log(proto.ShutdownRequest.type)
//let meta = code2ProtocolConverter.asCompletionParams(document, position, context)

function asTextDocumentIdentifier(textDocument) { return { uri: _uriConverter(textDocument.uri) };}

function asWorkerPosition(position) { return { line: position.line, character: position.character };}

function asCompletionTriggerKind(triggerKind) { switch (triggerKind) {
	case 0: return proto.CompletionTriggerKind.TriggerCharacter;  
	case 1:return proto.CompletionTriggerKind.TriggerForIncompleteCompletions;
	default:return proto.CompletionTriggerKind.Invoked; } }

let position={line:0,character:0}
// let fileuri="D:\\AGI\\metalazero\\native\\lazero_kali_amd64\\cognitionService\\virtual\\vscode_ipc.sh";
let fileuri="file://D:/AGI/metalazero/native/lazero_kali_amd64/cognitionService/virtual/vscode_ipc.sh";
//asTextDocumentIdentifier(textDocument)
// bad links. or great.
//do not have the document yet. get it parsed.
let meta={
	textDocument: {uri:fileuri},
	position: {line:0,character:0},
	context:{
		triggerKind: asCompletionTriggerKind(),
        triggerCharacter: " "},
    // shit?
    // rootNode:[]
}
let token=undefined
//uri2TextDocument
// this is shutdown.
// wtf is the token?
// use client/browser in place of node?
//conn.sendRequest(proto.CompletionRequest.type, meta,token).then(()=>{log("SUCCESS")}).catch(()=>{log("FAILED")})
// dir(proto)
// log(proto.InitializeRequest.type)
//{"jsonrpc":"2.0","id":0,"error":{"code":-32603,"message":"Request initialize failed with message: Cannot read property 'workspace' of undefined"}}
// bash-language-server/node_modules/vscode-jsonrpc/lib/common/connection.js -> ~400
//let init={workspace:"file:///sdcard/lazero/flutter/html/"}
// const bash_lsp_capabilities={"textDocumentSync":1,"completionProvider":{"resolveProvider":true,"triggerCharacters":["$","{"]},"hoverProvider":true,"documentHighlightProvider":true,"definitionProvider":true,"documentSymbolProvider":true,"workspaceSymbolProvider":true,"referencesProvider":true}
const std_cap = {textDocument:{completion:{completionItem:{snippetSupport:true}}}}
// process.cwd() 
// complex number vagina depth.
let init={rootPath:"D:\\AGI\\metalazero\\native\\lazero_kali_amd64\\cognitionService\\virtual",capabilities:std_cap}
// let init={rootPath:"/data/data/com.termux/files/home/metalazero/native/lazero_kali_amd64/cognitionService/virtual",capabilities:[]}
//let init={}
//let init={workspace:"file:///sdcard/lazero/flutter/html/",capabilities:[]}


conn.sendRequest(proto.InitializeRequest.type, init).then(()=>{log("SUCCESS");
conn.sendRequest(proto.CompletionRequest.type, meta,token).then(()=>{log("COMP SUCCESS")}).catch(()=>{log("FAILED")});
}).catch(()=>{log("FAILED")})

//dir(proto)
//let WSR=proto.WorkspaceSymbolRequest.type
//log(WSR)
//conn.sendRequest(WSR,undefined).then(()=>{log("SUCCESS")}).catch(()=>{log("FAILED")})
//conn.sendRequest(proto.ShutdownRequest.type, undefined).then(()=>{log("SUCCESS")}).catch(()=>{log("FAILED")})
//conn.sendRequest({method:itd,params:[uri]}).then(()=>{}).catch(()=>{})
// there must be errors.
// can i send some shits?
// this is the fastest way to get shit.