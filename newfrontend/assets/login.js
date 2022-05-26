// client side js for login page

let name = document.querySelector(".login-name");
let password = document.querySelector(".login-password");
let sbutton = document.querySelector(".loginButton");
version=1 // for versioning (scope of improvement)
sbutton.addEventListener("click",(event)=>{
    event.preventDefault(); // prevents the page from refreshing
    console.log(name.value);
    try{
        // calls the server for user details
    fetch("/name/"+name.value+"/"+version)
    .then(function(response){
        return response.text();
        
    })
    .then(function(data){

        // truns the string data into json
        data=JSON.parse(data.replaceAll(`'`,`"`));
        
        //extracts password from the data received
        var new_password=data[0].password;
        data=data[0].username;
        
        let flag = 0;
        
        //if the password matches we change the page or else it refreshes and nothing happens
        if(data===name.value && new_password===password.value){
            console.log("hello");
            flag=1;

        }
    
        if(flag==1){
            // we store the name in the local storage for use in the next page
            localStorage.setItem("userName",name.value);
            // replace the current page with the next one
            window.location.replace("index");
            
        }
        else{
            // is user auth fails we land here
            console.log("user correct username or password");
            location.reload();

        }
    })  
    }catch{
        // if the try fails in the case of username being wrong it lands here
        
        console.log("user correct username or password");
        location.reload();
    }
}); 
