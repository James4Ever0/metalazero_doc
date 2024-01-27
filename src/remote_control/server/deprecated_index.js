
const refreshRate=10;
var sleepTime = 1000/refreshRate;
// first let's get the screenshots.
function test_screen()
{
	console.log("screen refreshing!");
	var screen = document.getElementById("screenCanvas");
	// wait till ready?
	var ctx = screen.getContext("2d");				
	var image = new Image();
	image.src="/screenshot/"+Date.now()+".jpg";
	image.onload = function(){
		ctx.drawImage(image,0,0);
		delete image;

		setTimeout(()=>{test_screen()},sleepTime);					
	}

}
window.addEventListener("load",test_screen);
function postData(suffix,payload){
	//get base location first.
	var remoteHost = window.location.href;
	var options = {method:"POST",
		body: JSON.stringify(payload),
		headers: {"Content-Type": "application/json"}
	};
	fetch(remoteHost+suffix, options).then(res => res.json()).then(res => console.log("post response:\n"+res)); 

}
// check some buffers. regularly clear things? nope?
var global_previousCursor = {};
var global_nextCursor = {};
var keyevent = {};
function touchDown(previousCursor,nextCursor){
	var a = previousCursor;
	var b = nextCursor;
	if (a.type == "touchstart" && b.type == "mousemove"){
		if (Math.abs(a.clientX - b.x) <5 && Math.abs(a.clientY - b.Y)< 5 && Math.abs(a.timeStamp - b.timeStamp) < 2500){
			// trigger hold event? shall I? mouse down?

			postData("/mouse",{type:"mouseDown"});	
			return false;
		}					}

	return true;
}
function touchMove(previousCursor,nextCursor){var a = previousCursor;
	var b = nextCursor;
	if ((a.type == "touchstart" || a.type == "touchmove") && b.type == "touchmove"){
		var deltaX = b.clientX - a.clientX;
		var deltaY = b.clientY - a.clientY;
		postData("/mouse",{type:"mouseMove",deltaX:deltaX,deltaY:deltaY});
	}
}
function touchUp(previousCursor,nextCursor){
	var b = previousCursor;
	var a = nextCursor;
	if ((a.type == "touchstart" || a.type == "touchend") && ( b == {} || b.type == "mousemove" || b.type == "touchmove")){
		//	if (Math.abs(a.clientX - b.x) <5000 && Math.abs(a.clientY - b.Y)< 5000){
		// trigger hold event? shall I? mouse down?
		postData("/mouse",{type:"mouseUp"});					//										}					}
	}
}
function click(previousCursor,nextCursor){
	// if not fired with alt key we use it as left click.
	var a = nextCursor;
	var b = previousCursor;
	if (a.type == "click" && (b.type == "mouseup" || b.type == "touchend" || b.type == "touchstart") && Math.abs(a.timeStamp - b.timeStamp) < 2500){
		var altKey = a.altKey;
		var button = "left";
		if (altKey){button = "right";}
		postData("/mouse",{type:"click",button:button});
	}
}
function dblclick(previousCursor,nextCursor){
	// if not fired with alt key we use it as left click.
	var a = nextCursor;
	if (a.type == "click" && (b.type == "mouseup" || b.type == "touchend" || b.type == "touchstart") && Math.abs(a.timeStamp - b.timeStamp) < 2500){
		var altKey = a.altKey;
		var button = "left";
		if (altKey){button = "right";}
		postData("/mouse",{type:"doubleClick",button:button});
	}
}

