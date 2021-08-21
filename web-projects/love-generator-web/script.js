const loveForm = document.getElementById('love-form')
const loveButton = document.getElementById('love-btn')
const loveScore = document.getElementById("love-score")
const loveComment = document.getElementById("love-comment")
var crushName = document.getElementById("crush-name-text").value;

const loveNumber = Math.floor(Math.random() * 100) + 1;

loveButton.onclick = function() {
    loveForm.remove();
    loveButton.remove();
    calculateScore()
}

function calculateScore() {
    loveScore.innerText = "Your love score is " + loveNumber + "%!";

    if (loveNumber > 70) {
        loveComment.innerText = "*** You and " + crushName + "love each other like Kanye loves Kanye! ***";
    }

    if (loveNumber > 30 && loveScore <= 70) {
        loveComment.innerText = "** Something could be between you two. Fingers crossed! **";
    }

    if (loveNumber <= 30) {
        loveComment.innerText = "* You and " + crushName + "go together like oil and water! *";
    }
}