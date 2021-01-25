
const loveScore = Math.floor(Math.random() * 100) + 1;

document.getElementById("love-btn").onclick = function(){
    document.getElementById("love-score").innerText = "Your love score is " + loveScore + "%!"; 
}
