# RPS Game Strategy

This document provides an in-depth explanation of the strategies used in the `RPS.py` player function to increase the player's win rate against various opponents.

## Pattern-Based Predictions

### Quincy’s Pattern

The opponent "Quincy" follows a set repeating pattern: `["R", "R", "P", "P", "S"]`. To counter this, the player function:

1. Detects that Quincy uses a predictable pattern.
2. Tracks the position in the pattern by using the current turn count modulo the pattern length.
3. Counters each move in the pattern by choosing a winning move based on Quincy's expected choice.

This allows our player to gain a consistent edge over Quincy.

## Frequency Analysis

### Mrugesh’s Frequency Analysis

"Mrugesh" tends to favor certain moves more frequently over time. To counter Mrugesh, the player:

1. Analyzes the last 10 moves to find the most common move.
2. Chooses the move that would defeat the most frequent move observed.

This frequency analysis enables the player to adapt to Mrugesh’s tendencies, increasing the win rate.

## Two-Move Sequence Predictions

### Abbey’s Sequence Prediction

"Abbey" bases moves on sequences of the player’s previous two moves. The player function:

1. Tracks the occurrences of two-move sequences in the game history.
2. Predicts the most likely response based on Abbey’s tendencies, using a dictionary to store counts of each sequence.
3. Counters Abbey’s expected choice by selecting the move that would defeat it.

This sequence tracking and prediction approach effectively anticipates Abbey’s moves.

## Decision Logic Based on Historical Plays

The player function combines multiple strategies based on historical play data to choose the best counter move. By analyzing patterns, frequencies, and sequences, the player:

- Selects the counter move with the highest likelihood of winning.
- Updates its strategy dynamically, allowing for adaptation against various opponents.

These strategies collectively contribute to a higher winning rate across different play styles.
