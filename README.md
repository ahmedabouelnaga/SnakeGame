# Snake Game

A simple and fun implementation of the classic Snake game using Python and the Pygame library. This project is perfect for beginners looking to learn about game development in Python.

## Features

- Classic Snake gameplay
- Score tracking
- Collision detection
- Restart or quit option after game over
- Randomly spawning food

## Prerequisites

Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

Additionally, you need to install the Pygame library. Install it using pip:

```bash
pip install pygame
```

## How to Run

1. Clone the repository or download the `snake_game.py` file.
2. Open a terminal and navigate to the directory containing the `snake_game.py` file.
3. Run the script using Python:

```bash
python snake_game.py
```

4. The game window will open. Use the arrow keys to control the snake.

## Controls

- **Arrow Keys**: Move the snake
  - Up: Move up
  - Down: Move down
  - Left: Move left
  - Right: Move right
- **Q**: Quit the game after game over
- **C**: Restart the game after game over

## Game Rules

1. The snake moves continuously in the direction of the last arrow key press.
2. Eat the red food to grow the snake and increase your score.
3. The game ends if:
   - The snake collides with the walls.
   - The snake collides with itself.

## Project Structure

```
.
├── snake_game.py     # Main Python script
├── README.md         # Project README file
```

## Improvements and Customizations

Feel free to fork this repository and add your own features! Some ideas include:

- Adding sound effects
- Introducing levels or increasing speed as the game progresses
- Implementing obstacles
- Creating a pause/resume feature

## License

This project is open-source and available under the [MIT License](LICENSE).

