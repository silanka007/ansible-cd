var http = require("http");
var server = http.createServer(function (req, res) {
  res.writeHead(200);
  return res.end(JSON.stringify({
    name: "Paul Silanka",
    stack: "Full-stack Software Engineer/Data",
    pushCount: 5
  }));
});
server.listen(3000);
