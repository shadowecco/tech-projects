// Title Elements

const titleElement = $('#title-container')[0]
const githubElement = $('#github-row')[0]
const beginBtn = $('#begin-btn')[0]

// Player Elements

const playerElement = $('#player-container')[0]
const nextStepBtn = $('#class-btn')[0]
const startElement = $('#start-container')[0]
const startBtn = $('#start-btn')[0]

// Rank Elements

const rankElement = $('#rank-container')[0]
const knightBtn = $('#knight-btn')[0]
const ladyBtn = $('#lady-btn')[0]
const lordBtn = $('#lord-btn')[0]
const squireBtn = $('#squire-btn')[0]
const villagerBtn = $('#villager-btn')[0]
const witchBtn = $('#witch-btn')[0]
const wizardBtn = $('#wizard-btn')[0]

// Quest Elements

const questElement = $('#quest-container')[0]
const textElement = $('#quest-text')[0]
const optionButtonsElement = $('#option-buttons')[0]

// Footer Elements

const footerElement = $("footer")[0]
const footerCopyright = $("footer")[0].getElementsByTagName("p")[0]
const footerCredit = $("footer")[0].getElementsByTagName("p")[1]

// Buttons - in the order they are clicked to activate functions

beginBtn.addEventListener('click', playerIntro)

nextStepBtn.addEventListener('click', setRank)

knightBtn.addEventListener('click', setPlayer)
ladyBtn.addEventListener('click', setPlayer)
lordBtn.addEventListener('click', setPlayer)
squireBtn.addEventListener('click', setPlayer)
villagerBtn.addEventListener('click', setPlayer)
witchBtn.addEventListener('click', setPlayer)
wizardBtn.addEventListener('click', setPlayer)

startBtn.addEventListener('click', startGame)

// Function for username/playername input

function playerIntro() {

    footerschemeMagic()

    titleElement.remove();
    beginBtn.classList.add('hide')
    footerCopyright.remove();

    playerElement.style.display = "block";
    nextStepBtn.style.display = "block";
}

function getName() {
    var playerName = document.getElementById("user-form-text").value;
    return playerName
}

// Function for rank input

function setRank() {

    footerschemeFire()

    nextStepBtn.style.display = "none";
    playerElement.style.display = "none";
    rankElement.style.display = "block";
}

// Game Intro displaying chosen name and rank

function setPlayer() {

    footerschemeblueFire()

    rankElement.style.display = "none";
    startElement.style.display = "block";
    startBtn.style.display = "block";

    var player_name = getName()
    var player_rank = $(this).val();

    startElement.innerText = "Welcome to Ravenbrooke, " + player_name + ". The journey will be long and difficult but you can do it. Good luck, young " + player_rank + "!"
}

// Start Game

function startGame() {
    state = []
    showTextNode(1)

    footerschemeItems()

    startElement.style.display = "none";
    startBtn.style.display = "none";
    questElement.style.display = "block";
    textElement.style.display = "block";

}

function showTextNode(textNodeIndex) {
    const textNode = textNodes.find(textNode => textNode.id === textNodeIndex)
    textElement.innerText = textNode.text
    while (optionButtonsElement.firstChild) {
        optionButtonsElement.removeChild(optionButtonsElement.firstChild)
    }

    textNode.options.forEach(option => {
        if (showOption(option)) {
            const button = document.createElement('button')
            button.innerText = option.text
            button.classList.add('btn')
            button.addEventListener('click', () => selectOption(option))
            optionButtonsElement.appendChild(button)
        }
    })
}

function showOption(option) {
    return option.requiredState == null || option.requiredState(state)
}

function selectOption(option) {
    const nextTextNodeId = option.nextText
    if (nextTextNodeId <= 0) {
        return startGame()
    }

    // Condition so that background images/credits changes in terms of scenario

    if (nextTextNodeId == 99 || nextTextNodeId == 100) {
        footerschemeMagic()
    } else if (nextTextNodeId == 97) {
        footerschemeItems()
    } else {
        footerschemeTest()
    }

    state = Object.assign(state, option.setState)
    showTextNode(nextTextNodeId)
}