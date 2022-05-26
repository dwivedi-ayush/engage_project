let name = document.querySelector(".login-name");
let password = document.querySelector(".login-password");
let sbutton = document.querySelector(".loginButton");
console.log("hello");
sbutton.addEventListener("click",(event)=>{
    event.preventDefault();
    fetch('http://localhost:3000/public/usernames.json')
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        let flag = 0;
        data.map((item,index)=>{
            if(item.name===name.value){
                flag=1;

            }
        });
        if(flag==1){
            console.log("1");
            localStorage.setItem("userName",name.value);
            console.log("2");
            window.location.replace("index");
            console.log("3");
        }
        else{}
    })  
}); 