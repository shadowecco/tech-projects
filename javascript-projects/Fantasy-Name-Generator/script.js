
// Function for when "Female" button is pushed.
// Takes random line from female_names text and last_names text.
// Display them on webpage.

$( "#female-btn").click(function() {
    var femNameTxt = $.get('female_names.txt', function (txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var feName = lines[randLineNum];

    var laNameTxt = $.get('last_names.txt', function(txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var laName = lines[randLineNum];

        document.getElementById("fantasy-name").innerText="Your new name is " + feName + " " + laName;

    });

        });
  });


 // Function for when "Male" button is pushed.
// Takes random line from male_names text and last_names text.
// Display them on webpage.





  $( "#male-btn").click(function() {
    var maleNameTxt = $.get('male_names.txt', function (txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var maleName = lines[randLineNum];

    var laNameTxt = $.get('last_names.txt', function(txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var laName = lines[randLineNum];

        document.getElementById("fantasy-name").innerText="Your new name is " + maleName + " " + laName;

    });

        });
  });

// Function for when "Random" button is pushed.
// Takes random line from female_names text, male_names text and last_names text.
// Will randomly pick a gender from array and will display gender name along with last name on page.

  $( "#random-btn").click(function() {

// Array so a gender can be selected at random
    var ranGender = ['female', 'male']
    var ranName = ranGender[Math.floor(Math.random()*ranGender.length)];
    
    var maleNameTxt = $.get('male_names.txt', function (txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var maleName = lines[randLineNum];

    var femNameTxt = $.get('female_names.txt', function (txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var feName = lines[randLineNum];
    
    // Last name will display regardless of gender

    var laNameTxt = $.get('last_names.txt', function(txt) {
        var lines = txt.split("\n");
        var randLineNum = Math.floor(Math.random() * lines.length);
        var laName = lines[randLineNum];

    if (ranName === 'male') {
        document.getElementById("fantasy-name").innerText="Your new name is " + maleName + " " + laName;
    } else if (ranName === 'female') {
        document.getElementById("fantasy-name").innerText="Your new name is " + feName + " " + laName
    }
        
    });
});
        });
  });