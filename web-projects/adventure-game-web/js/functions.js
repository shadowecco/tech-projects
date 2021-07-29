beginButton.addEventListener('click', playerIntro)

nextStepButton.addEventListener('click', startGame)

function playerIntro() {
    titleElement.remove();
    beginButton.classList.add('hide')
    startButton.classList.add('hide')
    playerElement.style.display = "block";
    nextStepButton.style.display = "block";
    footerLinks.remove();
    footerCopyright.remove();
    document.body.style.backgroundImage = magicBg
    footerCredit.innerHTML = magicFooterCredits
    footerCredit.className = "magicBgColour"
}

function startGame() {

    document.body.style.backgroundImage = fireBg
    footerCredit.innerHTML = fireFooterCredits
    footerCredit.className = "fireBgColour"
    state = {}
    nextStepButton.style.display = "none";
    playerElement.style.display = "none";
    questElement.style.display = "block";
    showTextNode(1)
}

function showTextNode(textNodeIndex) {
    const textNode = gameArray.find(textNode => textNode.id === textNodeIndex)
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

    if (nextTextNodeId == 2 || nextTextNodeId == 100) {
        document.body.style.backgroundImage = magicBg
        footerCredit.innerHTML = magicFooterCredits
        footerCredit.className = "magicBgColour"
    } else if (nextTextNodeId == 3) {
        document.body.style.backgroundImage = itemsBg
        footerCredit.innerHTML = itemsFooterCredits
        footerCredit.className = "itemsBgColour"
    } else {
        document.body.style.backgroundImage = fireBg
        footerCredit.innerHTML = fireFooterCredits
        footerCredit.className = "fireBgColour"
    }

    state = Object.assign(state, option.setState)
    showTextNode(nextTextNodeId)
}