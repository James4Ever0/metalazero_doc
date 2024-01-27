// do this after the shit has been loaded?
                                        function keyboardLog(text){
                                                                                        var logger =  document.getElementById("keyboardLog");
                                                                                        logger.innerText = text;}
                                        function mouseLog(text){
                                                                                        var logger =  document.getElementById("mouseLog");
                                                                                        logger.innerText = text;}
                                        function touchLog(text){
                                                                                        var logger = document.getElementById("touchLog");
                                                                                        logger.innerText = text;
                                                                                }

                                        document.addEventListener("keydown",(e)=>{keyboardLog("keydown event\n"+JSON.stringify({key:e.key,code:e.code,altKey:e.altKey,ctrlKey:e.ctrlKey,metaKey:e.metaKey,shiftKey:e.shiftKey,type:e.type,timeStamp:e.timeStamp}));
                                                                                //      console.log("keydown event");
                                                                                //      console.log(e);
                                                                                });
                                        document.addEventListener("keypress",(e)=>{//console.log("keypress event");
                                                                                //      console.log(e);
                                                                                        keyboardLog("keypress event\n"+JSON.stringify({key:e.key,code:e.code,altKey:e.altKey,ctrlKey:e.ctrlKey,metaKey:e.metaKey,shiftKey:e.shiftKey,type:e.type,timeStamp:e.timeStamp}));
                                                                                });

                                        document.addEventListener("keyup",(e)=>{//console.log("keyup event");
                                                                                //      console.log(e);
                                                                                        keyboardLog("keyup event\n"+JSON.stringify({key:e.key,code:e.code,altKey:e.altKey,ctrlKey:e.ctrlKey,metaKey:e.metaKey,shiftKey:e.shiftKey,type:e.type,timeStamp:e.timeStamp}));
                                                                                });
                                        document.addEventListener("mousedown",(e)=>{mouseLog("mousedown event\n"+JSON.stringify({x:e.x,y:e.y,movementX:e.movementX,movementY:e.movementY,type:e.type,timeStamp:e.timeStamp,ctrlKey:e.ctrlKey,altKey:e.altKey,shiftKey:e.shiftKey,metaKey:e.metaKey}));
                                                                                });
                                        document.addEventListener("mouseup",(e)=>{mouseLog("mouseup event\n"+JSON.stringify({x:e.x,y:e.y,movementX:e.movementX,movementY:e.movementY,type:e.type,timeStamp:e.timeStamp,ctrlKey:e.ctrlKey,altKey:e.altKey,shiftKey:e.shiftKey,metaKey:e.metaKey}));
                                                                                });
                                        document.addEventListener("click",(e)=>{mouseLog("click event\n"+JSON.stringify({x:e.x,y:e.y,movementX:e.movementX,movementY:e.movementY,type:e.type,timeStamp:e.timeStamp,ctrlKey:e.ctrlKey,altKey:e.altKey,shiftKey:e.shiftKey,metaKey:e.metaKey}));
					});
                                        document.addEventListener("dblclick",(e)=>{mouseLog("dblclick event\n"+JSON.stringify({x:e.x,y:e.y,movementX:e.movementX,movementY:e.movementY,type:e.type,timeStamp:e.timeStamp,ctrlKey:e.ctrlKey,altKey:e.altKey,shiftKey:e.shiftKey,metaKey:e.metaKey}));
                                                                                });
                                        document.addEventListener("mousemove",(e)=>{mouseLog("mousemove event\n"+JSON.stringify({x:e.x,y:e.y,movementX:e.movementX,movementY:e.movementY,type:e.type,timeStamp:e.timeStamp,ctrlKey:e.ctrlKey,altKey:e.altKey,shiftKey:e.shiftKey,metaKey:e.metaKey}));
                                                                                //      console.log("mousemove event");
                                                                                //      console.log(e);
                                                                                        // must log the event contents.
                                                                                });
                                        document.addEventListener("touchstart",(e)=>{
                                                                                        var firstTouch = e.touches[0];
                                                                                        touchLog("touchstart event\n"+JSON.stringify({metaKey:e.metaKey,altKey:e.altKey,ctrlKey:e.ctrlKey,shiftKey:e.shiftKey,touches:{clientX:firstTouch.clientX,clientY:firstTouch.clientY,force:firstTouch.force,identifier:firstTouch.identifier,pageX:firstTouch.pageX,pageY:firstTouch.pageY,radiusX:firstTouch.radiusX,radiusY:firstTouch.radiusY,rotationAngle:firstTouch.rotationAngle,screenX:firstTouch.screenX,screenY:firstTouch.screenY},type:e.type,timeStamp:e.timeStamp}));
//console.log(e);
                                                                                });
                                        document.addEventListener("touchmove",(e)=>{
        var firstTouch = e.touches[0];
                                                                                        touchLog("touchmove event\n"+JSON.stringify({metaKey:e.metaKey,altKey:e.altKey,ctrlKey:e.ctrlKey,shiftKey:e.shiftKey,touches:{clientX:firstTouch.clientX,clientY:firstTouch.clientY,force:firstTouch.force,identifier:firstTouch.identifier,pageX:firstTouch.pageX,pageY:firstTouch.pageY,radiusX:firstTouch.radiusX,radiusY:firstTouch.radiusY,rotationAngle:firstTouch.rotationAngle,screenX:firstTouch.screenX,screenY:firstTouch.screenY},type:e.type,timeStamp:e.timeStamp}));
//console.log(e);

                                                                                });
                                        document.addEventListener("touchend",(e)=>{

        //      var firstTouch = e.touches[0];
                                                                                        touchLog("touchend event\n"+JSON.stringify({metaKey:e.metaKey,altKey:e.altKey,ctrlKey:e.ctrlKey,shiftKey:e.shiftKey,type:e.type,timeStamp:e.timeStamp}));
//console.log(e);

                                                                        });
                                        document.addEventListener("touchleave",(e)=>{
        var firstTouch = e.touches[0];
                                                                                        touchLog("touchleave event\n"+JSON.stringify({metaKey:e.metaKey,altKey:e.altKey,ctrlKey:e.ctrlKey,shiftKey:e.shiftKey,touches:{clientX:firstTouch.clientX,clientY:firstTouch.clientY,force:firstTouch.force,identifier:firstTouch.identifier,pageX:firstTouch.pageX,pageY:firstTouch.pageY,radiusX:firstTouch.radiusX,radiusY:firstTouch.radiusY,rotationAngle:firstTouch.rotationAngle,screenX:firstTouch.screenX,screenY:firstTouch.screenY},type:e.type,timeStamp:e.timeStamp}));
//console.log(e);


                                                                                });
                                        document.addEventListener("touchcancel",(e)=>{
                                                                                        var firstTouch = e.touches[0];
                                                                                        touchLog("touchcancel event\n"+JSON.stringify({metaKey:e.metaKey,altKey:e.altKey,ctrlKey:e.ctrlKey,shiftKey:e.shiftKey,touches:{clientX:firstTouch.clientX,clientY:firstTouch.clientY,force:firstTouch.force,identifier:firstTouch.identifier,pageX:firstTouch.pageX,pageY:firstTouch.pageY,radiusX:firstTouch.radiusX,radiusY:firstTouch.radiusY,rotationAngle:firstTouch.rotationAngle,screenX:firstTouch.screenX,screenY:firstTouch.screenY},type:e.type,timeStamp:e.timeStamp}));
//console.log(e);


                                                                                });
                                        // reset all events when idle, in client and server side.
                                        function clearText(){
                                                                                        var textarea = document.getElementById("hiddenInput");
                                                                                        textarea.value="";
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
