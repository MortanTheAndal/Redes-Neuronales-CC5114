import unittest
from Tarea1.Perceptron import Perceptron


class MyTestCase(unittest.TestCase):
    input1 = [1, 1]
    input2 = [1, 0]
    input3 = [0, 1]
    input4 = [0, 0]

    def test_nand(self):
        weights_nand = [-1.0, -1.0]
        nand = Perceptron(weights_nand, 0.5)
        self.assertEqual(nand.resolve([1, 1]), 0)
        self.assertEqual(nand.resolve([1, 0]), 0)
        self.assertEqual(nand.resolve([0, 0]), 1)
        self.assertEqual(nand.resolve([0, 1]), 0)

    def test_and(self):
        weight_and = [1, 1]
        AND = Perceptron(weight_and, -1)
        self.assertEqual(AND.resolve([1, 1]), 1)
        self.assertEqual(AND.resolve([1, 0]), 0)
        self.assertEqual(AND.resolve([0, 0]), 0)
        self.assertEqual(AND.resolve([0, 1]), 0)

    def test_or(self):
        weights_or = [1, 1]
        OR = Perceptron(weights_or, 0)
        self.assertEqual(OR.resolve([1, 1]), 1)
        self.assertEqual(OR.resolve([1, 0]), 1)
        self.assertEqual(OR.resolve([0, 0]), 0)
        self.assertEqual(OR.resolve([0, 1]), 1)


if __name__ == '__main__':
    unittest.main()
