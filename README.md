# TSP Solver: Simulated Annealing & Genetic Algorithm

4 Implementations of metaheuristic algorithms that aim to solve the Travelling Salesperson Problem (TSP). <br>
Each algorithm tries to find the shortest possible route to visit a set of cities exactly once and return to the starting city. <br>

## Overview

4 Algorithms - (basicA, basicB, enhancedA, enhancedB) to solve 10 city datasets, each containing between 12 to 535 cities <br>

| Algorithm | Code | Tariff | Basic | Enhanced |
|---|---|---|---|---|
| **Simulated Annealing** | SA | 5 | `AlgAbasic.py` | `AlgAenhanced.py` |
| **Genetic Algorithm** | GA | 6 | `AlgBbasic.py` | `AlgBenhanced.py` |

## TSP Solver Algorithms 

#### 1) AlgAbasic.py -- Simulated Annealing (Basic)

- Standard SA with random initial tour generation and 2-opt neighbourhood moves
- Accepts worse solutions probabilistically based on a cooling temperature schedule
 
#### 2) AlgAenhanced.py -- Simulated Annealing (Enhanced)

- Nearest-neighbour heuristic for initial tour construction
- Multiple neighbourhood operators: 2-opt, node insertion, and Or-opt moves
- Adaptive neighbourhood selection that favours operators producing improvements

#### 3) AlgBbasic.py -- Genetic Algorithm (Basic)

- Standard GA with random population initialisation, tournament selection
- As well as order crossover (OX), and swap mutation

#### 4) AlgBenhanced.py -- Genetic Algorithm (Enhanced)

- Population seeded with nearest-neighbour heuristic tours
- Additional inversion mutation operator alongside swap mutation
- Adaptive mutation strategy
- 2-opt local search applied to offspring for hybrid GA approach

## Project Structure

```
├── city-files/                          # Each city dataset (12–535 cities)
│   ├── AISearchfile012.txt
│   ├── AISearchfile017.txt
│   └── ...
├── ttsh43_for_submission/               # Submission directory
│   ├── AlgAbasic.py                     # Simulated Annealing (basic)
│   ├── AlgAenhanced.py                  # Simulated Annealing (enhanced)
│   ├── AlgBbasic.py                     # Genetic Algorithm (basic)
│   ├── AlgBenhanced.py                  # Genetic Algorithm (enhanced)
│   ├── AlgA_AISearchfile*.txt           # Best tour found by SA, one for each dataset
│   ├── AlgB_AISearchfile*.txt           # Best tour found by GA, one for each dataset
│   └── AISearchValidationFeedback.txt   # Feedback on validation check of files  
├── validate_before_handin.py            # Validation check of files, feedback is inside ttsh43
```

## How to use

To use an algorithm to attempt to find the shortest possible route of a city dataset:

```bash
cd ttsh43_for_submission                                   # cd into folder
python AlgAbasic.py ../city-files/AISearchfile042.txt      # run [alg] [dataset]
```

## Algorithm Results

Running the above will generate a solution file that details the shortest route the algorithm COULD find.
There are (2 enhanced algorithms * 10 city datasets) different solution files.
Please read them, these are found inside ttsh43_for_submission

