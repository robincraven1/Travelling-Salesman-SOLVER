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

added_note = "Genetic Algorithm ENHANCED with elitism, 2-opt local search, and inversion mutation"

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
# ENHANCED IMPLEMENTATION (MEMETIC / HYBRID GA)
#
# This file builds upon the basic GA with four enhancements that improve
# solution quality without changing the core GA parameters (pop_size,
# max_it, mutation_rate, tournament_size).
#
# ENHANCEMENTS OVERVIEW:
# 1. ELITISM — Preserve the top 2 individuals unchanged across generations,
#    guaranteeing monotonic improvement of the best tour.
# 2. 2-OPT LOCAL SEARCH (MEMETIC GA) — Probabilistically apply local
#    optimisation to children, combining global search with local refinement.
# 3. INVERSION MUTATION — Add a second mutation operator (segment reversal)
#    alongside swap mutation, providing more diverse perturbations.
# 4. NEAREST NEIGHBOUR SEEDING — Initialise some individuals with the
#    greedy NN heuristic, giving the population good genetic material
#    from generation 1.
#
# Keeping the same core parameters as the basic version ensures a fair
# comparison: any improvement is due to the enhancements, not tuning.
############################################################################

# ========================== GA PARAMETERS ==========================
# These are IDENTICAL to the basic version for fair comparison.

# pop_size: Number of individuals in the population. 50 gives moderate
# diversity while keeping per-generation computation manageable.
pop_size = 50

# max_it: Maximum number of generations. The evolutionary loop runs for
# up to 500 generations (or until the 55-second time limit).
max_it = 500

# mutation_rate: Probability each child undergoes mutation. 0.1 balances
# exploration (introducing variation) with exploitation (preserving
# good structure from crossover).
mutation_rate = 0.1

# tournament_size: Number of individuals sampled per tournament selection.
# With size 5 out of 50, there is moderate selection pressure.
tournament_size = 5

# ========================== ENHANCEMENT PARAMETERS ==========================

# elite_count: Number of top individuals preserved unchanged each generation.
# With elite_count=2, the two best tours are guaranteed to survive, ensuring
# the best solution can never be lost through crossover or mutation.
elite_count = 2

# local_search_prob: Probability that a child undergoes 2-opt local search
# after crossover and mutation. Set to 0.1 to balance computational cost
# (local search is expensive) against benefit. Applying it to every child
# would be too slow; never applying it wastes the opportunity.
local_search_prob = 0.1

# local_search_iterations: Number of random 2-opt swap attempts during
# each local search invocation. 20 attempts is a light-touch optimisation
# that can fix obvious inefficiencies without spending too much time.
local_search_iterations = 20


def calculate_tour_length(a_tour):
    """
    Calculate the total distance of a complete tour (Hamiltonian cycle).

    Sums edge weights along the tour and closes the cycle back to start.
    Identical to the basic version.

    Parameters:
        a_tour (list[int]): A permutation of city indices 0..num_cities-1.

    Returns:
        int: Total tour distance.
    """
    total_length = 0
    n = len(a_tour)
    # Sum distances between consecutive cities
    for i in range(n - 1):
        total_length += dist_matrix[a_tour[i]][a_tour[i + 1]]
    # Close the cycle: last city back to first
    total_length += dist_matrix[a_tour[n - 1]][a_tour[0]]
    return total_length


def generate_random_tour():
    """
    Generate a random tour by shuffling city indices.

    Returns:
        list[int]: A random permutation of city indices.
    """
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour


# =====================================================================
# ENHANCEMENT 4: NEAREST NEIGHBOUR SEEDING
# =====================================================================
# Instead of initialising ALL individuals randomly (as the basic version
# does), we seed the population with a few tours constructed using the
# nearest neighbour heuristic. These high-quality starting solutions give
# the GA good "genetic material" from generation 1, which crossover can
# immediately begin combining and improving.
#
# The remaining individuals are still random, maintaining population
# diversity. Combined with elitism (Enhancement 1), these good NN tours
# are guaranteed not to be lost in early generations.
#
# Each NN tour starts from a DIFFERENT random city, providing structural
# diversity among the seeded individuals.
# =====================================================================

