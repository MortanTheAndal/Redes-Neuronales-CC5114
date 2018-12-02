import unittest
from Tarea1.NeuralNetwork import Neuron, Network


class MyTestCase(unittest.TestCase):

    def test_neuron(self):
        neuron = Neuron(3)
        self.assertEqual(neuron.size, 3)
        self.assertEqual(neuron.delta, 0)
        self.assertEqual(len(neuron.weights), 3)
        self.assertEqual(len(neuron.inputs), 0)

    def test_CASE1(self):
        nw = Network(1, 2, 2, 1)
        nw.layers[0].neurons[0].bias = 0.5
        nw.layers[1].neurons[0].bias = 0.4

        nw.layers[0].neurons[0].weights = [0.4, 0.3]
        nw.layers[1].neurons[0].weights = [0.3]

        nw.training(1, 0.5, [[1, 1]], [[1]])

        self.assertEqual(nw.layers[0].neurons[0].bias, 0.502101508999489)
        self.assertEqual(nw.layers[0].neurons[0].weights, [0.40210150899948904, 0.302101508999489])
        self.assertEqual(nw.layers[1].neurons[0].bias, 0.43937745312797394)
        self.assertEqual(nw.layers[1].neurons[0].weights, [0.33026254863991883])

    def test_CASE2(self):
        nw = Network(2, 2, 2, 2)

        nw.layers[0].neurons[0].bias = 0.5
        nw.layers[0].neurons[1].bias = 0.4
        nw.layers[1].neurons[0].bias = 0.3
        nw.layers[1].neurons[1].bias = 0.6

        nw.layers[0].neurons[0].weights = [0.7, 0.3]
        nw.layers[0].neurons[1].weights = [0.3, 0.7]
        nw.layers[1].neurons[0].weights = [0.2, 0.3]
        nw.layers[1].neurons[1].weights = [0.4, 0.2]

        nw.training(2, 0.5, [[1, 1]], [[1, 1]])

        self.assertEqual(nw.layers[0].neurons[0].bias, 0.51043411869531352)
        self.assertEqual(nw.layers[0].neurons[0].weights, [0.7025104485493278, 0.3025104485493278])
        self.assertEqual(nw.layers[0].neurons[1].bias, 0.4249801135748337)
        self.assertEqual(nw.layers[0].neurons[1].weights, [0.3024981135748333, 0.724980113574834])

        self.assertEqual(nw.layers[1].neurons[0].bias, 0.3366294522515899)
        self.assertEqual(nw.layers[1].neurons[0].weights, [0.22994737881955657, 0.32938362863950127])
        self.assertEqual(nw.layers[1].neurons[1].bias, 0.6237654881509048)
        self.assertEqual(nw.layers[1].neurons[1].weights, [0.41943005652646226, 0.21906429169838573])

    def test_and(self):
        """
        Tests the and gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[0], [0], [1], [0]]
        AND = Network(1, 1, 2, 1)
        AND.training(50000, 0.1, inputs, answers)
        self.assertEqual(AND.forward_propagation(inputs[0])[0] < 0.1, True)
        self.assertEqual(AND.forward_propagation(inputs[1])[0] < 0.1, True)
        self.assertEqual(1.0 - AND.forward_propagation(inputs[2])[0] < 0.1, True)
        self.assertEqual(AND.forward_propagation(inputs[3])[0] < 0.1, True)

    def test_or(self):
        """
        Tests the or gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[0], [1], [1], [1]]
        OR = Network(1, 1, 2, 1)
        OR.training(50000, 0.1, inputs, answers)
        self.assertEqual(OR.forward_propagation(inputs[0])[0] < 0.1, True)
        self.assertEqual(1.0 - OR.forward_propagation(inputs[1])[0] < 0.1, True)
        self.assertEqual(1.0 - OR.forward_propagation(inputs[2])[0] < 0.1, True)
        self.assertEqual(1.0 - OR.forward_propagation(inputs[3])[0] < 0.1, True)

    def test_nand(self):
        """
        Tests the nand gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[1], [0], [0], [0]]
        NAND = Network(1, 1, 2, 1)
        NAND.training(50000, 0.1, inputs, answers)
        self.assertEqual(1.0 - NAND.forward_propagation(inputs[0])[0] < 0.1, True)
        self.assertEqual(NAND.forward_propagation(inputs[1])[0] < 0.1, True)
        self.assertEqual(NAND.forward_propagation(inputs[2])[0] < 0.1, True)
        self.assertEqual(NAND.forward_propagation(inputs[3])[0] < 0.1, True)

    def test_xor(self):
        """
        Tests the xor gate on an Neural Network
        :return:
        """
        inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
        answers = [[0], [1], [0], [1]]
        XOR = Network(3, 3, 2, 1)
        XOR.training(50000, 0.1, inputs, answers)
        self.assertEqual(XOR.forward_propagation(inputs[0])[0] < 0.1, True)
        self.assertEqual(1.0 - XOR.forward_propagation(inputs[1])[0] < 0.1, True)
        self.assertEqual(XOR.forward_propagation(inputs[2])[0] < 0.1, True)
        self.assertEqual(1.0 - XOR.forward_propagation(inputs[3])[0] < 0.1, True)


if __name__ == '__main__':
    unittest.main()
