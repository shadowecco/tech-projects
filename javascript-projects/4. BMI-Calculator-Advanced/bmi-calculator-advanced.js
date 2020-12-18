function bmiCalculator (weight,height){
  var bmi = weight / Math.pow(height, 2);
  interpretation = Math.round(bmi);
  return interpretation
}

var weight = prompt("What is your weight in kg?");
var height = prompt("What is your height in m?");

if (interpretation < 18.5) {
    alert("Your BMI is " + interpretation + " so you are underweight.")
}

if (interpretation > 18.5 && loveScore <= 24.9) {
    alert("Your BMI is " + interpretation + " so you have a normal weight.")
}

if (loveScore > 24.9) {
    alert("Your BMI is " + interpretation + " so you are overweight.")
}

/*Answer should be around 20 in this case)*/