def generate_nearest_neighbor_tour():
    """
    Generate a tour using the nearest neighbour greedy heuristic.

    Algorithm:
        1. Choose a random starting city.
        2. From the current city, move to the nearest unvisited city.
        3. Repeat until all cities are visited.

    Time complexity: O(n^2).

    Returns:
        list[int]: A tour constructed by the nearest neighbour heuristic.
    """
    # Pick a random start city (different runs → different NN tours)
    start_city = random.randint(0, num_cities - 1)
    tour = [start_city]
    visited = {start_city}  # Set for O(1) membership checking

    current_city = start_city
    while len(tour) < num_cities:
        # Find the nearest unvisited city by scanning all candidates
        best_next = None
        best_distance = float('inf')
        for city in range(num_cities):
            if city not in visited:
                distance = dist_matrix[current_city][city]
                if distance < best_distance:
                    best_distance = distance
                    best_next = city
        # Move to the nearest unvisited city
        tour.append(best_next)
        visited.add(best_next)
        current_city = best_next

    return tour


def initialize_population():
    """
    Create the initial population with a mix of NN and random tours.

    ENHANCEMENT 4: The first few individuals are constructed using the
    nearest neighbour heuristic (each from a different random start city).
    The rest are random permutations.

    With pop_size=50, we seed min(5, 50//10) = 5 NN tours and 45 random
    tours. This provides:
    - Good initial solutions for crossover to build upon.
    - Sufficient diversity from the random tours to avoid premature
      convergence to a single NN-derived solution.

    Returns:
        list[list[int]]: A population of pop_size tours.
    """
    population = []

    # Seed the population with a few nearest neighbour tours
    # min(5, pop_size // 10) ensures we don't seed too many (max 10% of pop)
    num_nn_tours = min(5, pop_size // 10)
    for _ in range(num_nn_tours):
        individual = generate_nearest_neighbor_tour()
        population.append(individual)

    # Fill the remaining slots with random tours for diversity
    for _ in range(pop_size - num_nn_tours):
        individual = generate_random_tour()
        population.append(individual)

    return population


def calculate_fitness(individual):
    """
    Calculate fitness as the negative of tour length (shorter = higher fitness).

    Parameters:
        individual (list[int]): A tour.

    Returns:
        int: Fitness value (negative tour length).
    """
    tour_len = calculate_tour_length(individual)
    return -tour_len


def tournament_selection(population, fitnesses):
    """
    Select one parent using tournament selection.

    Randomly sample tournament_size individuals and return the fittest.
    Same logic as the basic version.

    Parameters:
        population (list[list[int]]): Current population.
        fitnesses (list[int]): Fitness values for each individual.

    Returns:
        list[int]: A copy of the winning individual.
    """
    tournament_indices = random.sample(range(len(population)), tournament_size)
    best_idx = tournament_indices[0]
    best_fitness = fitnesses[best_idx]
    for idx in tournament_indices[1:]:
        if fitnesses[idx] > best_fitness:
            best_fitness = fitnesses[idx]
            best_idx = idx
    return population[best_idx][:]


def order_crossover(parent1, parent2):
    """
    Perform Order Crossover (OX) to produce one child from two parents.

    This is the same proven OX operator used in the basic version:
        1. Copy a random segment from parent1 into the child.
        2. Fill remaining positions with cities from parent2 in order,
           skipping cities already present.

    OX is particularly well-suited for TSP because it preserves the
    relative ordering of cities from both parents while producing a
    valid permutation.

    Parameters:
        parent1 (list[int]): First parent tour.
        parent2 (list[int]): Second parent tour.

    Returns:
        list[int]: The child tour.
    """
    n = len(parent1)
    # Choose two crossover points (point1 < point2)
    point1 = random.randint(0, n - 2)
    point2 = random.randint(point1 + 1, n - 1)

    # Initialise child with placeholder values
    child = [-1] * n

    # Copy the segment from parent1 into the child
    for i in range(point1, point2 + 1):
        child[i] = parent1[i]

    # Track which cities are already in the child
    child_set = set(child[point1:point2 + 1])

    # Fill remaining positions from parent2, starting after point2 and wrapping
    current_pos = (point2 + 1) % n
    for i in range(n):
        city = parent2[(point2 + 1 + i) % n]
        if city not in child_set:
            child[current_pos] = city
            current_pos = (current_pos + 1) % n

    return child


def swap_mutation(individual):
    """
    Swap mutation: exchange the cities at two randomly chosen positions.

    Same as the basic version. Makes a small localised change.

    Parameters:
        individual (list[int]): The tour to mutate.

    Returns:
        list[int]: A new mutated tour.
    """
    n = len(individual)
    mutated = individual[:]
    pos1 = random.randint(0, n - 1)
    pos2 = random.randint(0, n - 1)
    while pos2 == pos1:
        pos2 = random.randint(0, n - 1)
    mutated[pos1], mutated[pos2] = mutated[pos2], mutated[pos1]
    return mutated


# =====================================================================
# ENHANCEMENT 3: INVERSION MUTATION
# =====================================================================
# The basic version uses only swap mutation. Inversion mutation provides
# a complementary operator that makes larger, more structured changes.
#
# Inversion mutation reverses a segment of the tour, which is equivalent
# to a 2-opt move. This is more natural for TSP because:
# - It preserves adjacency relationships WITHIN the reversed segment
#   (the same cities remain adjacent, just in reverse order).
# - Only the two EDGES at the segment endpoints change.
# - This targeted disruption is more likely to be beneficial than swap
#   mutation, which breaks up to 4 edges.
#
# Using BOTH mutation types provides diversity in the types of
# perturbations applied to the population.
# =====================================================================

def inversion_mutation(individual):
    """
    ENHANCEMENT 3: Inversion mutation — reverse a random segment.

    Algorithm:
        1. Choose two random positions pos1 < pos2.
        2. Reverse the sub-sequence individual[pos1..pos2].

    This is structurally equivalent to a 2-opt move. It changes only the
    two edges at the endpoints of the reversed segment while preserving
    all adjacency relationships within the segment.

    Example:
        Before: [A, B, C, D, E, F], pos1=1, pos2=4
        After:  [A, E, D, C, B, F]
        Only edges (A,B)→(A,E) and (E,F)→(B,F) changed.

    Parameters:
        individual (list[int]): The tour to mutate.

    Returns:
        list[int]: A new mutated tour with one segment reversed.
    """
    n = len(individual)
    mutated = individual[:]
    # Choose two positions: pos1 < pos2
    pos1 = random.randint(0, n - 2)
    pos2 = random.randint(pos1 + 1, n - 1)
    # Reverse the segment between pos1 and pos2 (inclusive)
    mutated[pos1:pos2 + 1] = reversed(mutated[pos1:pos2 + 1])
    return mutated


def mutate(individual):
    """
    ENHANCEMENT 3: Mixed mutation strategy.

    With probability 0.5, apply swap mutation.
    With probability 0.5, apply inversion mutation.

    This provides a balance between:
    - Small random perturbations (swap) — fine-grained diversity.
    - Larger structural rearrangements (inversion) — can fix suboptimal
      segment orderings that swap mutation cannot address.

    Parameters:
        individual (list[int]): The tour to mutate.

    Returns:
        list[int]: The mutated tour.
    """
    if random.random() < 0.5:
        return swap_mutation(individual)       # Small perturbation
    else:
        return inversion_mutation(individual)  # Structural rearrangement


# =====================================================================
# ENHANCEMENT 2: 2-OPT LOCAL SEARCH (MEMETIC / HYBRID GA)
# =====================================================================
# Standard GAs rely entirely on crossover and mutation to improve tours.
# These global operators are good at combining "building blocks" from
# different parents but poor at fine-tuning a nearly-optimal tour.
#
# By adding a 2-opt local search phase, we transform the GA into a
# MEMETIC ALGORITHM (also called a hybrid GA). The idea is:
# - GLOBAL operators (crossover, mutation) handle broad exploration
#   of the solution space.
# - LOCAL search (2-opt) handles fine-grained refinement of promising
#   individuals.
#
# The local search is applied probabilistically (with probability
# local_search_prob = 0.1) to balance its computational cost against
# its benefit. Only improving 2-opt swaps are accepted (steepest
# ascent within the limited attempts).
# =====================================================================

def two_opt_improvement(tour):
    """
    ENHANCEMENT 2: Apply limited 2-opt local search to improve a tour.

    Algorithm:
        1. For each of local_search_iterations attempts:
            a. Pick two random positions i and j (where j >= i+2).
            b. Reverse the segment tour[i+1..j] (a 2-opt swap).
            c. Calculate the new tour length.
            d. If the new tour is shorter, KEEP the swap.
            e. Otherwise, DISCARD the swap (revert to the original).

    This is a "stochastic 2-opt" approach: instead of exhaustively trying
    all O(n^2) possible swaps (which would be too slow), we try a fixed
    number of random swaps and keep any that help.

    Only IMPROVING swaps are kept — the tour never worsens. This is pure
    local search / hill-climbing, complementing the GA's global search.

    Parameters:
        tour (list[int]): The tour to improve.

    Returns:
        list[int]: The improved tour (or the original if no improvement found).
    """
    n = len(tour)
    # 2-opt needs at least 4 cities to have two non-adjacent edges to swap
    if n < 4:
        return tour
    improved_tour = tour[:]
    current_length = calculate_tour_length(improved_tour)

    for _ in range(local_search_iterations):
        # Choose two random positions for the 2-opt swap
        # i must be at most n-3 so that j can be at least i+2
        # (we need the segments to be non-adjacent for a meaningful swap)
        i = random.randint(0, n - 3)
        j = random.randint(i + 2, n - 1)

        # Perform the 2-opt swap: reverse segment [i+1 .. j]
        new_tour = improved_tour[:]
        new_tour[i + 1:j + 1] = reversed(new_tour[i + 1:j + 1])
        new_length = calculate_tour_length(new_tour)

        # Accept the swap ONLY if it improves the tour (greedy / hill-climbing)
        if new_length < current_length:
            improved_tour = new_tour
            current_length = new_length

    return improved_tour


# =====================================================================
# ENHANCED GENETIC ALGORITHM MAIN FUNCTION
# =====================================================================

def genetic_algorithm_enhanced():
    """
    Enhanced Genetic Algorithm for TSP (Memetic / Hybrid GA).

    The core GA structure is the same as the basic version (selection,
    crossover, mutation, replacement), but with four enhancements:

    Enhancement 1 — Elitism:
        Before generating children, sort the population by fitness and
        copy the top elite_count individuals directly into the next
        generation. This guarantees that the best solution can only stay
        the same or improve across generations — it can never be lost.

    Enhancement 2 — 2-Opt Local Search:
        After crossover and mutation, each child has a local_search_prob
        chance of undergoing 2-opt local search. This refines promising
        individuals, combining global GA search with local optimisation.

    Enhancement 3 — Inversion Mutation:
        Instead of always using swap mutation, the mutate() function
        randomly chooses between swap and inversion mutation, providing
        more diverse types of perturbations.

    Enhancement 4 — Nearest Neighbour Seeding:
        The initial population includes some NN-constructed tours alongside
        random ones, giving the GA high-quality genetic material from the
        start. Combined with elitism, these good solutions are preserved.

    Returns:
        tuple: (best_tour, best_length) — the shortest tour found.
    """
    # ---- Initialise population (ENHANCEMENT 4: includes NN seeds) ----
    population = initialize_population()

    # ---- Evaluate fitness of every individual ----
    fitnesses = [calculate_fitness(ind) for ind in population]

    # ---- Record the best individual seen so far ----
    best_idx = fitnesses.index(max(fitnesses))
    best_tour = population[best_idx][:]
    best_length = calculate_tour_length(best_tour)

    # ---- Main evolutionary loop ----
    for iteration in range(max_it):
        # Check the 55-second time limit
        if (time.time() - start_time) >= 55:
            break

        # ---- ENHANCEMENT 1: ELITISM ----
        # Sort the population by fitness (descending) and preserve the
        # top elite_count individuals unchanged in the next generation.
        # This ensures the best tours are never lost.
        sorted_indices = sorted(range(len(population)), key=lambda k: fitnesses[k], reverse=True)
        elite = [population[sorted_indices[i]][:] for i in range(elite_count)]

        # Start the new population with the elite individuals
        new_population = []
        for ind in elite:
            new_population.append(ind)

        # ---- Generate remaining children to fill the population ----
        # Only need (pop_size - elite_count) children since elites are preserved
        while len(new_population) < pop_size:
            # Select two parents via tournament selection
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)

            # Create child via Order Crossover (OX)
            child = order_crossover(parent1, parent2)

            # ENHANCEMENT 3: Mutate using mixed strategy (swap OR inversion)
            if random.random() < mutation_rate:
                child = mutate(child)  # Randomly applies swap or inversion

            # ENHANCEMENT 2: Apply 2-opt local search with probability 0.1
            # This turns the GA into a memetic algorithm: crossover and mutation
            # handle global exploration, while 2-opt handles local refinement.
            if random.random() < local_search_prob:
                child = two_opt_improvement(child)

            new_population.append(child)

        # ---- Replace old population and evaluate new fitness ----
        population = new_population
        fitnesses = [calculate_fitness(ind) for ind in population]

        # ---- Update global best if we found a shorter tour ----
        current_best_idx = fitnesses.index(max(fitnesses))
        current_best_length = calculate_tour_length(population[current_best_idx])
        if current_best_length < best_length:
            best_tour = population[current_best_idx][:]
            best_length = current_best_length

    # Return the best tour found across all generations
    return best_tour, best_length


# ========================== RUN THE ALGORITHM ==========================
# Execute the enhanced GA and store results in the reserved variables
# 'tour' and 'tour_length' expected by the template code.
tour, tour_length = genetic_algorithm_enhanced()

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
