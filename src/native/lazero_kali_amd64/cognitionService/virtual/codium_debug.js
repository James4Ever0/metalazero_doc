//const WebSocket = require('ws');
const port = 9999;
/*
(async ()=>{
const client = new WebSocket("ws://localhost:"+port+"/");
client.on("message",msg=>console.log(msg));
//await new Promise(resolve => client.once("open",resolve));

//client.send("hello")
})();*/
var W3CWebSocket = require('websocket').w3cwebsocket;

var client = new W3CWebSocket(`ws://localhost:${port}/`);
//var client = new W3CWebSocket(`ws://localhost:${port}/`, 'echo-protocol');

client.onerror = function() {
    console.log('Connection Error');
};

client.onopen = function() {
    console.log('WebSocket Client Connected');

    function sendNumber() {
        if (client.readyState === client.OPEN) {
            var number = Math.round(Math.random() * 0xFFFFFF);
            client.send(number.toString());
            setTimeout(sendNumber, 1000);
        }
    }
    sendNumber();
};

client.onclose = function() {
    console.log('echo-protocol Client Closed');
};

client.onmessage = function(e) {
    if (typeof e.data === 'string') {
        console.log("Received: '" + e.data + "'");
    }
};
