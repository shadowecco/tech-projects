document.getElementById("star-wars-btn").onclick = function() {
    var firstName = document.getElementById('first-name').value;
    var lastName = document.getElementById('last-name').value;
    var maidenName = document.getElementById('maiden-name').value;
    var birthTown = document.getElementById('birth-town').value;

    var subFirstName = firstName.toLowerCase().slice(0, 2)
    var subLastName = lastName.slice(0, 3)
    var subMaidenName = maidenName.slice(0, 2);
    var subBirthTown = birthTown.toLowerCase().slice(0, 3);

    var swFirstName = subLastName + subFirstName
    var swLastName = subMaidenName + subBirthTown

    document.getElementById("star-wars-name").innerText = "Your Star Wars Name is " + swFirstName[0].toUpperCase() + swFirstName.substring(1) + " " + swLastName[0].toUpperCase() + swLastName.substring(1)
};