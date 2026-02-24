# TSP Solver: Simulated Annealing & Genetic Algorithm

Implementations of two metaheuristic algorithms to solve the Travelling Salesperson Problem (TSP), developed for the COMP2261 Artificial Intelligence module at Durham University.

## Overview

This project tackles the TSP using two distinct approaches, each with a basic and enhanced variant:

| Algorithm | Code | Tariff | Basic | Enhanced |
|---|---|---|---|---|
| **Simulated Annealing** | SA | 5 | `AlgAbasic.py` | `AlgAenhanced.py` |
| **Genetic Algorithm** | GA | 6 | `AlgBbasic.py` | `AlgBenhanced.py` |

Both algorithms were tested on 10 city datasets ranging from 12 to 535 cities.

## Algorithms

### Simulated Annealing (Algorithm A)

**Basic** — Standard SA with random initial tour generation and 2-opt neighbourhood moves. Accepts worse solutions probabilistically based on a cooling temperature schedule.

**Enhanced** — Improvements over the basic version:
- Nearest-neighbour heuristic for initial tour construction
- Multiple neighbourhood operators: 2-opt, node insertion, and Or-opt moves
- Adaptive neighbourhood selection that favours operators producing improvements

### Genetic Algorithm (Algorithm B)

**Basic** — Standard GA with random population initialisation, tournament selection, order crossover (OX), and swap mutation.

**Enhanced** — Improvements over the basic version:
- Population seeded with nearest-neighbour heuristic tours
- Additional inversion mutation operator alongside swap mutation
- Adaptive mutation strategy
- 2-opt local search applied to offspring for hybrid GA approach

## Project Structure

```
├── city-files/                  # Input datasets (12–535 cities)
│   ├── AISearchfile012.txt
│   ├── AISearchfile017.txt
│   └── ...
├── ttsh43_for_submission/       # Submission directory
│   ├── AlgAbasic.py             # Simulated Annealing (basic)
│   ├── AlgAenhanced.py          # Simulated Annealing (enhanced)
│   ├── AlgBbasic.py             # Genetic Algorithm (basic)
│   ├── AlgBenhanced.py          # Genetic Algorithm (enhanced)
│   ├── AlgA_AISearchfile*.txt   # Best tours found by SA
│   ├── AlgB_AISearchfile*.txt   # Best tours found by GA
│   └── AISearchValidationFeedback.txt
├── skeleton_for_chosen_algorithm.py
├── validate_before_handin.py
└── algorithm_choice_options.txt
```

## Usage

Run any algorithm on a city file:

```bash
cd ttsh43_for_submission
python AlgAbasic.py ../city-files/AISearchfile042.txt
```

Validate all outputs before submission:

```bash
python validate_before_handin.py
```

## Tech

- **Language:** Python 3 (standard library only — no external packages)
- **Key modules:** `random`, `math`, `time`
