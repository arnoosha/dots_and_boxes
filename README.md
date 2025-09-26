# Dots and Boxes AI

This project is an implementation of an artificial intelligence agent that plays the classic **Dots and Boxes** game.  
The AI uses **alpha-beta pruning with a heuristic evaluation function** to decide moves and aims to maximize its chances of completing boxes while minimizing the opponent’s opportunities.

## Overview

The game of Dots and Boxes is played on a grid of dots. Players take turns drawing lines between adjacent dots. When a player completes the fourth side of a box, they claim the box and take another turn. The player with the most boxes at the end of the game wins.

This project focuses on the AI agent’s decision-making process:
- Evaluating possible moves
- Detecting completed boxes
- Avoiding moves that give away boxes to the opponent
- Searching the game tree using **minimax with alpha-beta pruning**

## Features

- **Move Generation**  
  Identifies all legal moves available at any given game state.

- **Box Completion Check**  
  Detects when a move completes a square.

- **Three-Line Avoidance**  
  Prevents selecting moves that create three sides of a square, which often leads to giving the opponent a box.

- **Heuristic Function**  
  Evaluates the desirability of a move by estimating the number of boxes gained vs. boxes potentially given to the opponent.

- **Alpha-Beta Pruning**  
  Optimizes the minimax search to reduce computation and explore deeper game states within time limits.

- **Dynamic Depth Control**  
  Search depth adapts based on board size. Larger boards use shallower searches to stay efficient.

- **Time Constraint**  
  Each move is computed within a 2-second time budget to ensure responsiveness.

## How It Works

1. **State Representation**  
   The game state is represented as a list of occupied edges between grid points.

2. **Decision Process**  
   - The AI generates all possible moves.  
   - For each move, it simulates the new state and evaluates it using minimax with alpha-beta pruning.  
   - A heuristic score is computed for terminal or depth-limited states.  
   - The move with the best score is chosen.

3. **Game Termination**  
   The game ends when there are no possible moves left.

## Example Usage

```python
from dots_and_boxes_ai import Ai

# Create a 5x5 grid AI player
ai = Ai(shape=(5, 5))

# Example game state (list of edges already drawn)
state = [((0,0),(1,0)), ((1,0),(2,0)), ((0,0),(0,1))]

# Let the AI decide the best move
best_move = ai.decide(state)
print("AI chose move:", best_move)
