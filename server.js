const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({extended: true}));

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.get("/auto", function(req, res) {
  res.sendFile(__dirname + "/autoCorrect.html");
});

app.post("/", function(req, res) {
  var n1 = Number(req.body.n1);
  var n2 = Number(req.body.n2);
  var result = n1 + n2;
  res.send("" + result);
});

app.post("/auto", function(req, res) {
  var w = req.body.word;
  var spawn = require('child_process').spawn;
  console.log('spawn works');
  var process = spawn('python', ['auto_correct.py', w]);
  console.log("process works");
  var result;
  process.stdout.on('data', function(data) {
    res.send(data.toString());
  });
  
});

app.listen(3000, function() {
  console.log("-----------------------------------------");
});