const node_1 = require("vscode-languageserver-protocol/node")
const process = require("./processes") 
const cp = require("child_process")

function dir(a) {console.dir(a)}
function log(a) {console.log(a)}
function inspect(a) {return Object.getOwnPropertyNames(a)}
// something else?
//var serverProcess = cp.spawn("node",["vscode_lsp.js"])
var serverProcess = cp.spawn("bash-language-server",["start"])
//var serverProcess = cp.spawn("bash")// this shit does not properly respond to us.

const { StringDecoder } = require('string_decoder');
const decoder = new StringDecoder('utf8');

function dc(a){return decoder.write(a)}
//(type, ...args) <- way to hide these things.
serverProcess.stderr.on("data",d=>{log("STDERR\n"+dc(d))})
serverProcess.stdout.on("data",d=>{log("STDOUT\n"+dc(d))})
// this is buffer, decode it first.
// does this really matter? can we write into the stdin?
// no don't you think about this.
var client = {reader:new node_1.StreamMessageReader(serverProcess.stdout)
,writer:new node_1.StreamMessageWriter(serverProcess.stdin)}

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
dir(conn)
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
let fileuri="file:///sdcard/lazero/flutter/html/baidu_html-1598791515.html";
//asTextDocumentIdentifier(textDocument)
//do not have the document yet. get it parsed.
let meta={
	textDocument: {uri:fileuri},
	position: asWorkerPosition(position),
	context:{
		triggerKind: asCompletionTriggerKind(),
		triggerCharacter: " "}
}
let token=undefined
//uri2TextDocument
// this is shutdown.
// wtf is the token?
// use client/browser in place of node?
//conn.sendRequest(proto.CompletionRequest.type, meta,token).then(()=>{log("SUCCESS")}).catch(()=>{log("FAILED")})
dir(proto)
log(proto.InitializeRequest.type)
//{"jsonrpc":"2.0","id":0,"error":{"code":-32603,"message":"Request initialize failed with message: Cannot read property 'workspace' of undefined"}}
// bash-language-server/node_modules/vscode-jsonrpc/lib/common/connection.js -> ~400
//let init={workspace:"file:///sdcard/lazero/flutter/html/"}
let init={rootPath:"file:///",capabilities:[]}
//let init={}
//let init={workspace:"file:///sdcard/lazero/flutter/html/",capabilities:[]}


dir(proto)
conn.sendRequest(proto.InitializeRequest.type, init).then(()=>{log("SUCCESS");
let WSR=proto.WorkspaceSymbolRequest.type
log(WSR)
	//progress.attachWorkDone
conn.sendRequest(WSR,{workDoneToken:undefined}).then(()=>{log("SUCCESS")}).catch(()=>{log("FAILED")})
}).catch(()=>{log("FAILED")})

//conn.sendRequest(proto.CompletionRequest.type, meta,token).then(()=>{log("COMP SUCCESS")}).catch(()=>{log("FAILED")});
//conn.sendRequest(proto.ShutdownRequest.type, undefined).then(()=>{log("SUCCESS")}).catch(()=>{log("FAILED")})
//conn.sendRequest({method:itd,params:[uri]}).then(()=>{}).catch(()=>{})
// there must be errors.
// can i send some shits?
