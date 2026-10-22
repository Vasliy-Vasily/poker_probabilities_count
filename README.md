[Русская версия](#русский)

# Poker Counter

A small tool for estimating your win probability in Texas Hold'em using the Monte Carlo method.

---

## English

### What it does

You enter your hole cards, the board cards, and the number of players — the program generates 10,000 random deals for opponents and missing board cards, then computes the percentage of cases where your hand is the best.

### Features

- Card input format: `9 hearts 12 spades` (rank 2–14, where 11 = J, 12 = Q, 13 = K, 14 = A; suits: `hearts`, `diamonds`, `spades`, `clubs`).
- Input validation:
  - rank range,
  - allowed suits,
  - no duplicates in hand or on board,
  - no overlap between hand and board.
- Evaluation of all 9 poker hand types: from high card to straight flush, including kickers, the A-2-3-4-5 wheel, and straight flush.
- 10,000 Monte Carlo simulations.
- Output: win, tie, and loss percentages with a 95% confidence interval.

### Project structure

```
poker_probabilities_count/
│
├── main.py              # entry point
├── getting_data.py      # input & validation
├── evaluation.py        # 7-card hand evaluation
├── generation.py        # Monte Carlo simulations
├── error.py             # 95% confidence interval errors
├── research.py          # Creates graphs
├── README.md
```
### Research

This module presents research on the dependence of probabilities.
- Dependence of the probabilities of a win, draw, or loss on the number of simulations (to demonstrate convergence)
- Probability of winning, draw and losing with the same combination of cards (in hand and on the table), depending on the number of players


### Libraries

- `math`
- `random`

### Example

```
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
```

### Author

Vasily Orlov

GitHub:
https://github.com/Vasliy-Vasily
---

## Русский

# Покерный калькулятор

Небольшой инструмент для оценки вероятности выигрыша в техасском холдеме с использованием метода Монте-Карло.

### Что делает

Вы вводите свои карманные карты, карты на столе и количество игроков — программа генерирует 10 000 случайных раздач для оппонентов и недостающих карт стола, после чего вычисляет процент случаев, в которых ваша комбинация оказывается лучшей.

### Возможности

- Формат ввода карт: `9 hearts 12 spades` (номинал 2–14, где 11 = J, 12 = Q, 13 = K, 14 = A; масти: `hearts`, `diamonds`, `spades`, `clubs`).
- Проверка корректности ввода:
  - диапазон номиналов,
  - допустимые масти,
  - отсутствие дубликатов в руке и на столе,
  - отсутствие пересечения между рукой и столом.
- Оценка всех 9 покерных комбинаций: от старшей карты до стрит-флеша, с учётом кикеров, колеса A-2-3-4-5 и стрит-флеша.
- 10 000 симуляций Монте-Карло.
- Вывод: проценты побед, ничьих и поражений с 95% доверительным интервалом.

### Структура проекта

```
poker_probabilities_count/
│
├── main.py              # точка входа
├── getting_data.py      # ввод и валидация
├── evaluation.py        # оценка 7 карт
├── generation.py        # симуляции Монте-Карло
├── error.py             # погрешность для 95% доверительного интервала
├── research.py          # Строит графики
├── README.md
```

### Исследование
В этом модуле представлены исследования зависимости вероятностей
- Зависимость вероятностей победы, ничьей или проигрыша от количества симуляций (для демонстрации сходимости)
- Вероятность победы, ничьи и поражения с одной и той же комбинацией карт (на руках и на столе) в зависимости от количества игроков

### Библиотеки

- `math`
- `random`

### Пример

```
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
```
### Автор

Василий Орлов

GitHub:
https://github.com/Vasliy-Vasily
---
