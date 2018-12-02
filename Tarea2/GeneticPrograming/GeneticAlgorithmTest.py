import unittest
from string import *
import GeneticAlgorithm as ga


class MyTestCase(unittest.TestCase):
    def test_pop_creation_char(self):
        genes = printable  # every character possible including /n and /t and that kind of stuff
        pop = ga.generate_first_population(10, 5, genes)
        self.assertEqual(len(pop), 10)
        for ind in pop:
            self.assertEqual(len(ind), 5)

    def test_pop_creation_bin(self):
        genes = '01'
        pop = ga.generate_first_population(10, 7, genes)
        self.assertEqual(len(pop), 10)
        for ind in pop:
            self.assertEqual(len(ind), 7)

    def test_get_fitness(self):
        target = '011001100'
        self.assertEqual(ga.get_fitness('010101010)', target), 5)



if __name__ == '__main__':
    unittest.main()
