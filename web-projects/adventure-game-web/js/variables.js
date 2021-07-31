function selectOption(option) {
    const nextTextNodeId = option.nextText
    if (nextTextNodeId <= 0) {
        return startGame()
    }

    // Condition so that background images/credits changes in terms of scenario

    if (nextTextNodeId == 99 || nextTextNodeId == 100) {
        document.body.style.backgroundImage = magicBg
        footerCredit.innerHTML = magicFooterCredits
        footerCredit.className = "magicBgColour"
    } else if (nextTextNodeId == 97) {
        document.body.style.backgroundImage = itemsBg
        footerCredit.innerHTML = itemsFooterCredits
        footerCredit.className = "itemsBgColour"
    } else {
        document.body.style.backgroundImage = fireBg
        footerCredit.innerHTML = "Test"
        footerCredit.className = "itemsBgColour"
    }

    state = Object.assign(state, option.setState)
    showTextNode(nextTextNodeId)
}

// Theme Set 1

const fireBg = "url('./images/photo-by-jr-korpa-unsplash.jpg')"

const firePhotoLink = "https://unsplash.com/photos/NDUjrvZKMeE";
const firePhotoArtist = "https://unsplash.com/@korpa?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
const fireUnsplashLink = "https://unsplash.com/s/photos/fantasy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"

const fireFooterCredits = '<a href="' + firePhotoLink + '">Photo</a> by <a href="' + firePhotoArtist + '">Jr Korpa</a> on <a href="' + fireUnsplashLink + '">Unsplash</a>'

// Theme Set 2

const magicBg = "url('./images/photo-by-billy-huynh-unsplash.jpg')"

const magicPhotoLink = "https://unsplash.com/photos/W8KTS-mhFUE";
const magicPhotoArtist = "https://unsplash.com/@billy_huy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
const magicUnsplashLink = "https://unsplash.com/s/photos/magic?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"

const magicFooterCredits = '<a href="' + magicPhotoLink + '">Photo</a> by <a href="' + magicPhotoArtist + '">Billy Huynh</a> on <a href="' + magicUnsplashLink + '">Unsplash</a>'

// Theme Set 3

const bluefireBg = "url('./images/photo-by-patrick-hendry-unsplash.jpg')"

const bluefirePhotoLink = "https://unsplash.com/photos/lbOfqldsKEw";
const bluefirePhotoArtist = "https://unsplash.com/@worldsbetweenlines?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
const bluefireUnsplashLink = "https://unsplash.com/s/photos/magic?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"

const bluefireFooterCredits = '<a href="' + bluefirePhotoLink + '">Photo</a> by <a href="' + bluefirePhotoArtist + '">Patrick Hendry</a> on <a href="' + bluefirePhotoLink + '">Unsplash</a>'

// Theme Set 4

const itemsBg = "url('./images/photo-by-joanna-kosinska-unsplash.jpg')"

const itemsPhotoLink = "https://unsplash.com/photos/MnKWt1W1GDg";
const itemsPhotoArtist = "https://unsplash.com/@joannakosinska?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
const itemsUnsplashLink = "https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"

const itemsFooterCredits = '<a href="' + itemsPhotoLink + '">Photo</a> by <a href="' + itemsPhotoArtist + '">Joanna Kosinska</a> on <a href="' + itemsUnsplashLink + '">Unsplash</a>'