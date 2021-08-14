let daytime = document.querySelector(".daytime");
let obon = document.querySelector(".obon");

let startTime = 0;

let json = ""


// const flyingTime = json.time;
let flyingTime = 5;
const endDistance = 90 * flyingTime;



addEventListener('keypress', function(e){
    if(e.key == "Enter"){
        // daytime.classList.toggle("moving");
        // obon.classList.toggle("down");
        console.log(json.time);
        flyingTime = json.time;
        document.getElementById("daytime").style.animation = "moving " + flyingTime + "s linear";
        document.getElementById("obon").style.animation = "down " + flyingTime + "s linear";
        document.getElementById("obon").getElementsByTagName("img")[0].classList.add("rotate");
        startTime = Date.now();
        
        // 一定時間ごとに距離を計算
        const intervalId = setInterval(() =>{
            let duaration = Date.now() - startTime;
            let dis = calcDistance(duaration);
            if(duaration / 1000  > flyingTime){
                clearInterval(intervalId);　//intervalIdをclearIntervalで指定している
                endView(dis - (( 90.0 / 1000 ) * 500));
            }
        }, 500);
    }
})


let dis = document.getElementById("distance");
function calcDistance(duaration){
    var distance = ( 90 / 1000 ) * duaration;
    dis.textContent = Math.floor(distance) + " km";
    return Math.floor(distance)
}

function endView(dis){
    window.alert("あなたの記録は" + Math.floor(dis) + "kmです！");
    console.log(dis);
    console.log(endDistance);
    location.replace('/results/');
}
