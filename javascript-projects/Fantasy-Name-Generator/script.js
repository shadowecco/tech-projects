

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


  $( "#random-btn").click(function() {

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