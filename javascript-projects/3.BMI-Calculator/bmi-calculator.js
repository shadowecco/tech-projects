function bmiCalculator (weight,height){
  var bmi = weight / Math.pow(height, 2);
  return Math.round(bmi);
}

var bmi = bmiCalculator(65, 1.6)

/*Answer should be around 20 in this case)*/