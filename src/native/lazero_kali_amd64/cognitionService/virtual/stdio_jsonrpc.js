const {setup, sendNotification, sendRequest, RPCError} = require('stdio-jsonrpc')
function print(m){console.log(m);}
setup({
  onNotification(method, params) {
	  print(method);
	  print(params);
    // handle a notification
  },
  onRequest(method, params, callback) {
    // handle a request
	  print(method);
	  print(params);
//    callback(new RPCError.MethodNotFound())
callback(console.log("NOTHING TO EXECUTE."))
  }
})

sendRequest('ping').then(pong => {
  sendNotification('pong', { msg: pong })
})
.catch(err => {
	print(err);
  // something bad happened
})
