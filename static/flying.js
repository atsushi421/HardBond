let daytime = document.querySelector(".daytime");
let obon = document.querySelector(".obon");

let startTime = 0;

let json = ""


// const flyingTime = json.time;
let flyingTime = 5;
let endDistance = 89 * flyingTime;

const animationForwards = "animation-fill-mode: forwards;";

addEventListener('keypress', function(e){
    if(e.key == "Enter"){
        // daytime.classList.toggle("moving");
        // obon.classList.toggle("down");
        console.log(json.time);
        flyingTime = json.time;
        endDistance = json.distance;
        document.getElementById("enter").style.display = "none";
        document.getElementById("daytime").style.animation = "moving " + flyingTime + "s linear";
        document.getElementById("daytime").style.animationFillMode = "forwards";
        document.getElementById("obon").style.animation = "down " + flyingTime + "s linear";
        document.getElementById("obon").style.animationFillMode = "forwards";
        document.getElementById("obon").getElementsByTagName("img")[0].style.animation = "rotate " + 1 + "s linear " + flyingTime;
        document.getElementById("obon").getElementsByTagName("img")[0].style.animationFillMode = "forwards";
        // document.getElementById("obon").getElementsByTagName("img")[0].classList.add("rotate");
        startTime = Date.now();
        
        
        // 一定時間ごとに距離を計算
        const intervalId = setInterval(() =>{
            let duaration = Math.floor((Date.now() - startTime) / 1000);
            let dis = calcDistance(duaration);
            if(duaration > flyingTime){
                clearInterval(intervalId);　//intervalIdをclearIntervalで指定している
                endView(endDistance);
            }
        }, 500);
    }
})


let dis = document.getElementById("distance");
function calcDistance(duaration){
    var distance = 89 * duaration;
    console.log(duaration)
    if(duaration <= flyingTime){
        dis.textContent = distance + " km";
    }
    return distance
}

function endView(dis){
    window.alert("あなたの記録は" + dis + "kmです！");
    location.replace('/results/');
}