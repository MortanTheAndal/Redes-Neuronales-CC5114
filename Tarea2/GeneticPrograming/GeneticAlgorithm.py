import random
import time


class Individual(object):
    """
    class for a individual from the population.
    """

    def __init__(self, size, gene_pool):
        """

        :param size: number of genes that has the individual
        """
        self.genes = ''.join(random.choice(gene_pool) for _ in range(size))
        self.fitness = -1

    def __str__(self):
        """

        :return: string for an individual.
        """
        return "String:" + self.genes + "\t" + "Fitness:" + str(self.fitness)


def generate_first_population(pop_size, individual_size, gene_pool):
    """
    createst a population of individuals
    :param pop_size: that the population should have.
    :param individual_size: size of genes that each member of the population should have.
    :return: a list with individuals.
    """
    pop = []
    while len(pop) < pop_size:
        new_individual = Individual(individual_size, gene_pool)
        pop.append(new_individual)
    return pop


def get_fitness(guess, target):
    """
    calculates fitness for a individual based on a comparison with a target
    :param guess: an individual from the population
    :param target: the secret word
    :return:number of characters that are different between guess and target
    """
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)


def fit_test(target, pop, fitness_func):
    """
    calculates fitness for every individual of a population
    :param target: the secret word
    :param pop: the population
    :param fitness_func: fitness function, for it may depend on each example
    :return: the population whit the fitness calculated.
    """
    for individual in pop:
        individual.fitness = fitness_func(individual.genes, target)
    return pop


def select_fittest(pop, rev):
    """
    first sort by fitness, then discarding the weakest
    :param pop: population
    :param rev: boolean, reverse order of the sort.
    :return: the fittest individuals for mating and mutating
    """
    pop = sorted(pop, key=lambda ind: ind.fitness, reverse=rev)
    for indiv in pop:
        print(str(indiv))
    pop = pop[:int(0.25 * len(pop))]
    return pop


def crossover(pop, population, len_target, gene_pool):
    """
    selects 2 parents from the fit population, and creates two new individuals
    :param pop: the population
    :param population: size of the population
    :param len_target: length of the target word
    :param gene_pool: set of possible genes
    :return: a population with the fittest and their children
    """
    children = []
    for _ in range(0, int((population - len(pop)) / 2)):
        p1 = random.choice(pop)
        p2 = random.choice(pop)

        c1 = Individual(len_target, gene_pool)
        c2 = Individual(len_target, gene_pool)

        split = random.randint(0, len_target)

        c1.genes = p1.genes[0:split] + p2.genes[split:len_target]
        c2.genes = p2.genes[0:split] + p1.genes[split:len_target]
        children.append(c1)
        children.append(c2)
    pop.extend(children)
    return pop


def mutate(pop, mutation_rate, target_len, gene_pool):
    """
    randomly mutates genes
    :param pop:population
    :param mutation_rate: mutation factor
    :param target_len: the length of the target
    :param gene_pool: set of possible genes
    :return:
    """
    for ind in pop:
        for index, param in enumerate(ind.genes):
            if random.uniform(0.0, 1.0) <= mutation_rate:
                ind.genes = ind.genes[0:index] + random.choice(gene_pool) + ind.genes[index + 1:target_len]
    return pop


def get_gen_avg(pop):
    """
    calculates the avg fitness 4 a population
    :param pop: a population
    :return: an average fitness float
    """
    sum = 0
    for ind in pop:
        sum += ind.fitness
    return float(sum / len(pop))


def genetic_algorithm(population, generations, gene_pool, target, len_target, mutation_rate):
    """

    :param population: size of population
    :param generations: number of generations
    :param gene_pool: set of genes
    :param target: secret word
    :param len_target: size of the secret word
    :param mutation_rate: mutation threshold
    :return: a tuple of the time taken, and the list
    """
    pop = generate_first_population(population, len_target, gene_pool)
    start = time.monotonic()
    gen_avg = []
    for gen in range(0, generations):
        print("GENERATION: " + str(gen))
        pop = fit_test(target, pop, get_fitness)
        gen_avg.append(get_gen_avg(pop))
        pop = select_fittest(pop, True)
        pop = crossover(pop, population, len_target, gene_pool)
        pop = mutate(pop, mutation_rate, len_target, gene_pool)

        if any(ind.fitness >= len_target for ind in pop):
            print("SOLUTION FOUND !!!!")
            end = time.monotonic()
            print("Total Time : " + str((end - start)) + "\t At Generation N°: " + str(gen))
            return (end - start), gen_avg
    end = time.monotonic()
    return (end - start), gen_avg
