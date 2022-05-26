const fs = require('fs');
const http = require('http');
const express = require('express')
const app = express();
var path = require("path");
app.use("/assets",express.static("assets"))
// app.set('/views', path.join(__dirname, 'views'));
app.set('/public', path.join(__dirname, 'public'));
app.set('view engine', 'ejs');


app.get("/callPythonUpdate/:name/:movie",function(req,res,next){
    const{spawn}= require('child_process');
    console.log("hehe");
    console.log(req.params.movie);
    console.log(req.params.name);
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/handle_update.py',req.params.name,req.params.movie]);
    childProcess.stdout.on('data',(data)=>{
    console.log(data.toString());
});
})

function callServer(name) {
    const{spawn}=   require('child_process');
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/server.py',name]);
    childProcess.stdout.on('data',(data)=>{
        console.log("python responed",data.toString());});
  }



app.get("/name/:name/:version",function(req,res,next){
    callServer(req.params.name);
    // console.log("name server got",req.params.name);
    const{spawn}=   require('child_process');
    // var sendName=localStorage.getItem('userName');
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/get_user.py',req.params.name]);
    childProcess.stdout.on('data',(data)=>{
    res.send(data);
    console.log("1",req.params.name);
    console.log("!",req.params.name);
    
});

})


app.get("/getMovies/:version",function(req,res,next){
    // console.log("name server got",req.params.name);
    const{spawn}=   require('child_process');
    // var sendName=localStorage.getItem('userName');
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/get_movies.py']);
    childProcess.stdout.on('data',(data)=>{
    res.send(data);
    
});
})
// sending json data
var usernames = require('./public/usernames.json');
app.get("/public/usernames.json",function(req,res,next){
    res.send(usernames);
})
// just for paster response time


// handling page request
app.get("/",function(req,res){
    res.sendFile(path.join(__dirname+'/login.html'));
})
app.get("/index",function(req,res){
    res.sendFile(path.join(__dirname+'/index.html'));
})

app.listen(3000)
console.log("server is running on port 3000");

