import random
from typing import List, Callable, Tuple
from constant import food_dict, meals_percent

Genome = List[int]
Population = List[Genome]
PopulateFunc = Callable[[], Population]
FitnessFunc = Callable[[Genome, List[int], List[int], float, float, float, float], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome, List[int]], Genome]


def scoreCalo(value: float, expect: float) -> int:
    if(value>=(0.97*expect) and value<=(1.03*expect)):
        return 4
    if(value>=(0.95*expect) and value<(0.97*expect)):
        return 2
    if(value>(1.03*expect) and value<=(1.05*expect)):
        return 2
    return 0

 
def score(value: float, expect: float) -> int:
    if(value>=(0.97*expect) and value<=(1.03*expect)):
        return 2
    if(value>=(0.95*expect) and value<(0.97*expect)):
        return 1
    if(value>(1.03*expect) and value<=(1.05*expect)):
        return 1
    return 0


def generate_genome(meals_foods: List[int]) -> Genome:
    return [random.randint(food_dict[x][3],food_dict[x][4]) for x in meals_foods]


def generate_population(size: int, meals_foods: List[int]) -> Population:
    return [generate_genome(meals_foods) for _ in range(size)]


def evaluate(
    individual: Genome, 
    meal_foods: List[int],
    food_per_meal: List[int], 
    expect_calo: float, 
    expect_prot: float, 
    expect_carb: float, 
    expect_fat: float) -> int:

    tot_calo = sum(x*food_dict[y][5] for x,y in zip(individual,meal_foods))
    tot_prot = sum(x*food_dict[y][6] for x,y in zip(individual,meal_foods))
    tot_carb = sum(x*food_dict[y][7] for x,y in zip(individual,meal_foods))
    tot_fat = sum(x*food_dict[y][8] for x,y in zip(individual,meal_foods))
    
    point =  scoreCalo(tot_calo, expect_calo) + score(tot_prot, expect_prot) + score(tot_carb, expect_carb) + score(tot_fat, expect_fat)

    index = 0
    count=0
    for i in food_per_meal:
        meal_calo = 0
        ex_meal_calo = meals_percent[count] * tot_calo
        for _ in range(i):
            key_food = meal_foods[index]
            meal_calo += individual[index] * food_dict[key_food][5]
            index += 1
        point += score(meal_calo, ex_meal_calo)
        count += 1
        
    return point


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")

    length = len(a)
    if length < 2:
        return a, b

    p = random.randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]


def mutation(
    genome: Genome, 
    meals_foods: List[int], 
    num: int = 1, 
    probability: float = 0.5) -> Genome:

    for _ in range(num):
        index = random.randrange(len(genome))
        key_food=meals_foods[index]
        if random.random() > probability:
            genome[index] = genome[index]
        else:
            temp= random.randint(food_dict[key_food][3],food_dict[key_food][4])
            while genome[index] == temp:
                temp = random.randint(food_dict[key_food][3],food_dict[key_food][4])
            genome[index]=temp
    return genome



def selection_pair(
    population: Population, 
    fitness_func: FitnessFunc, 
    meal_foods: List[int],
    food_per_meal: List[int],
    expect_calo: float, 
    expect_prot: float, 
    expect_carb: float, 
    expect_fat: float) -> Population:
    return random.choices(
        population=population,
        weights=[fitness_func(gene, meal_foods, food_per_meal, expect_calo, expect_prot, expect_carb, expect_fat) for gene in population],
        k=2
    )


def sort_population(population: Population, fitness_func: FitnessFunc) -> Population:
    return sorted(population, key=fitness_func, reverse=True)


def run_evolution(
        exp_calo: float,
        macro: List[float],
        meals_foods:List[int],
        food_per_meal: List[int],
        populate_func: PopulateFunc = generate_population,
        fitness_func: FitnessFunc = evaluate,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        fitness_score: int = 20,
        generation_limit: int = 5000
        ) \
        -> Tuple[Population, int]:

    exp_prot = (macro[0]*exp_calo)/4
    exp_carb = (macro[1]*exp_calo)/4
    exp_fat = (macro[2]*exp_calo)/9

    population = populate_func(20, meals_foods)
    
    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome,meals_foods,food_per_meal, exp_calo, exp_prot, exp_carb, exp_fat), reverse=True)

        if fitness_func(population[0],meals_foods,food_per_meal, exp_calo, exp_prot, exp_carb, exp_fat) == fitness_score:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func, meals_foods, food_per_meal, exp_calo, exp_prot, exp_carb, exp_fat)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a, meals_foods)
            offspring_b = mutation_func(offspring_b, meals_foods)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    return population, i

