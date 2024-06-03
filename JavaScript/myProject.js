console.log('hi');
const getUserChoice = userInput => {
userInput = userInput.toLowerCase();
if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') {
  return userInput;
} else {
  console.log('Error!');
}
}

const getComputerChoice = () => {
  let randomNum = Math.floor(Math.random() * 3);
  switch (randomNum) {
    case 0:
    return 'rock';
    break;
    case 1:
    return 'paper';
    break;
    case 2:
    return 'scissors';
    break;
  }
}

const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
    return "The game was a tied."
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'The computer won'
    } else {
      return 'The user won'
    }
  }
  if (userChoice === 'scissors') {
    if (computerChoice === 'rock') {
      return 'The computer won'
    } else {
      return 'The user won'
    }
  }
  if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return 'The computer won'
    } else {
      return 'The user won'
    }
  }
  if (userChoice === 'bomb') {
    return "The user won"
  }
}

const playGame = () => {
  let userChoice = getUserChoice('scissors');
  let computerChoice =getComputerChoice();
  console.log(userChoice);
  console.log(computerChoice);
 console.log(determineWinner(userChoice, computerChoice));
}
playGame();
