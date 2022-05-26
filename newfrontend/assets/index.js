// const http = require('http');
// const document = require('document');

var main = document.querySelector(".main");


var genres = ["recommended"]
var recommended = [];
var name = localStorage.getItem('userName');
console.log("hello",name);
version=1;
fetch("/name/"+name+"/"+version)
.then(function(resp){
    return resp.text();
})
.then(function(data){
    // console.log(data);
    console.log(data)
    json_data=JSON.parse(data.replaceAll(`'`,`"`));
    genres.push(json_data[0].topGenre);
    // console.log(genres);
    main.innerHTML = main.innerHTML + '<div class='+genres[0]+'><h1>'+genres[0]+'</h1><div class="cards_'+genres[0]+' con"></div></div>';
    // genres.map((item,index)=>{
    //     main.innerHTML = main.innerHTML + '<div class='+item+'><h1>'+item+'</h1><div class="cards_'+item+' con"></div></div>';
    // }); 
    recommended.push(json_data[0].recommendedMovies);
    // console.log("recommended hehe",json_data[0].recommendedMovies);
    var cards_diff_array = document.querySelectorAll(".con");
    
    var arr = [];
    for (var i = 0; i < cards_diff_array.length; i++) {
      arr.push(cards_diff_array[i]);
    }
    
    console.log(genres[1]);
    genres[1]=genres[1].slice(0,5);
    genres[1].map((gen,index)=>{
        console.log("item hehe",gen);
        
        console.log("gen hehe",gen);
        main.innerHTML = main.innerHTML + '<div class='+gen+'><h1>'+gen+'</h1><div class="cards_'+gen+' con"></div></div>';
        
        
    }); 
    var cards_diff_array = document.querySelectorAll(".con");
    var arr = [];
    for (var i = 0; i < cards_diff_array.length; i++) {
        arr.push(cards_diff_array[i]);
    }
    fetch("/getMovies/"+version)
        .then(function(resp){
            return resp.text();
        })
        .then(function(data){
            
            data=JSON.parse(data.replaceAll(`'`,`"`));
            // console.log(data);
            var cards_recommended=document.querySelector(".cards_recommended");
            recommended.map((rec)=>{
                rec.map((movies)=>{
                    data.map((movie)=>{
                        // console.log("movie",movie.title);
                        if(movie.title == movies){
                            cards_recommended.innerHTML = cards_recommended.innerHTML + '<a href='+movie.href+'><div class="card"><img src='+movie.src+' alt="icon"><p class="h1">'+movie.title+'</p><p class="h2">'+movie.genre_ids+'</p></div></a>';
                        }
                    })
                })
                
            })
            arr.map((item,index)=>{
                console.log("item",item);
                data.map((movie)=>{
                    // console.log("movie2",movie);
                    movie.genre_ids.map((gen)=>{
                        if(item.classList[0]=="cards_"+gen){
                            item.innerHTML = item.innerHTML + '<a href='+movie.href+'><div class="card"><img src='+movie.src+' alt="icon"><p class="h1">'+movie.title+'</p><p class="h2">'+movie.genre_ids+'</p></div></a>';
                        }
                    })
                })
            })
            var cards = document.querySelectorAll(".con");
            cards.forEach((card)=>{
                card.addEventListener("click",(event)=>{
                    event.preventDefault();
                    var movieName=event.target.querySelectorAll("p")[0].innerHTML;
                    console.log(movieName);
                    localStorage.setItem("movie",movieName);
                    fetch("./callPythonUpdate/"+name+"/"+movieName)
                    .then(function(resp){
                        return resp.text();
                    })
                })
            })
        })

    
})




