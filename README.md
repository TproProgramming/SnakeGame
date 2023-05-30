# Snake Game

A classic Snake Game implemented in Python using the Pygame library.

## Features

- Intuitive controls: Control the snake's movement using the arrow keys (Up, Down, Left, Right) on your keyboard.
- Score system: Earn points by eating food, and keep track of your high scores.
- Top 10 high scores: The game records the top 10 high scores achieved by players.
- Game over conditions: The game ends if the snake collides with a wall or its own body.
- Play again: After each game, you can choose to play again and improve your score.

### Prerequisites

- Python3
- Pygame library

### How to Play 

1. Make sure you have Python 3.x installed on your system.
2. Install the Pygame library by running the following command: *pip install pygame*
3. Download or clone the repository.
4. Navigate to the project directory.
5. Run the game by executing the following command: *python Snake.py*
6. Control the snake's movement using the arrow keys (Up, Down, Left, Right).
7. Eat the food (red rectangles) to grow the snake and earn points.
8. Avoid colliding with the walls or the snake's own body.
9. The game ends when the snake hits a wall or its own body.
10. If you achieve a high score, you will be prompted to enter your name.
11. The top 10 high scores will be displayed at the end of each game.
12. To play again, enter 'Y' when prompted, otherwise enter 'N' to exit the game.

## Gameplay Controls

- Arrow Up: Move the snake up.
- Arrow Down: Move the snake down.
- Arrow Left: Move the snake left.
- Arrow Right: Move the snake right.

## High Scores

The game keeps track of the top 10 high scores achieved by players. The scores are saved in a file named "highscores.txt" in the following format: *Name:Score

If you achieve a high score, you will be prompted to enter your name. The high scores will be displayed at the end of each game.


## Known Issue

There is currently an error with the snake colliding with itself. As a temporary workaround, the problematic part of the code has been commented out. Without this modification, the game ends when the snake gets the first piece of food. 

## Acknowledgments

This Snake Game is based on the classic game concept and was implemented using the Pygame library.

Enjoy playing the Snake Game!
