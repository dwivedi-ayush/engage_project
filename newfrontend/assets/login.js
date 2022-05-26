let name = document.querySelector(".login-name");
let password = document.querySelector(".login-password");
let sbutton = document.querySelector(".loginButton");
console.log("hello");
version=1
sbutton.addEventListener("click",(event)=>{
    event.preventDefault();
    // fetch('http://localhost:3000/public/usernames.json')
    console.log(name.value);
    try{
    fetch("/name/"+name.value+"/"+version)
    .then(function(response){
        // return response.json();
        return response.text();
    })
    .then(function(data){
        data=JSON.parse(data.replaceAll(`'`,`"`));
        console.log(data);
        var new_password=data[0].password;
        data=data[0].username;
        
        console.log(data);
        let flag = 0;
    
        if(data===name.value && new_password===password.value){
            console.log("hello");
            flag=1;

        }
    
        if(flag==1){
            console.log("1");
            localStorage.setItem("userName",name.value);
            console.log("2");
            window.location.replace("index");
            console.log("3");
        }
        else{
            console.log("user correct username or password");

        }
    })  
    }catch{
        console.log("user correct username or password");
    }
}); 
