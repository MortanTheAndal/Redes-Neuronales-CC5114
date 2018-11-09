import unittest
from NeuralNetwork import Neuron, Layer, Network


class MyTestCase(unittest.TestCase):

    def test_neuron(self):
        neuron = Neuron(3)
        self.assertEqual(neuron.size, 3)
        self.assertEqual(neuron.delta, 0)
        self.assertEqual(len(neuron.weights), 3)
        self.assertEqual(len(neuron.inputs), 0)

    def test_and(self):
        """
        Tests the and gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[0], [0], [1], [0]]
        AND = Network(1, 1, 2, 1)
        AND.training(50000, 0.1, inputs, answers)
        self.assertEqual(AND.forward_propagation(inputs[0])[0] < 0.5, True)
        self.assertEqual(AND.forward_propagation(inputs[1])[0] < 0.5, True)
        self.assertEqual(AND.forward_propagation(inputs[2])[0] > 0.5, True)
        self.assertEqual(AND.forward_propagation(inputs[3])[0] < 0.5, True)

    def test_or(self):
        """
        Tests the or gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[0], [1], [1], [1]]
        OR = Network(1, 1, 2, 1)
        OR.training(50000, 0.1, inputs, answers)
        self.assertEqual(OR.forward_propagation(inputs[0])[0] < 0.5, True)
        self.assertEqual(OR.forward_propagation(inputs[1])[0] > 0.5, True)
        self.assertEqual(OR.forward_propagation(inputs[2])[0] > 0.5, True)
        self.assertEqual(OR.forward_propagation(inputs[3])[0] > 0.5, True)

    def test_nand(self):
        """
        Tests the nand gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[1], [0], [0], [0]]
        NAND = Network(1, 1, 2, 1)
        NAND.training(50000, 0.1, inputs, answers)
        self.assertEqual(NAND.forward_propagation(inputs[0])[0] > 0.5, True)
        self.assertEqual(NAND.forward_propagation(inputs[1])[0] < 0.5, True)
        self.assertEqual(NAND.forward_propagation(inputs[2])[0] < 0.5, True)
        self.assertEqual(NAND.forward_propagation(inputs[3])[0] < 0.5, True)

    def test_XOR(self):
        """
        Tests the xor gate on an Neural Network
        :return:
        """
        inputs = [[0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]
        answers = [[0], [1], [0], [1]]
        XOR = Network(3, 2, 3, 1)
        XOR.training(300000, 0.5, inputs, answers)
        self.assertEqual(XOR.forward_propagation(inputs[0])[0] < 0.5, True)
        self.assertEqual(XOR.forward_propagation(inputs[1])[0] > 0.5, True)
        self.assertEqual(XOR.forward_propagation(inputs[2])[0] > 0.5, True)
        self.assertEqual(XOR.forward_propagation(inputs[3])[0] < 0.5, True)


if __name__ == '__main__':
    unittest.main()
