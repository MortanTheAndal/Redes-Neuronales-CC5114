from GeneticAlgorithm import *
from NQueensGA import *
import matplotlib.pyplot as plt

target_string = "Mortan The Andal"  ## '0100010101000101010010101010' ##
target_string_len = len(target_string)
no_individuals = 50
no_generation = 1000
pool = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  ##'01'  ##
mut_rate = 0.1
str1 = genetic_algorithm(no_individuals, no_generation, pool, target_string, target_string_len, mut_rate)

plt.plot(str1[1], 'r--')
plt.title("Cadena : 'Mortan The Andal'  Tiempo: " + str(str1[0]))
plt.xlabel("Generaciones")
plt.ylabel("Promedio de Fitness")
plt.show()

target_string = '0100010101000101010010101010'
target_string_len = len(target_string)
no_individuals = 50
no_generation = 1000
pool = '01'
mut_rate = 0.1
str2 = genetic_algorithm(no_individuals, no_generation, pool, target_string, target_string_len, mut_rate)

plt.plot(str2[1], 'b*')
plt.title("Cadena : '0100010101000101010010101010'  Tiempo: " + str(str1[0]))
plt.xlabel("Generaciones")
plt.ylabel("Promedio de Fitness")
plt.show()

b_z = 4
pop_size = 20
no_generations = 10000
mut_rate = 0.2
nq1 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

b_z = 6
pop_size = 20
no_generations = 10000
mut_rate = 0.2
nq2 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

b_z = 8
pop_size = 20
no_generations = 10000
mut_rate = 0.2
nq3 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

b_z = 10
pop_size = 20
no_generations = 10000
mut_rate = 0.2
nq4 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

plt.plot(nq1[1], 'b*', label='N = 4')
plt.plot(nq2[1], 'r--', label='N = 6')
plt.plot(nq3[1], 'g^', label='N = 8')
plt.plot(nq4[1], 'c*', label='N = 10')
plt.title("N-Queens  Tiempo: " + str(nq1[0] + nq2[0] + nq3[0] + nq4[0]))
plt.xlabel("Generaciones")
plt.ylabel("Promedio de Fitness")
plt.legend()
plt.show()

b_z = 8
pop_size = 20
no_generations = 10000
mut_rate = 0.2
nq1 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

b_z = 8
pop_size = 30
no_generations = 10000
mut_rate = 0.2
nq2 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

b_z = 8
pop_size = 40
no_generations = 10000
mut_rate = 0.2
nq3 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

b_z = 8
pop_size = 50
no_generations = 10000
mut_rate = 0.2
nq4 = NQ_ga(pop_size, no_generations, b_z, mut_rate)

plt.plot(nq1[1], 'b*', label='cant. población = 20')
plt.plot(nq2[1], 'r--', label='cant. población = 30')
plt.plot(nq3[1], 'g^', label='cant. población = 40')
plt.plot(nq4[1], 'c*', label='cant. población = 50')
plt.title("N-Queens  Tiempo: " + str(nq1[0] + nq2[0] + nq3[0] + nq4[0]))
plt.xlabel("Generaciones")
plt.ylabel("Promedio de Fitness")
plt.legend()
plt.show()
