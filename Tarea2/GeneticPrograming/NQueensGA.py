from GeneticAlgorithm import select_fittest
import numpy as np
import time
import random

"""
In GeneticAlgorithm.py is implemented a functional but simple genetic algorithm.
Its extendible for every problem with a string approach.
this aint the case.
In this file we are going to try to solve the N_queens Problem using an array approach.
"""


class Board(object):
    def __init__(self, size):
        self.board = []
        for i in range(0, size):
            self.board.append(random.randint(0, size - 1))
        self.fitness = -1

    def __str__(self):
        return "BOARD: " + str(self.board) + "\t Fitness: " + str(self.fitness)


def generate_population(population, ind_size):
    pop = []
    while len(pop) < population:
        board = Board(ind_size)
        pop.append(board)
    return pop


def n_queen_fitness_function(pop):
    for bo in pop:
        collision = 0
        for i in range(len(bo.board)):
            for j in range(i, len(bo.board)):
                if i != j and bo.board[i] == bo.board[j]:
                    collision += 1
                if i != j and np.absolute(bo.board[i] - bo.board[j]) == np.absolute(i - j):
                    collision += 1
        bo.fitness = collision
    return pop


def crossover(pop, population, board_size):
    children = []
    for _ in range(0, int((population - len(pop)) / 2)):
        p1 = random.choice(pop)
        p2 = random.choice(pop)

        c1 = Board(board_size)
        c2 = Board(board_size)

        split = random.randint(0, board_size - 1)

        c1.genes = p1.board[0:split].extend(p2.board[split:board_size])
        c2.genes = p2.board[0:split].extend(p1.board[split:board_size])
        children.append(c1)
        children.append(c2)
    pop.extend(children)
    return pop


def mutate(pop, board_size, mutation_rate):
    for ind in pop:
        for index, param in enumerate(ind.board):
            if random.uniform(0.0, 1.0) <= mutation_rate:
                ind.board[index] = random.randint(0, board_size - 1)
    return pop


def get_pop_avg(pop):
    sum = 0
    for ind in pop:
        sum += ind.fitness
    return float(sum / len(pop))


def NQ_ga(population, generations, board_size, mutation_rate):
    pop = generate_population(population, board_size)
    start = time.monotonic()
    generation_avgs = []
    for gen in range(generations):
        print("GENERATION: " + str(gen))
        pop = n_queen_fitness_function(pop)
        generation_avgs.append(get_pop_avg(pop))
        pop = select_fittest(pop, False)
        pop = crossover(pop, population, board_size)
        pop = mutate(pop, board_size, mutation_rate)

        if any(ind.fitness == 0 for ind in pop):
            print("SOLUTION FOUND !!!!")
            end = time.monotonic()
            print("Total Time : " + str((end - start)) + "\t At Generation N°: " + str(gen))
            return (end - start), generation_avgs
    end = time.monotonic()
    return (end - start), generation_avgs

