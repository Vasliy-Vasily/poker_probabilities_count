# Poker Counter

A small tool for estimating your win probability in Texas Hold'em using the Monte Carlo method.

## What it does

You enter your hole cards, the board cards, and the number of players — the program generates 10,000 random deals for opponents and missing board cards, then computes the percentage of cases where your hand is the best.

## Features

- Card input format: `9 hearts 12 spades` (rank 2–14, where 11 = J, 12 = Q, 13 = K, 14 = A; suits: `hearts`, `diamonds`, `spades`, `clubs`).
- Input validation:
  - rank range,
  - allowed suits,
  - no duplicates in hand or on board,
  - no overlap between hand and board.
- Evaluation of all 9 poker hand types: from high card to straight flush, including kickers, the A-2-3-4-5 wheel, and straight flush.
- 10,000 Monte Carlo simulations.
- Output: win, tie, and loss percentages.

## Project structure

## Example 
Welcome to the Poker counter! Looks like someone wants to win some money
Tell me, how many players are in the game including you?
4
Nice, now tell me the values of your cards, where jack - 11, queen - 12, king - 13, ace - 14
Also tell me the suits (hearts, diamonds, spades, clubs)
Example: 9 hearts 12 spades
9 hearts 12 spades
Now, how many cards are on table now?
0
So you have 9 hearts 12 spades
Now the program will now generate 10,000 random distributions of cards among your opponents hands and calculate the probability that you currently hold the best hand.
 
In 10000 simulations you have won in 26.96 % of games, you got draw in 3.03 % of games and lost in 70.01 % of games
