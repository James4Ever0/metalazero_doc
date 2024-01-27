// listen for checkForWord request, call getTags which includes callback to sendResponse.
// get the id of current tab.
console.log("LAZERO PLUGIN\n    -\n   |               ___  __  __\n  / \\  |    /|  /  ___ |   |  |\n \\  _\\ |__ / | /__ ___ |   |__|\n\nTo make everything\nexecutable, analyzable, controllable.");
delete chrome.debugger;
// may encounter similar situation on firefox for android.
var currentid="anonymous";

const requesturl = "http://localhost:5000/chrome_html";
// current id may only come from the request.
const evaltimeout=1000;

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

function timeout(ms){

	return new Promise((resolve,reject) => {
		setTimeout(function(){
			reject();
		},ms);
	});

}
function seval(str){

	return new Promise((resolve, reject) => {
try{
		let result = JSON.stringify(eval(str));
// same function here.
// shall you use timestamp?
		// will this get the result in time?
		//console.log("eval result:",result);
		chrome.runtime.sendMessage({
			method: "POST", action:"console_output",data:JSON.stringify({
				tab_id:currentid,result:result})},function(responseText){
					//console.log("console eval get response text",responseText);
				});
}catch (e){
// also send the result.
	chrome.runtime.sendMessage({
			method: "POST", action:"console_output",data:JSON.stringify({
				tab_id:currentid,error:e.toString()})},function(responseText){
					//console.log("console eval get response text",responseText);
				});

}
		resolve(true);
	});
}

function reval(str){

	Promise.race([seval(str),timeout(evaltimeout)]).then((v) =>{
		//console.log("eval in time");
	}).catch(() => {
		//console.log("eval out of time.");
	})
}
const maxseconds=5;

var isrunning=false;

function sleep(ms) {

	return new Promise(resolve => setTimeout(resolve, ms));
}
// do not do it twice.
// it might still be too frequent.
// but we've got rate control.
async function dfunc(ms){
	if (!isrunning){
		let count=-1;
		while(true){
			if (!isrunning){
				count+=1;
				isrunning=true;
			}else{
				break;
			};
			await sleep(ms);
			isrunning=false;
			try {
				let htmldump=document.getElementsByTagName("html");
				let htmlcontent=htmldump[0].outerHTML;
				if (document.readyState != "loading" || count==maxseconds){
					chrome.runtime.sendMessage({
						method: 'POST', action: 'xhttp',url: requesturl, data: htmlcontent}, function(responseText) {
							//console.log("has response:\n"+responseText);
						});
					//console.log("posted data length: "+htmlcontent.length);
					if(count!=maxseconds){
						isrunning=false;
						break;
					}}}catch (e) {
						alert(e);
					}}}}
dfunc(500);

document.getElementsByTagName("html")[0].onchange=function (){
	if (!isrunning){
		dfunc(500);
	};
}
// in order to send to local server, the CORS extension must be enabled.
// otherwise, it will be literally impossible.
// also pose danger to the whole shit.
chrome.runtime.onMessage.addListener(
	function (request, sender, callback) {

		//console.log("sender",sender);
		//check the api.
		if (request.action === 'console_command') {
//console.log("checking command data:");
//console.log(request.data);
currentid = request.tab_id;
// will then start the command.
reval(request.data);
			return true;

		}
		return false;
	}
);
