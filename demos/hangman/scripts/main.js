const words = [
  "javascript",
  "hangman",
  "Spooky",
  "programming",
  "halloween",
  "october",
  "ghost",
  "witch",
  "pumpkin",
  "candy",
  "costume",
  "scary",
  "spider",
  "zombie",
  "vampire",
  "monster",
  "skeleton",
  "werewolf",
  "haunted",
  "graveyard",
  "scream",
  "trick",
  "treat",
  "popcorn",
  "caramel",
  "apple",
  "cider",
  "candle",
  "Brownie",
  "piano",
  "guitar",
  "violin",
  "saxophone",
  "trumpet",
  "broomstick",
  "cauldron",
];
const maxIncorrectGuesses = 6;
let currentWord = "";
let guessedLetters = [];
let incorrectWordBank = [];
let incorrectGuesses = 0;

const hangmanParts = {
  head: "O",
  torso: "|",
  leftArm: "/",
  rightArm: "\\",
  leftLeg: "/",
  rightLeg: "\\",
};

function getDrawing(incorrectGuesses) {
  let head = " ";
  let torso = " ";
  let leftArm = " ";
  let rightArm = " ";
  let leftLeg = " ";
  let rightLeg = " ";

  switch (incorrectGuesses) {
    case 1:
      head = "O";
      break;
    case 2:
      head = "O";
      torso = "|";
      break;
    case 3:
      head = "O";
      torso = "|";
      leftArm = "/";
      break;
    case 4:
      head = "O";
      torso = "|";
      leftArm = "/";
      rightArm = "\\";
      break;
    case 5:
      head = "O";
      torso = "|";
      leftArm = "/";
      rightArm = "\\";
      leftLeg = "/";
      break;
    case 6:
      head = "O";
      torso = "|";
      leftArm = "/";
      rightArm = "\\";
      leftLeg = "/";
      rightLeg = "\\";
      break;
  }

  return `
     ------
     |    |
     |    ${head}
     |   ${leftArm}${torso}${rightArm}
     |   ${leftLeg} ${rightLeg}
     |
    ---
    `;
}

function newGame() {
  // Choose a random word from the list
  currentWord = words[Math.floor(Math.random() * words.length)];
  // Reset guessed letters, incorrect word bank, and incorrect guess count
  guessedLetters = [];
  incorrectWordBank = [];
  incorrectGuesses = 0;
  updateDisplay();
  document.getElementById("message").textContent = "";
  document.getElementById("incorrect-word-bank").textContent = "";
  document.getElementById("hangman-drawing").textContent =
    getDrawing(incorrectGuesses);
}

function updateDisplay() {
  // Update the displayed word based on guessed letters
  let displayedWord = "";
  for (let letter of currentWord) {
    if (guessedLetters.includes(letter)) {
      displayedWord += letter + " ";
    } else {
      displayedWord += "_ ";
    }
  }
  document.getElementById("word-display").textContent = displayedWord.trim();
}

function makeGuess() {
  const guessInput = document.getElementById("guess-input");
  const guess = guessInput.value.toLowerCase();

  // Validate input: Check if it's a single letter and is not a number
  if (guess.length !== 1 || guess < "a" || guess > "z") {
    document.getElementById("message").textContent =
      "Please enter a valid letter.";
    guessInput.value = "";
    return;
  }

  // Check if the letter has already been guessed
  if (guessedLetters.includes(guess)) {
    document.getElementById("message").textContent =
      "You've already guessed that letter.";
    guessInput.value = "";
    return;
  }

  // Add the guessed letter to the list of guessed letters
  guessedLetters.push(guess);

  // Check if the guessed letter is not in the word
  if (!currentWord.includes(guess)) {
    incorrectGuesses++;
    incorrectWordBank.push(guess);
    document.getElementById("incorrect-word-bank").textContent =
      incorrectWordBank.join(", ");
    document.getElementById("hangman-drawing").textContent =
      getDrawing(incorrectGuesses);
    if (incorrectGuesses === maxIncorrectGuesses) {
      document.getElementById(
        "message"
      ).textContent = `You've run out of guesses. The word was ${currentWord}.`;
      guessInput.disabled = true;
      return;
    }
  }

  // Update the displayed word after the guess
  updateDisplay();

  // Check if the player has guessed the word
  if (!document.getElementById("word-display").textContent.includes("_")) {
    document.getElementById("message").textContent =
      "Congratulations! You've guessed the word.";
    guessInput.disabled = true;
  }

  // Clear the guess input
  guessInput.value = "";
}

function restartGame() {
  // Reset the game to its initial state and start a new game
  guessedLetters = [];
  incorrectWordBank = [];
  incorrectGuesses = 0;
  updateDisplay();
  document.getElementById("message").textContent = "";
  document.getElementById("incorrect-word-bank").textContent = "";
  document.getElementById("hangman-drawing").textContent =
    getDrawing(incorrectGuesses);
}

// Attach event listeners to buttons
document.getElementById("submit-btn").addEventListener("click", makeGuess);
document.getElementById("new-word-btn").addEventListener("click", newGame);
document.getElementById("restart-btn").addEventListener("click", restartGame);

// Start a new game when the page loads
newGame();
