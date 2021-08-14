let daytime = document.querySelector(".daytime");
let obon = document.querySelector(".obon");

addEventListener('keypress', function(e){
    console.log(e)
    if(e.key == "Enter"){
        daytime.classList.toggle("moving");
        obon.classList.toggle("suspention");
    }
})

