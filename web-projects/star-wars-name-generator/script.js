document.getElementById("star-wars-btn").onclick = function() {

    const allianceList = ["Jedi", "Sith", "Neutral", "Rebel Alliance", "Galactic Empire", "Resistance", "First Order"]
    var ranAlliance = allianceList[Math.floor(Math.random() * allianceList.length)];

    var firstName = document.getElementById('first-name').value;
    var lastName = document.getElementById('last-name').value;
    var maidenName = document.getElementById('maiden-name').value;
    var birthTown = document.getElementById('birth-town').value;

    var subFirstName = firstName.toLowerCase().slice(0, 2);
    var subLastName = lastName.slice(0, 3);
    var subMaidenName = maidenName.slice(0, 2);
    var subBirthTown = birthTown.toLowerCase().slice(0, 3);

    var swFirstName = subLastName + subFirstName
    var swLastName = subMaidenName + subBirthTown

    document.getElementById("star-wars-name").innerText = "Your Star Wars Name is " + swFirstName[0].toUpperCase() + swFirstName.substring(1) + " " + swLastName[0].toUpperCase() + swLastName.substring(1)

    if (ranAlliance == "Neutral") {
        document.getElementById("star-wars-alliance").innerText = "Your alliance is " + ranAlliance;
    } else {
        document.getElementById("star-wars-alliance").innerText = "Your alliance is with the " + ranAlliance;
    }
}; 