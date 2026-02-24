############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
############ DO NOT INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random
from datetime import datetime

############ START OF SECTOR 0 (IGNORE THIS COMMENT)
############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES MIGHT NOT RUN WHEN I RUN THEM! DO NOT TOUCH MY COMMENTS EITHER!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW IS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, IN LOWER CASE, E.G., 'abcd12', WHICH IN TURN SITS 
############ IN ANOTHER FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO 
############ MATTER HOW THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS  
############ ASSUMED THAT THE CITY FILE IS IN THE FOLDER 'city-files'.
############
############ END OF SECTOR 0 (IGNORE THIS COMMENT)

input_file = "AISearchfile012.txt"

############ START OF SECTOR 1 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

############ END OF SECTOR 1 (IGNORE THIS COMMENT)

############ START OF SECTOR 2 (IGNORE THIS COMMENT)
path_for_city_files = os.path.join("..", "city-files")
############ END OF SECTOR 2 (IGNORE THIS COMMENT)

############ START OF SECTOR 3 (IGNORE THIS COMMENT)
path_to_input_file = os.path.join(path_for_city_files, input_file)
if os.path.isfile(path_to_input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_to_input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the city-file folder.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############
############ END OF SECTOR 3 (IGNORE THIS COMMENT)

############ START OF SECTOR 4 (IGNORE THIS COMMENT)
path_for_alg_codes_and_tariffs = os.path.join("..", "alg_codes_and_tariffs.txt")
############ END OF SECTOR 4 (IGNORE THIS COMMENT)

############ START OF SECTOR 5 (IGNORE THIS COMMENT)
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############
############ END OF SECTOR 5 (IGNORE THIS COMMENT)

my_user_name = "ttsh43"

############ START OF SECTOR 6 (IGNORE THIS COMMENT)
############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############
############ END OF SECTOR 6 (IGNORE THIS COMMENT)

my_first_name = ""
my_last_name = ""

############ START OF SECTOR 7 (IGNORE THIS COMMENT)
############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############
############ END OF SECTOR 7 (IGNORE THIS COMMENT)

algorithm_code = "GA"

############ START OF SECTOR 8 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

start_time = time.time()

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER. NOTE THAT I CALCULATE THE TIME OF
############ A RUN USING THE RESERVED VARIABLE 'start_time' AND INCLUDE THE RUN-TIME IN 'added_note' LATER.
############
############ IN FACT, YOU CAN INCLUDE YOUR ADDED NOTE IMMEDIATELY BELOW OR EVEN INCLUDE YOUR ADDED NOTE
############ AT ANY POINT IN YOUR PROGRAM: JUST DEFINE THE STRING VARIABLE 'added_note' WHEN YOU WISH
############ (BUT DON'T REMOVE THE ASSIGNMENT IMMEDIATELY BELOW).
############
############ END OF SECTOR 8 (IGNORE THIS COMMENT)

added_note = "Genetic Algorithm basic implementation"

############ START OF SECTOR 9 (IGNORE THIS COMMENT)
############
############ NOW YOUR CODE SHOULD BEGIN BUT FIRST A COMMENT.
############
############ IF YOU ARE IMPLEMENTING GA THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'pop_size' TO DENOTE THE SIZE OF YOUR POPULATION (THIS IS '|P|' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING AC THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_ants' TO DENOTE THE NUMBER OF ANTS (THIS IS 'N' IN THE PSEUDOCODE)
############
############ IF YOU ARE IMPLEMENTING PS THEN:
############  - IF YOU EXECUTE YOUR MAIN LOOP A FIXED NUMBER OF TIMES THEN USE THE VARIABLE 'max_it' TO DENOTE THIS NUMBER
############  - USE THE VARIABLE 'num_parts' TO DENOTE THE NUMBER OF PARTICLES (THIS IS 'N' IN THE PSEUDOCODE)
############
############ DOING THIS WILL MEAN THAT THIS INFORMATION IS WRITTEN WITHIN 'added_note' IN ANY TOUR-FILE PRODUCED.
############ OF COURSE, THE VALUES OF THESE VARIABLES NEED TO BE ACCESSIBLE TO THE MAIN BODY OF CODE.
############ IT'S FINE IF YOU DON'T ADOPT THESE VARIABLE NAMES BUT THIS USEFUL INFORMATION WILL THEN NOT BE WRITTEN TO ANY
############ TOUR-FILE PRODUCED BY THIS CODE.
############
############ END OF SECTOR 9 (IGNORE THIS COMMENT)

############################################################################
# GENETIC ALGORITHM (GA) FOR THE TRAVELLING SALESMAN PROBLEM
# -----------------------------------------------------------------------
# BASIC IMPLEMENTATION
#
# A Genetic Algorithm is an evolutionary metaheuristic inspired by
# natural selection and genetics. It maintains a POPULATION of candidate
# solutions (tours) and iteratively evolves them over GENERATIONS using:
#   - SELECTION: Choose fit parents (short tours) to reproduce.
#   - CROSSOVER: Combine two parents to create a child tour.
#   - MUTATION: Randomly perturb a child to maintain diversity.
#   - REPLACEMENT: The new generation of children replaces the old.
#
# For the TSP, each individual is a permutation of city indices
# representing a complete tour. Fitness is defined as the negative of
# tour length (so shorter tours have higher fitness).
#
# This basic implementation uses:
#   - Random initialisation (all individuals are random permutations)
#   - Tournament selection (select the best from a random sample)
#   - Order Crossover (OX) (a crossover operator designed for permutations)
#   - Swap mutation (exchange two random cities)
#   - Full generational replacement (entire population replaced each gen)
############################################################################

# ========================== GA PARAMETERS ==========================

# pop_size: The number of individuals in the population (|P| in pseudocode).
# A larger population provides more genetic diversity but costs more
# computation per generation. 50 is a common moderate choice.
pop_size = 50

# max_it: The maximum number of generations (iterations of the main loop).
# Each generation involves selection, crossover, and mutation for the
# entire population. 500 generations should be enough for convergence
# on small-to-medium instances.
max_it = 500

# mutation_rate: The probability that a child undergoes mutation after
# crossover. A rate of 0.1 means roughly 10% of children are mutated.
# Too high → too much randomness, destroys good solutions.
# Too low → population converges prematurely, lacks diversity.
mutation_rate = 0.1

# tournament_size: The number of individuals randomly sampled for each
# tournament selection. Larger tournaments apply stronger selection
# pressure (fitter individuals are more likely to win). With size 5
# out of 50, there is moderate selection pressure.
tournament_size = 5


def calculate_tour_length(a_tour):
    """
    Calculate the total distance of a complete tour (Hamiltonian cycle).

    Sums edge weights along the tour and closes the cycle back to start.

    Parameters:
        a_tour (list[int]): A permutation of city indices 0..num_cities-1.

    Returns:
        int: Total tour distance.
    """
    total_length = 0
    n = len(a_tour)
    # Sum distances between consecutive cities in the tour
    for i in range(n - 1):
        total_length += dist_matrix[a_tour[i]][a_tour[i + 1]]
    # Close the cycle: edge from last city back to first
    total_length += dist_matrix[a_tour[n - 1]][a_tour[0]]
    return total_length


def generate_random_tour():
    """
    Generate a random tour by creating [0, 1, ..., num_cities-1]
    and shuffling it into a random permutation.

    Returns:
        list[int]: A random permutation of city indices.
    """
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour


def initialize_population():
    """
    Create the initial population of random tours.

    Each of the pop_size individuals is an independently generated random
    permutation. This provides maximum diversity in the initial population,
    but the tours are typically very poor quality. The GA must evolve them
    over many generations to reach good solutions.

    Returns:
        list[list[int]]: A population of pop_size random tours.
    """
    population = []
    for _ in range(pop_size):
        individual = generate_random_tour()
        population.append(individual)
    return population


def calculate_fitness(individual):
    """
    Calculate the fitness of an individual (tour).

    In the TSP, we want to MINIMISE tour length. However, genetic algorithms
    traditionally MAXIMISE fitness. To reconcile this, we define fitness as
    the NEGATIVE of tour length:
        fitness = -tour_length

    This way, shorter tours have higher (less negative) fitness values,
    and the GA's selection mechanisms correctly favour shorter tours.

    Parameters:
        individual (list[int]): A tour (permutation of city indices).

    Returns:
        int: The fitness value (negative tour length).
    """
    tour_len = calculate_tour_length(individual)
    # Negate so that shorter tours have higher fitness
    return -tour_len


def tournament_selection(population, fitnesses):
    """
    Select one parent using tournament selection.

    Algorithm:
        1. Randomly sample tournament_size individuals from the population.
        2. Return a copy of the individual with the highest fitness.

    Tournament selection is popular because:
    - It provides adjustable selection pressure (via tournament_size).
    - It does not require sorting the entire population.
    - It works well with negative fitness values (unlike roulette wheel).

    With tournament_size = 5 and pop_size = 50, each tournament samples
    10% of the population, giving moderate selection pressure.

    Parameters:
        population (list[list[int]]): The current population of tours.
        fitnesses (list[int]): Fitness values corresponding to each individual.

    Returns:
        list[int]: A copy of the winning individual (the selected parent).
    """
    # Randomly choose tournament_size distinct indices from the population
    tournament_indices = random.sample(range(len(population)), tournament_size)
    # Find the individual with the best (highest) fitness in the tournament
    best_idx = tournament_indices[0]
    best_fitness = fitnesses[best_idx]
    for idx in tournament_indices[1:]:
        if fitnesses[idx] > best_fitness:
            best_fitness = fitnesses[idx]
            best_idx = idx
    # Return a COPY of the winner (so mutations don't affect the original)
    return population[best_idx][:]


def order_crossover(parent1, parent2):
    """
    Perform Order Crossover (OX) to produce one child from two parents.

    OX is specifically designed for permutation-based representations
    (like TSP tours). It preserves the relative ordering of cities from
    each parent while ensuring the child is a valid permutation.

    Algorithm:
        1. Choose two random crossover points: point1 < point2.
        2. Copy the segment parent1[point1..point2] into the child at
           the same positions.
        3. Starting from position (point2 + 1), fill the remaining child
           positions with cities from parent2 (wrapping around), skipping
           any city already present in the child.

    Example:
        parent1 = [1, 2, 3, 4, 5, 6, 7, 8]
        parent2 = [3, 7, 5, 1, 6, 8, 2, 4]
        point1 = 2, point2 = 4
        Step 2: child = [_, _, 3, 4, 5, _, _, _]  (copied from parent1)
        Step 3: Fill from parent2 starting after point2:
                parent2 order from pos 5: [8, 2, 4, 3, 7, 5, 1, 6]
                Skip 3, 4, 5 (already in child): [8, 2, 7, 1, 6]
                child = [7, 1, 3, 4, 5, 6, 8, 2]

    Parameters:
        parent1 (list[int]): The first parent tour.
        parent2 (list[int]): The second parent tour.

    Returns:
        list[int]: The child tour (a valid permutation).
    """
    n = len(parent1)
    # Choose two random crossover points (point1 < point2)
    point1 = random.randint(0, n - 2)
    point2 = random.randint(point1 + 1, n - 1)

    # Initialise child with -1 placeholders (unfilled positions)
    child = [-1] * n

    # Step 2: Copy the segment from parent1 directly into the child
    for i in range(point1, point2 + 1):
        child[i] = parent1[i]

    # Build a set of cities already in the child for O(1) lookup
    child_set = set(child[point1:point2 + 1])

    # Step 3: Fill remaining positions with cities from parent2
    # Start filling from the position after point2, wrapping around
    current_pos = (point2 + 1) % n
    for i in range(n):
        # Iterate through parent2 starting from (point2 + 1), wrapping
        city = parent2[(point2 + 1 + i) % n]
        if city not in child_set:
            # Place this city in the next available position
            child[current_pos] = city
            current_pos = (current_pos + 1) % n

    return child


def swap_mutation(individual):
    """
    Perform swap mutation: select two random distinct positions and
    exchange the cities at those positions.

    Example:
        Before: [A, B, C, D, E], swap positions 1 and 3
        After:  [A, D, C, B, E]

    Swap mutation makes a small, localised change. It breaks and creates
    at most 4 edges in the tour. This is a simple mutation operator that
    maintains the permutation property (every city appears exactly once).

    Parameters:
        individual (list[int]): The tour to mutate.

    Returns:
        list[int]: A new mutated tour.
    """
    n = len(individual)
    mutated = individual[:]  # Work on a copy to preserve the original
    # Pick two distinct random positions
    pos1 = random.randint(0, n - 1)
    pos2 = random.randint(0, n - 1)
    while pos2 == pos1:
        pos2 = random.randint(0, n - 1)
    # Swap the cities at those positions
    mutated[pos1], mutated[pos2] = mutated[pos2], mutated[pos1]
    return mutated


def genetic_algorithm():
    """
    Main Genetic Algorithm for TSP (basic version).

    Follows the standard GA pseudocode from lectures:

        1. P <- initialise_population(pop_size)
        2. Evaluate fitness of all individuals in P
        3. best <- fittest individual in P
        4. FOR generation = 1 TO max_it:
            4a. P' <- empty population
            4b. WHILE |P'| < pop_size:
                  i.   parent1 <- tournament_select(P)
                  ii.  parent2 <- tournament_select(P)
                  iii. child <- order_crossover(parent1, parent2)
                  iv.  IF random() < mutation_rate THEN
                           child <- swap_mutation(child)
                  v.   Add child to P'
            4c. P <- P'                          [full generational replacement]
            4d. Evaluate fitness of all in P
            4e. IF fittest(P) > best THEN best <- fittest(P)
        5. RETURN best

    Full generational replacement means the ENTIRE population is replaced
    each generation. This is simple but has a weakness: the best solution
    can be lost if it is not selected as a parent or if crossover/mutation
    degrades it. (The enhanced version addresses this with elitism.)

    Returns:
        tuple: (best_tour, best_length) — the shortest tour found.
    """
    # ---- STEP 1: Initialise the population with random tours ----
    population = initialize_population()

    # ---- STEP 2: Evaluate fitness of every individual ----
    # fitness[i] = -tour_length(population[i]), so higher = better
    fitnesses = [calculate_fitness(ind) for ind in population]

    # ---- STEP 3: Record the best individual seen so far ----
    best_idx = fitnesses.index(max(fitnesses))
    best_tour = population[best_idx][:]
    best_length = calculate_tour_length(best_tour)

    # ---- STEP 4: Main evolutionary loop (one iteration = one generation) ----
    for iteration in range(max_it):
        # Check the 55-second time limit before each generation
        if (time.time() - start_time) >= 55:
            break

        # ---- STEP 4a-b: Create the next generation ----
        new_population = []

        # Generate pop_size children through selection, crossover, mutation
        while len(new_population) < pop_size:
            # STEP 4b-i & ii: Select two parents via tournament selection
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)

            # STEP 4b-iii: Create a child by combining the two parents
            # Order Crossover preserves relative city orderings from parents
            child = order_crossover(parent1, parent2)

            # STEP 4b-iv: Mutate the child with probability mutation_rate
            # This introduces random variation to prevent premature convergence
            if random.random() < mutation_rate:
                child = swap_mutation(child)

            # Add the child to the new population
            new_population.append(child)

        # ---- STEP 4c: Replace the old population entirely ----
        # This is "full generational replacement" — the old population is
        # completely discarded. The best solution from the previous generation
        # is NOT guaranteed to survive (a weakness addressed by elitism).
        population = new_population

        # ---- STEP 4d: Evaluate fitness of the new population ----
        fitnesses = [calculate_fitness(ind) for ind in population]

        # ---- STEP 4e: Update the global best if a better tour was found ----
        current_best_idx = fitnesses.index(max(fitnesses))
        current_best_length = calculate_tour_length(population[current_best_idx])
        if current_best_length < best_length:
            best_tour = population[current_best_idx][:]
            best_length = current_best_length

    # ---- STEP 5: Return the best tour found across all generations ----
    return best_tour, best_length


