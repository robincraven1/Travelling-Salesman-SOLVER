# TSP Solver: Simulated Annealing & Genetic Algorithm

Implementations of two metaheuristic algorithms to solve the Travelling Salesperson Problem (TSP).
An optimization problem aimed at finding the shortest possible route to visit a set of cities exactly once and return to the starting city.
Developed for the COMP2261 Artificial Intelligence module at Durham University.

## OVERVIEW

This project tackles the TSP using two distinct implementations, each with a basic and enhanced variant:

| Algorithm | Code | Tariff | Basic | Enhanced |
|---|---|---|---|---|
| **Simulated Annealing** | SA | 5 | `AlgAbasic.py` | `AlgAenhanced.py` |
| **Genetic Algorithm** | GA | 6 | `AlgBbasic.py` | `AlgBenhanced.py` |

10 city datasets, each containing between 12 to 535 cities.
Each algorithm outputs the shortest possible route it could find wthin each dataset. 

## ALGORITHMS

### Simulated Annealing (Algorithm A)

**BASIC VERSION** 
- Standard SA with random initial tour generation and 2-opt neighbourhood moves
- Accepts worse solutions probabilistically based on a cooling temperature schedule

**ENHANCED VERSION** 
- Nearest-neighbour heuristic for initial tour construction
- Multiple neighbourhood operators: 2-opt, node insertion, and Or-opt moves
- Adaptive neighbourhood selection that favours operators producing improvements

### Genetic Algorithm (Algorithm B)

**BASIC VERSION**
- Standard GA with random population initialisation, tournament selection, order crossover (OX), and swap mutation.

**ENHANCED VERSION** 
- Population seeded with nearest-neighbour heuristic tours
- Additional inversion mutation operator alongside swap mutation
- Adaptive mutation strategy
- 2-opt local search applied to offspring for hybrid GA approach

## PROJECT STRUCTURE

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

## HOW TO USE

To use an algorithm to find the shortest possible route within a city dataset:

```bash
cd ttsh43_for_submission                                   # cd into folder
python AlgAbasic.py ../city-files/AISearchfile042.txt      # run [alg] [dataset]
```

## FINAL NOTES

All files were validated before submission by doing the following:

```bash
python validate_before_handin.py
```
