var http = require('http');
const fs = require("fs");
const chrome_html = "/post";
//const chrome_monitor = "/message";
var monotonic_html=0;
const port=8786;
//var monotonic_monitor=0;
//logger=require('html-differ/lib/logger')
//this is too slow.
//you can use some other abstract syntax. such as monotonic+timestamp.
const writeFileRecursive = function(path, buffer, callback){
    let lastPath = path.substring(0, path.lastIndexOf("/"));
    fs.mkdir(lastPath, {recursive: true}, (err) => {
        if (err) return callback(err);
        fs.writeFile(path, buffer, function(err){
            if (err) return callback(err);
            return callback(null);
        });
    });
}
var prev=null;
    var server = http.createServer ( function(request,response){

    response.writeHead(200,{"Content-Type":"text/plain"});
    if(request.method == "GET")
        {
            response.end("received GET request.")
        }
    else if(request.method == "POST")
        {//console.log(request.data);
		var body=[]
		request.on('data', function(data) {
      body.push(data)
      //console.log('Partial body: ' , data)
    })
    request.on('end', function() {
	    var concatBody=Buffer.concat(body)
	    if (request.url == chrome_html){
	monotonic_html+=1;
	    var next=concatBody.toString('utf-8')
	    writeFileRecursive("./emacs_post/"+Date.now()+"-"+monotonic_html+".log",next,error => {if (error) return console.log("error to write file.\n"+error.message); console.log("saved successfully");});}
	        // why are you doing it?
	    // we are going to save the file, in case that you are dumb.
      console.log('Body From '+request.url+'\nLength:',concatBody.length)
      response.writeHead(200, {'Content-Type': 'text/html'})
	    // this is not.
      response.end('post received')
    })
        }
    else
        {
            response.end("Undefined request .");
        }
});
//arbitrary path.
server.listen(port);
console.log("Server running on port "+port);
// the socket port might need some change. do not use the same port?
