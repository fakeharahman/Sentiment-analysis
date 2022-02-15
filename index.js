const express = require("express");
const app = express();
const path=require("path")

app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader(
      "Access-Control-Allow-Methods",
      "GET, PUT, POST, DELETE, PATCH"
    );
    res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
    next();
  });

app.use( express.static( __dirname + '/views' ));

app.get( '*', function( req, res ) {
    res.sendFile( path.join( __dirname, 'views', "index.html"));
  });

app.use("/sentiment-check", (req, res, next)=>{
    console.log("here");
    const { spawn } = require('child_process');
    const text="noob"
    const pythonProcess = spawn('python',[__dirname+"/model_prediction/make_prediction.py", text]);
    pythonProcess.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log(data);
        res.status(201).json({data: data.toString()})
    });
})

app.listen(7979,  () => console.log('listening on port 7979'));