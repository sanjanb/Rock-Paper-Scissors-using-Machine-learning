# Rock-Paper-Scissors Machine Learning Project

This project explores advanced strategies for the classic Rock-Paper-Scissors game using machine learning concepts, frequency analysis, and predictive algorithms. Our goal is to design a `player` function that can adapt to various opponents' strategies, aiming for a high win rate. This project also serves as a learning resource for foundational machine learning concepts, game theory, and Python programming basics.

## Project Structure

The repository is organized as follows:

- **src/**: Contains the main game logic and strategy implementations.
  - `main.py`: Entrypoint for running the game simulations.
  - `RPS.py`: The core player strategy code, where different prediction strategies are implemented.
  - `RPS_game.py`: Handles game simulation between the player and various opponent strategies.
- **tests/**: Contains unit tests to validate the player's performance against predefined strategies.
  - `test_module.py`: Tests to ensure the `player` function maintains a high win rate against each opponent.
- **docs/**: Learning resources and explanations of core concepts used in the project.
  - `machine_learning.md`: An introduction to machine learning basics and their application in RPS.
  - `rps_game_strategy.md`: Detailed breakdown of strategies used in the `player` function.
  - `python_basics.md`: An overview of Python programming concepts relevant to this project.
  - `references.md`: Curated list of resources for further learning.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your_username/RPS_Game.git
   cd RPS_Game
   ```

2. **Run the game**:
   To see how well the `player` performs, you can directly run the main script:

   ```bash
   python src/main.py
   ```

3. **Run the tests**:
   Ensure the `player` function is performing as expected by running the unit tests:
   ```bash
   python -m unittest discover tests
   ```

## How the Game Works

In this project, the player function is tested against several predefined opponents, each with a unique playing strategy:

- **Quincy**: Follows a fixed sequence of moves.
- **Abbey**: Adapts based on the player's recent moves.
- **Kris**: Plays moves in response to patterns in the player’s behavior.
- **Mrugesh**: Uses frequency analysis to predict the player's next move.

The goal is to develop a `player` function that can recognize each opponent’s strategy and counter it effectively to win at least 60% of games in each match-up.

## Learning Content

### Machine Learning Concepts

- **Types of Learning**: Understand the basics of supervised, unsupervised, and reinforcement learning, and their potential applications in RPS.
- **Overfitting and Underfitting**: Learn about these common issues in machine learning models and how they affect prediction strategies.
- For more details, see [docs/machine_learning.md](docs/machine_learning.md).

### Game Strategy and Pattern Analysis

- **Pattern Recognition**: How fixed patterns (like Quincy’s strategy) can be countered.
- **Frequency Analysis**: Techniques to recognize and counter frequent moves in an opponent’s play.
- **Two-Move Sequence Prediction**: Used to detect and counter adaptive strategies like Abbey's.
- Detailed explanations are provided in [docs/rps_game_strategy.md](docs/rps_game_strategy.md).

### Python Programming Basics

- **Core Data Structures**: Learn how lists, dictionaries, and control structures are used to create effective game strategies.
- **Functions and Control Flow**: Basic function definitions, loops, and conditional statements for programming the game logic.
- **Unit Testing**: Introduction to writing unit tests in Python to verify strategy performance.
- See [docs/python_basics.md](docs/python_basics.md) for more.

### References

For further reading and a deeper understanding, check out the curated list of additional resources in [docs/references.md](docs/references.md).

## Contribution Guidelines

Contributions are welcome! To make the project more robust or add new strategies, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Make your changes** and ensure they’re well-documented.
4. **Run tests** to verify the integrity of the code.
5. **Push your branch** to your forked repository.
6. **Submit a pull request** for review.

When contributing, please ensure your code is clean, follows best practices, and includes any necessary documentation. For substantial contributions, consider creating new documentation within the `docs/` folder.

## License

This project is licensed under the MIT License. You’re free to use, modify, and distribute the code as long as you include the original license. See the [LICENSE](LICENSE) file for details.

## Committing and Pushing to GitHub

After making your changes and organizing the project files, you can initialize the Git repository and push it to GitHub:

```bash
cd RPS_Game
git init
git add .
git commit -m "Initial commit with project structure and documentation"
git remote add origin https://github.com/sanjanb/Rock-Paper-Scissors-using-Machine-learning.git
git push -u origin main
```

This completes the setup and prepares the project for version control on GitHub.

Happy coding and enjoy exploring game strategies with Rock-Paper-Scissors!

---
