var crushName = document.getElementById("crush-name-text").value;

const loveScore = Math.floor(Math.random() * 100) + 1;

document.getElementById("love-btn").onclick = function(){
    document.getElementById("love-score").innerText = "Your love score is " + loveScore + "%!"; 

    if (loveScore > 70) {
        document.getElementById("love-comment").innerText = "You and " + crushName + "love each other like Kanye loves Kanye!";
    }
    
    if (loveScore > 30 && loveScore <= 70) {
        document.getElementById("love-comment").innerText = "Something could be between you two. Fingers crossed!";
    }
    
    if (loveScore <= 30) {
        document.getElementById("love-comment").innerText = "You and " + crushName + "go together like oil and water!";
    }
}