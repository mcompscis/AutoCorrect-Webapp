const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({extended: true}));

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/autoCorrect.html");
});

app.post("/auto", function(req, res) {
  var w = req.body.word;
  var spawn = require('child_process').spawn;
  var process = spawn('python', ['auto_correct.py', w]);
  process.stdout.on('data', function(data) {
    var result = data.toString();
    res.render("words", { words: result});
  });
});

app.get("/result", function(req, res) {
  res.sendFile(__dirname + "/result.html");
});

app.listen(3000, function() {
  console.log("-----------------------------------------");
});