# ========================== RUN THE ALGORITHM ==========================
# Execute the GA and store results in the reserved variables 'tour' and
# 'tour_length' expected by the template code.
tour, tour_length = genetic_algorithm()

############ START OF SECTOR 10 (IGNORE THIS COMMENT)
############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############
############ DO NOT EDIT ANY TOUR FILE! ALL TOUR FILES MUST BE LEFT AS THEY WERE ON OUTPUT.
############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

end_time = time.time()
elapsed_time = round(end_time - start_time, 1)

if algorithm_code == "GA":
    try: max_it
    except NameError: max_it = None
    try: pop_size
    except NameError: pop_size = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'pop_size' = " + str(pop_size) + "."

if algorithm_code == "AC":
    try: max_it
    except NameError: max_it = None
    try: num_ants
    except NameError: num_ants = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_ants' = " + str(num_ants) + "."

if algorithm_code == "PS":
    try: max_it
    except NameError: max_it = None
    try: num_parts
    except NameError: num_parts = None
    if added_note != "":
        added_note = added_note + "\n"
    added_note = added_note + "The parameter values are 'max_it' = " + str(max_it) + " and 'num_parts' = " + str(num_parts) + "."
    
added_note = added_note + "\nRUN-TIME = " + str(elapsed_time) + " seconds.\n"
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y-%H:%M:%S")
added_note = added_note + "DATE-TIME = " + dt_string + ".\n"

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")
len_user_name = len(my_user_name)
user_number = 0
for i in range(0, len_user_name):
    user_number = user_number + ord(my_user_name[i])
alg_number = ord(algorithm_code[0]) + ord(algorithm_code[1])
len_dt_string = len(dt_string)
date_time_number = 0
for i in range(0, len_dt_string):
    date_time_number = date_time_number + ord(dt_string[i])
tour_diff = abs(tour[0] - tour[num_cities - 1])
for i in range(0, num_cities - 1):
    tour_diff = tour_diff + abs(tour[i + 1] - tour[i])
certificate = user_number + alg_number + date_time_number + tour_diff
local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = {0} ({1} {2}),\n".format(my_user_name, my_first_name, my_last_name))
f.write("ALGORITHM CODE = {0}, NAME OF CITY-FILE = {1},\n".format(algorithm_code, input_file))
f.write("SIZE = {0}, TOUR LENGTH = {1},\n".format(num_cities, tour_length))
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write(",{0}".format(tour[i]))
f.write(",\nNOTE = {0}".format(added_note))
f.write("CERTIFICATE = {0}.\n".format(certificate))
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

############ END OF SECTOR 10 (IGNORE THIS COMMENT)
