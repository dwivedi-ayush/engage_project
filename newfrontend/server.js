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
app.get("/name/:name",function(req,res,next){
    // console.log("name server got",req.params.name);
    const{spawn}=   require('child_process');
    // var sendName=localStorage.getItem('userName');
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/get_user.py',req.params.name]);
    childProcess.stdout.on('data',(data)=>{
    res.send(data);
    // console.log("1",req.params.name);
    const childProcess=spawn('python',['../recommendation_engine/main/algorithms/server.py',req.params.name]);
    // console.log("!",req.params.name);
    
});
})
app.get("/getMovies",function(req,res,next){
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

var userData = require('./public/userData.json');
app.get("/userData.json",function(req,res,next){
    res.send(userData);
})

var movies = require('./public/movies.json');
app.get("/movies.json",function(req,res,next){
    res.send(movies);
})


// handling page request
app.get("/",function(req,res){
    res.sendFile(path.join(__dirname+'/login.html'));
})
app.get("/index",function(req,res){
    res.sendFile(path.join(__dirname+'/index.html'));
})

app.listen(3000)


// const port = process.env.PORT || 3000;

// const server  = http.createServer((req, res)=>{
//     res.setHeader('Content-Type', 'text/html')
//     console.log(req.url)
//     if(req.url == '/'){
//         res.statusCode = 200;
//         const data = fs.readFileSync('login.html'); 
//         res.end(data.toString());
//     }
//     else if(req.url == '/index'){
//         res.statusCode = 200;
//         const data = fs.readFileSync('index.html'); 
//         res.end(data.toString());
//     }
//     else{
//         res.statusCode = 404;
//         res.end('<h1> Not Found</h1>');
//     }
    
// })
// server.listen(port, ()=>{
//     console.log(`Server is listening on port ${port}`);

// });

// const{spawn}=   require('child_process');
// var sendName=localStorage.getItem('userName');
// var sendMovie=localStorage.getItem('movie');
// const childProcess=spawn('python',['../recommendation_engine/main/algorithms/handle_update.py',sendName,sendMovie]);
// childProcess.stdout.on('data',(data)=>{
//     console.log(data.toString());
// });