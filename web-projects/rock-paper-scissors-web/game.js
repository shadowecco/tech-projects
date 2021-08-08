// DOM Elements

const userScore = document.getElementById('user-score');
const userChoice = document.getElementById('user-choice');
const userChoiceText = document.getElementById('user-choice-text');

const computerScore = document.getElementById('computer-score');
const computerChoice = document.getElementById('computer-choice');
const computerChoiceText = document.getElementById('computer-choice-text');

const resultText = document.getElementById('results');

const userRock = document.getElementById('user-r');
const userPaper = document.getElementById('user-p');
const userScissors = document.getElementById('user-s');

const computerRock = document.getElementById('computer-r');
const computerPaper = document.getElementById('computer-p');
const computerScissors = document.getElementById('computer-s');

const allGameIcons = document.querySelectorAll('.far');


//Which icon beats which in the game

const choices = {
    rock: { name: 'Rock', defeats: ['scissors'] },
    paper: { name: 'Paper', defeats: ['rock'] },
    scissors: { name: 'Scissors', defeats: ['paper'] },
  };

let userScoreNumber = 0;
let computerScoreNumber = 0;
let computerRanChoice = '';

// Reset all 'selected' icons

function resetSelected() {
    allGameIcons.forEach((icon) => {
      icon.classList.remove('selected');
    });
  }

// Reset score & userChoice/computerChoice

function resetAll() {
    userScoreNumber = 0;
    computerScoreNumber = 0;
    userScore.textContent = userScoreNumber;
    computerScore.textContent = computerScoreNumber;
    userChoiceText.textContent = '';
    computerChoiceText.textContent = '';
    resultText.textContent = 'Make your move!';
     resetSelected();
}

// Random computer choice

function computerRandomChoice() {
    const computerChoiceNumber = Math.floor(Math.random() * 3);
        if (computerChoiceNumber === 0) {
          computerRanChoice = 'rock';
        } else if (computerChoiceNumber === 1) {
          computerRanChoice = 'paper';
        } else {
          computerRanChoice = 'scissors';
        }
        return(computerRanChoice)
      }


// Add 'selected' styling & computerChoice

function displayComputerChoice(computerRanChoice) {
    var computerRanChoice = computerRandomChoice();
   switch (computerRanChoice) {
     case 'rock':
       computerRock.classList.add('selected');
      computerChoiceText.textContent = ' --- Rock';
       break;
     case 'paper':
       computerPaper.classList.add('selected');
      computerChoiceText.textContent = ' --- Paper';
       break;
     case 'scissors':
       computerScissors.classList.add('selected');
       computerChoiceText.textContent = ' --- Scissors';
       break;
     default:
       break;
   }
}

// Check result, increase scores, update resultText

function updateScore(userChoice) {
    if (userChoice === computerRanChoice) {
         resultText.textContent = "It's a tie.";
     } else {
          const choice = choices[userChoice];
          if (choice.defeats.indexOf(computerRanChoice) > -1) {
              resultText.textContent = 'You Won!';
              userScoreNumber++;
              userScore.textContent = userScoreNumber;
          } else {
              resultText.textContent = 'You Lost!';
             computerScoreNumber++;
             computerScore.textContent = computerScoreNumber;
         }
     }
 }

// Call functions to process turn

function checkResult(userChoice) {
    resetSelected();
    computerRandomChoice();
    displayComputerChoice();
    updateScore(userChoice);
}

 // Passing player selection value and styling icons
 
function select(userChoice) {
    checkResult(userChoice)
  // Add 'selected' styling & userChoice
  switch (userChoice) {
    case 'rock':
        userRock.classList.add('selected');
        userChoiceText.textContent = ' --- Rock';
      break;
    case 'paper':
      userPaper.classList.add('selected');
      userChoiceText.textContent = ' --- Paper';
      break;
    case 'scissors':
    userScissors.classList.add('selected');
    userChoiceText.textContent = ' --- Scissors';
      break;
    default:
      break;
  }
}