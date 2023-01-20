var http = require('http');
var url = require('url');
const forward = require('http-forward')
var index = 1;

http.createServer(function (req, res) {
	index = 1 - index;
	if (index == 0) {
    	   req.forward = {target:"http://10.0.0.1:8080/"};
    	   forward(req, res);
	}
	if (index == 1) {
    	   req.forward = {target:"http://10.0.0.2:8181/"};
    	   forward(req, res);
	}
}).listen(5002);

