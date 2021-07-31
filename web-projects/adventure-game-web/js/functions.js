beginButton.addEventListener('click', playerIntro)

nextStepButton.addEventListener('click', setRank)

knightButton.addEventListener('click', setPlayer)
ladyButton.addEventListener('click', setPlayer)
lordButton.addEventListener('click', setPlayer)
squireButton.addEventListener('click', setPlayer)
villagerButton.addEventListener('click', setPlayer)
witchButton.addEventListener('click', setPlayer)
wizardButton.addEventListener('click', setPlayer)

startButton.addEventListener('click', startGame)

function playerIntro() {

    document.body.style.backgroundImage = magicBg
    footerCredit.innerHTML = magicFooterCredits
    footerCredit.className = "magicBgColour"

    titleElement.remove();
    beginButton.classList.add('hide')
    footerLinks.remove();
    footerCopyright.remove();

    playerElement.style.display = "block";
    nextStepButton.style.display = "block";
}

function getName() {
    var playerName = document.getElementById("user-form-text").value;
    return playerName
}

function setRank() {

    document.body.style.backgroundImage = fireBg
    footerCredit.innerHTML = fireFooterCredits
    footerCredit.className = "fireBgColour"

    nextStepButton.style.display = "none";
    playerElement.style.display = "none";
    rankElement.style.display = "block";
}

function setPlayer() {

    document.body.style.backgroundImage = bluefireBg
    footerCredit.innerHTML = bluefireFooterCredits
    footerCredit.className = "fireBgColour"

    rankElement.style.display = "none";
    startElement.style.display = "block";
    startButton.style.display = "block";

    var player_name = getName()
    var player_rank = $(this).val();

    startElement.innerText = "Welcome to Ravenbrooke, " + player_name + ". The journey will be long and difficult but you can do it. Good luck, young " + player_rank + "!"
}

function startGame() {
    state = []
    showTextNode(1)
    document.body.style.backgroundImage = itemsBg
    footerCredit.innerHTML = itemsFooterCredits
    footerCredit.className = "itemsColour"

    startElement.style.display = "none";
    startButton.style.display = "none";
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