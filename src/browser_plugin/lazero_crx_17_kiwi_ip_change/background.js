//intercept all urls. get the result back,
//only keep a selected few.
console.log("LAZERO PLUGIN\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
delete chrome.debugger;
const consoleurl = "ws://100.115.92.2:4999/chrome_console";

var socket = new WebSocket(consoleurl);


const reconnect = 2000;


const background = "background: ";


const tab_id = "tab_id: ";


const currentid = "background";


const evaltimeout = 1000;
//kiwi does not have chrome.debugger.
//const command_prefix = "let chrome = Object.create(this.chrome);chrome.debugger=null;"
const command_prefix = "let eval = null;"
function command_processor (command){return command_prefix+command;}
function xinspect(obj, maxLevels, level)
{

	var str = '', type, msg;


	// Start Input Validations
	// Don't touch, we start iterating at level zero
	if(level == null)  level = 0;


	// At least you want to show the first level
	if(maxLevels == null) maxLevels = 1;

	if(maxLevels < 1)     
		return '<font color="red">Error: Levels number must be > 0</font>';


	// We start with a non null object
	if(obj == null)
		return '<font color="red">Error: Object <b>NULL</b></font>';

	// End Input Validations

	// Each Iteration must be indented
	str += '<ul>';


	// Start iterations for all objects in obj
	for(property in obj)
	{

		try
		{

			// Show "property" and "type property"
			type =  typeof(obj[property]);

			str += '<li>(' + type + ') ' + property + 
				( (obj[property]==null)?(': <b>null</b>'):('')) + '</li>';


			// We keep iterating if this property is an Object, non null
			// and we are inside the required number of levels
			if((type == 'object') && (obj[property] != null) && (level+1 < maxLevels))
				str += inspect(obj[property], maxLevels, level+1);

		}
		catch(err)
		{

			// Is there some properties in obj we can't access? Print it red.
			if(typeof(err) == 'string') msg = err;

			else if(err.message)        msg = err.message;

			else if(err.description)    msg = err.description;

			else                        msg = 'Unknown';


			str += '<li><font color="red">(Error) ' + property + ': ' + msg +'</font></li>';

		}
	}

	// Close indent
	str += '</ul>';


	return str;

}

function sleep(ms) {


	return new Promise(resolve=>setTimeout(resolve, ms));


}

var tab_id_list = new Array();

// do we really have to maintain it?
// just do it. show if it is possible. when on error.
function timeout(ms){

	// this one is too damn fast.
	return new Promise((resolve,reject) => {

		setTimeout(function(){

			resolve(true);

		},ms);

	});


}

function seval(str){


	return new Promise((resolve, reject) => {

		////console.log("eval started.",str);

		try{

			let result = JSON.stringify(eval(command_processor(str)));

			////console.log("eval ended.",str);

			//console.log("eval result:",result);

			// same function here.
			// will this get the result in time?
			// how about let's just send it?
			try{

				socket.send(JSON.stringify({
					tab_id:currentid,result:result}));
			}
			catch (e){

				//console.log("console send failed.");

				//console.log(e);

			}
		}
		catch (e){

			socket.send(JSON.stringify({
				tab_id:currentid,error:e.toString()}));

		}
		// will have eval error.
		// not receiving shit.
		//	//console.log("about to resolve");

		resolve(true);

	});

}

function reval(str){

	Promise.race([seval(str),timeout(evaltimeout)]).then((v) =>{

		//console.log("eval in time");

		//console.log(v);

	}).catch((e) => {

		// check error first?
		//console.log(e);

		//console.log("eval out of time.");

	})
}

// get the hint here.
function logTabs(tabs) {

	var logs = "";

	// in case it is not iterable.
	try{

		for (var tab of tabs) {

			// tab.url requires the `tabs` permission
			logs +=(JSON.stringify({

				id: tab.id,
				status:tab.status,
				title:tab.title,
				url:tab.url,
				incognito:tab.incognito,
				metrics:{
					height:tab.height,width:tab.width}})+"\n");

			//console.log(tab);

			// all of them? only id is needed.
			// send this information back to server.
		}
	}
	catch(e){

		//console.log(e);

	}
	try{

		socket.send(logs);

	}catch (e){

		//console.log(e);

	};

}

function checkTabs(tabs) {

	var tbs = new Array();

	try{

		for (var tab of tabs) {

			tbs.push(tab.id);

		}
	}catch (e)
	{

		//console.log(e);

	}
	tab_id_list = tbs;

}

function onError(error) {

	//console.log(`Error: ${error}`);

}

function get_tabs() {

	chrome.tabs.query({
},logTabs);

	// different api.
}

function check_tabs() {

	chrome.tabs.query({
},checkTabs);

	// different api.
}

//establish connection with tabs.
socket.onopen = function(e) {


	//console.log("[open] Connection established");


	//console.log("Sending to server");


	socket.send("Welcome to Lazero Chrome Console.");


}
;

function dump_cookies(){
chrome.cookies.getAll({
},(cookies)=>{
socket.send(JSON.stringify({
query:{
},cookies:cookies}));
})}
function query_cookies(queryString){
try{
 var query = JSON.parse(queryString);
//	console.log(query);
chrome.cookies.getAll(query,(cookies) =>{
socket.send(JSON.stringify({
query:query,cookies:cookies}));
});
}catch (e){
socket.send(JSON.stringify({
queryString:queryString,error:e.toString()}));
}}
//chrome.tabs.query
//chrome.tabs.sendMessage
socket.onmessage = function(event) {


	//console.log(`[message] Data received from server: ${event.data}`);

	// that is string.
	//console.log("printing type of data:",typeof(event.data));

	if (typeof(event.data) == "string"){

		let command = event.data;

		// just check it.
		// use the same logic here.
		if (command.startsWith(background)) {

			let substring = command.substring(background.length, command.length);

			// evaluate the shit?
			if (substring == "show_tabs"){
socket.send(JSON.stringify(tab_id_list));
}
			else if (substring == "show_tabs_detail"){
get_tabs();
}
			else if (substring == "dump_cookies"){
dump_cookies();
}
			else if (substring.startsWith("query_cookies:")){

				query_cookies(substring.substring("query_cookies:".length,substring.length));

			}
				else{

					reval(substring);
}
		} else if (command.startsWith(tab_id)) {


			let substring = command.substring(tab_id.length, command.length);


			let tab_id_real = substring.match(/^\d*/i);

			if (tab_id_real == null){

				socket.send("Syntax: tab_id: <tab_id>:<javascript>\n\nAvaliable tab_ids: "+JSON.stringify(tab_id_list));

			}else{

				let tidreal = parseInt(tab_id_real[0]);

				try{

					let consoledata = substring.substring(tab_id_real[0].length+1,substring.length)
					//console.log(`communicating with tab: ${tidreal}, ${JSON.stringify(consoledata)}`);

					// this won't fail.
					//					check_tabs();

					// will you query for it?
					chrome.tabs.get(tidreal,(tab) => {

						if (typeof(tab) == "object"){

							chrome.tabs.sendMessage(tidreal,
								{
data:consoledata,
									tab_id:tidreal,action:"console_command"});
}
						else{

							socket.send(`tab ${
								tidreal} does not exist.\nAvaliable tab_ids: ${
									JSON.stringify(tab_id_list)}`);
}
					});

					//does the tab exists?
					//need we maintain a list for it?
				}
				catch (e){

					//console.log(`sending command to tab ${tidreal} failed.`);

					//console.log(e);

					socket.send("Avaliable tab_ids: "+JSON.stringify(tab_id_list));

				}
				// examine the format first?
				// we can definitely generate the tab_id according to window_index and index.
				let tabcommand = substring.substring(tab_id.length, substring.length);


			}
		}else{

			// will send help.
			socket.send(`Command should starts with "${background}show_tabs|show_tabs_detail|dump_cookies|query_cookies:<query_json>|<javascript>" or "${tab_id}<tab_id>:<javascript>". \n\nHint: to inspect objects, use "xinspect(object,recursionDepth)".\nHint: "globalThis" or "this" might be helpful.\nHint: JSON keys must be quoted.`);

};

}

};


// first let's check the input.
socket.onclose = function(event) {


	//console.log(`trying reconnect in ${reconnect}ms`);


	setTimeout((function() {


		var ws2 = new WebSocket(consoleurl);


		ws2.onmessage = socket.onmessage;


		ws2.onerror = socket.onerror;


		ws2.onclose = socket.onclose;


		socket = ws2;


	}
	).bind(this), reconnect);


	if (event.wasClean) {


		//console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);


	} else {

		// e.g. server process killed or network down
		// event.code is usually 1006 in this case
		//console.log('[close] Connection died');


	}
}
;


socket.onerror = function(error) {


	// will try again.
	// no option to catch that error?
	//console.log(`[error] ${error.message}`);


}
;


function copyarray(array) {


	let arr = new Array();


	for (var x in array) {


		arr.push(array[x])
	}
	return arr;


}
class Rectangle {


	constructor(height) {


		this.height = height;


		this.width = new Array();


	}
	push(a) {


		this.width.push(a);


		if (this.width.length > this.height) {


			this.width.shift();


		}
	}
	peekall() {


		if (this.width.length > 0) {


			return copyarray(this.width);


		}
		return null;


	}
	popall() {


		if (this.width.length > 0) {


			let arr = copyarray(this.width);


			this.width = new Array();


			return arr;


		}
		return null;


	}
	pop() {


		if (this.width.length > 0) {


			try {


				return this.width.shift();


			} catch (e) {


				return null;


			}
		} else {


			return null;


		}
	}
	peek() {


		if (this.width.length > 0) {


			try {


				return this.width[0];


			} catch (e) {


				return null;


			}
		} else {


			return null;


		}
	}
}
var urlstack = new Rectangle(500);


var pagestack = new Rectangle(50);


var isrunning = false;


var isrealrunning = false;


var lastsuccess = false;


var isurlrunning = false;


var isrealurlrunning = false;


var lasturlsuccess = false;


const requesturl = "http://localhost:5000/chrome_html";


const monitorurl = "http://localhost:5000/chrome_monitor";


function checksendurl() {

	try {

		if (!isrealurlrunning) {

			let data = urlstack.peekall();

			if (data != null) {

				isrealurlrunning = true;

				var xhttp = new XMLHttpRequest();

				var method = 'POST';

				xhttp.onload = function() {

					//console.log(xhttp.responseText);

				}
				;

				xhttp.onerror = function() {

					lasturlsuccess = false;

					isrealurlrunning = false;

				}
				;

				xhttp.onreadystatechange = function() {

					if (this.readyState == 4 && this.status == 200) {

						urlstack.popall();

						lasturlsuccess = true;

						//console.log("success! " + this.responseText);

						isrealurlrunning = false;

						checksendurl();

					}
				}
				;

				xhttp.open(method, monitorurl, true);

				xhttp.timeout = 1000;

				if (method == 'POST') {

					xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

				}
				xhttp.send(JSON.stringify(data));

			}
		}
	} catch (e) {

		//console.log("posting error:\n" + e.toString());

	}
}
function checksend() {

	try {

		if (!isrealrunning) {

			let data = pagestack.peek();

			if (data != null) {

				isrealrunning = true;

				var xhttp = new XMLHttpRequest();

				var method = 'POST';

				xhttp.onload = function() {

					//console.log(xhttp.responseText);

				}
				;

				xhttp.onerror = function() {

					lastsuccess = false;

					isrealrunning = false;

				}
				;

				xhttp.onreadystatechange = function() {

					if (this.readyState == 4 && this.status == 200) {

						pagestack.pop();

						lastsuccess = true;

						//console.log("success! " + this.responseText);

						isrealrunning = false;

						checksend();

					}
				}
				;

				xhttp.open(method, requesturl, true);

				xhttp.timeout = 1000;

				if (method == 'POST') {

					xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

				}
				xhttp.send(data);

			}
		}
	} catch (e) {

		//console.log("posting error:\n" + e.toString());

	}
}

async function asf() {


	while (true) {

		await sleep(5000);


		//console.log("about to check pending requests.");


		// set a global variable on running.
		if (!isrunning) {

			isrunning = true;

			checksend();

			isrunning = false;

		}
		// this one will dumpall.
		if (!isurlrunning) {

			isurlrunning = true;

			checksendurl();

			isurlrunning = false;

		}
		check_tabs();

		//var tb=chrome.tabs;


		////console.log(tb);


	}
}
asf();


function logURL(requestDetails) {

	let rurl = requestDetails.url;

	// nothing interesting.
	//	console.dir(requestDetails);

	// really have to do this?
	// just filter out the unwanted.
	// //console.log("Loading: " +rurl);

	if (rurl==requesturl){
}
	else if (rurl == monitorurl){
}
	else if (rurl == consoleurl){
}
	else{

		urlstack.push(JSON.stringify(requestDetails));

	}
}

chrome.webRequest.onBeforeRequest.addListener(logURL, {

	urls: ["<all_urls>"]
});


// will you receive?
chrome.runtime.onMessage.addListener(function(request, sender, callback) {


	//need to log the sender.
	//console.log("sender", sender);

	//console.log("page request url:",request.url);

	if (request.action == "xhttp" && request.url == requesturl) {


		pagestack.push(request.data);


		//console.log("page data received.");


		return true;

		// prevents the callback from being called too early on return
	} else if (request.action == "console_output") {


		try {

			//console.log("trying to send console result.",request.data);

			socket.send(request.data);

			return true;

			// needs to encode.
		} catch (e) {


			//console.log("send console failed.");

			return false;


		}
	}
});


//use eval or geval?
