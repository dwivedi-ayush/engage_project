// server side script

const fs = require('fs');
const http = require('http');
const express = require('express')
const app = express();
var path = require("path");
app.use("/assets",express.static("assets"))
// app.set('/views', path.join(__dirname, 'views'));
app.set('/public', path.join(__dirname, 'public'));
app.set('view engine', 'ejs');

// all the database interactions are handled by python only
// we simply call a python function to all the database transactions

// to update the database with new liked genres for a person according to each movie watched
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


// helper function helps to update the database with new movies recommended whenever the page refreshes
// it changes the ddatabase using server.py
function callServer(name) {
    const{spawn}=   require('child_process');
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/server.py',name]);
    childProcess.stdout.on('data',(data)=>{
        console.log("python responed",data.toString());});
  }


// retrives the name and other datails such as password and recommended genre for a user and is used for user auth also
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

// retrives the movies that are stored in the database
app.get("/getMovies/:version",function(req,res,next){
    // console.log("name server got",req.params.name);
    const{spawn}=   require('child_process');
    // var sendName=localStorage.getItem('userName');
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/get_movies.py']);
    childProcess.stdout.on('data',(data)=>{
    res.send(data);
    
});
})


// handling page request 

// login is the landing page
app.get("/",function(req,res){
    res.sendFile(path.join(__dirname+'/login.html'));
})
// index.html is the home page after login
app.get("/index",function(req,res){
    res.sendFile(path.join(__dirname+'/index.html'));
})

// runs at port 3000
app.listen(3000)
console.log("server is running on port 3000");

