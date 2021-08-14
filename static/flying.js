let daytime = document.querySelector(".daytime");
let obon = document.querySelector(".obon");

let startTime = 0;
const flyingTime = 5;
const endDistance = 90 * flyingTime;

addEventListener('keypress', function(e){
    console.log(e)
    if(e.key == "Enter"){
        // daytime.classList.toggle("moving");
        // obon.classList.toggle("down");
        document.getElementById("daytime").style.animation = "moving " + flyingTime + "s linear";
        document.getElementById("obon").style.animation = "down " + flyingTime + "s linear";
        document.getElementById("obon").getElementsByTagName("img")[0].classList.add("rotate");
        startTime = Date.now();
        
        // 一定時間ごとに距離を計算
        const intervalId = setInterval(() =>{
            let dis = calcDistance();
            if(dis >= endDistance){　
                clearInterval(intervalId);　//intervalIdをclearIntervalで指定している
                endView(dis - (( 90.0 / 1000 ) * 500));
            }
        }, 500);
    }
})


let dis = document.getElementById("distance");
function calcDistance(){
    let now = Date.now();
    console.log(now - startTime);
    var distance = ( 90 / 1000 ) * (now - startTime);
    dis.textContent = Math.floor(distance) + " km";
    return distance
}

function endView(dis){
    // window.Location.href = '/home';
    window.alert("あなたの記録は" + Math.floor(dis) + "kmです！");
    location.replace('/results/');
}
