# Tic-Tac-Toe Game

Welcome to Tic-Tac-Toe Game ! It is a Python terminal game , which runs in Code Institute mock terminal on Heroku. It allows two players to play the classic game of Tic Tac Toe. Players can enter their usernames, where one will be assigned the symbol 'X' and the other 'O'. The program also provides warnings if the input is invalid.

The  live version of my project can be found under the following link [Tic Tac Toe](https://tic-tac-toe-2024-ec215a152e15.herokuapp.com/).

<img src ="media/responsive.png" alt="Screenshot of a terminal on different screen sizes">

## How to Play
 + Run the Python script by clicking on 'Run the programm" button.
 + Enter the usernames for both players.
 + Follow the prompts to input your moves.
 + The game will display the current state of the board after each move.
 + If a player wins, the game will announce the winner, or a tie.
 + After the game ends, players can choose to play again or exit.


## Existing Features
  + Two-player gameplay.
  + Players must input their usernames.

   <img src ="media/start.png" alt ="Initital game display">

  + Assignment of 'X' and 'O' symbols to players.

  <img src ="media/user-name.png" alt ="Prompt usernames for X and O">
 
  + Updating the board accordingly on players input.

  <img src ="media/x-o-input.png" alt = "Board update X and O">

  + Input validation and error checking.
    + User must enter numbers 
    + User can not enter the same position (number) twice.

<img src ="media/invalid-input.png" alt = "Input validation message">

+ Game end promts the user to enter y/n for play again or exit the game.
+ User must enter 'y' or 'n' otherwise error message is displayed.

<img src ="media/end-game.png">

## Features left to implement
  + Graphic Design
     + Design custom symbols for 'X' and 'O'
     + Graphical User Interface (GUI)
     + Develop a user-friendly graphical interface using a Python GUI library such as Tkinter or Kivy.

## Data Model

 + The board represents the current configuration of the Tic Tac Toe game board.
 + It can be represented as a list or array containing nine elements (numbers), each corresponding to a cell on the 3x3 grid.
 + Each cell can have one of three values: 'X' (Player 1), 'O' (Player 2), or '1-9 ' (Number).

## Technology Used
 + Python 3.0
 + GitHub , Gitpod
 + Heroku

### Libraries
 + os - Miscellaneous operating system interfaces

## Testing

Manually tested this project by doing the following:
+ Passed the code through PEP8 linter and confirmed there are no issues.
+ Invalid inputs: strings when numbers are expected ,out of bound inputs, same input twice
+ Tested in my local terminal and the Code Institute Heroku Terminal

### Bugs

#### Solved bugs
 + When I wrote the code, the invalid inputs messages were not displaying. I fixed this by re-arranging the function and removing the  `os.system('cls' if os.name == 'nt' else 'clear')` from inside of While loop and placing it outside of the loop. This adjustment allows for the display of warning messages for invalid inputs.

 + On game ending , if user entered anything else instead of y/n , the game was exiting completely. I resolved this by adding `def play_again():` function and by calling it after main function is executed.

 #### Remaining Bugs

  + No bugs remaining

### Validator Testing

 + PEP8
   + No errors were returned from PEP8 validator.

<img src = "media/validator.png" alt ="Validator Python">