document.addEventListener("touchstart",(e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	touchUp(global_previousCursor,global_nextCursor);
});
document.addEventListener("touchmove",(e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	touchMove(global_previousCursor,global_nextCursor);
});
document.addEventListener("touchend",(e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	touchUp(global_previousCursor,global_nextCursor);
});
document.addEventListener("click",(e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	click(global_previousCursor,global_nextCursor);
});
document.addEventListener("mousemove",(e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	if(touchDown(global_previousCursor,global_nextCursor)){
		postData("/mouse",{type:"mouseMove",deltaX:e.movementX,deltaY:movementY});
	}

});
document.addEventListener("mousedown", (e) => {global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	postData("/mouse",{type:"mouseDown"});
}
);
document.addEventListener("mouseup", (e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	postData("/mouse",{type:"mouseUp"});
}
);
document.addEventListener("dblclick", (e)=>{global_previousCursor = global_nextCursor;
	e.timeStamp = Date.now();
	global_nextCursor = e;
	dblclick(global_previousCursor, global_nextCursor);
}
);
const main_translate_table_key = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', '~': '~', '`': '`', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '&': '&', '*': '*', '(': '(', ')': ')', '-': '-', '_': '_', '+': '+', '=': '=', '{': '{', '}': '}', '[': '[', ']': ']', '|': '|', '\\': '\\', ':': ':', ';': ';', '"': '"', "'": "'", '<': '<', ',': ',', '>': '>', '.': '.', '?': '?', '/': '/', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'Tab': 'tab', 'Enter': 'enter', 'Escape': 'escape', 'ArrowUp': 'up', 'ArrowDown': 'down', 'ArrowLeft': 'left', 'ArrowRight': 'right', 'PageUp': 'pageup', 'PageDown': 'pagedown', 'Home': 'home', 'End': 'end', 'Backspace': 'backspace', 'Delete': 'delete', ' ': 'space'};
const modifier_translate_table_code = {'Alt': 'alt', 'Ctrl': 'ctrl', 'Shift': 'shift', 'Meta': 'meta', 'MetaLeft': 'metaleft', 'MetaRight': 'metaright', 'ShiftLeft': 'shiftleft', 'ShiftRight': 'shiftright', 'AltLeft': 'altleft', 'AltRight': 'altright', 'CtrlLeft': 'ctrlleft', 'CtrlRight': 'ctrlright'};
const modifier_keys = ["Alt","Meta","Shift","Ctrl"];
function translate_filter(key){
	var keyname = key.key;
	var keycode = key.code;
	if((Object.getOwnPropertyNames(main_translate_table_key).indexOf(keyname)!=-1) || (modifier_keys.indexOf(keyname)!=-1)){
		return true;
	}
	console.log("unknown key:\n"+"keycode:"+keycode+"\n+keyname:"+keyname)
	return false;
}

function modifier(key){
	var keyname = key.key;
	if (modifier_keys.indexOf(keyname)!=-1){
		return true;
	}
	return false;
}
function translate(key){
	var keycode = key.code;
	var keyname = key.key;
	if (translate_filter(key)){
		if (modifier(key)){
			return modifier_translate_table_code[keycode];
			// has residual work on metakeys.
		}
		return translate_table_key[keyname];
	}
	return false;

}


// prepare the translate table.
document.addEventListener("keydown", (e) =>{
	e.timeStamp = Date.now();
	keyevent = e;
	var target = translate(e);
	if (target){
		postData("/keyboard",{type:"keyDown",key:target})
	}
}
);
document.addEventListener("press", (e) =>{
	e.timeStamp = Date.now();
	keyevent = e;//just ignore this shit?
});
document.addEventListener("keyup",(e) =>{
	e.timeStamp = Date.now();
	keyevent = e;
	var target = translate(e);
	postData("/keyboard",{type:"keyUp",key:target});
});

//execute some idle cleaning jobs.

const keyboardReset = 2000;
const mouseReset = 1000;
function reset_keyboard(){

	var now = Date.now();
	var previous = keyevent.timeStamp;
	if( now-previous > keyboardReset){
		postData("/keyboard",{type:"reset"});
	};

	setTimeout(()=>{reset_keyboard()},keyboardReset);
}	
function reset_mouse(){
	var now = Date.now();
	var previous = nextCursor.timeStamp;
	if( now-previous > mouseReset){
		postData("/mouse",{type:"reset"});
	}
	setTimeout(()=>{reset_mouse()}, mouseReset);
}	

// reset all events when idle, in client and server side.
function clearText(){
	var textarea = document.getElementById("hiddenInput");
	textarea.value=""
	setTimeout(()=>{clearText()},500);
}
function focusText(){
	var textarea = document.getElementById("hiddenInput");
	textarea.focus();
	setTimeout(()=>{focusText()},200);
}
function onLoad(lambda){window.addEventListener("load",lambda);}
onLoad(clearText);
/*      function probeText(){var textarea = document.getElementById("hiddenInput");
											console.log("text: "+textarea.value);
										}
										*/
onLoad(focusText);
onLoad(reset_keyboard);
onLoad(reset_mouse);
//automatic reload? dialog?

