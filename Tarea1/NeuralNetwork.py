import numpy as npy


class Neuron(object):

    def __init__(self, size):
        """
        Creates a new neuron
        :param size: size of the weights and inputs
        """
        self.size = size
        self.bias = npy.random.uniform(0, 1)
        self.weights = []
        for _ in range(0, self.size):
            self.weights.append(npy.random.uniform(0, 1))
        self.inputs = []  # storing inputs for later
        self.output = 0
        self.delta = 0

    def sum(self, inputs):
        """
        Sum the multiplication of each weight and the input given
        :param inputs: the input given
        :return:the sum between each weight and input
        """
        neu_sum = 0
        if len(inputs) == self.size:
            self.inputs = inputs
            for i in range(self.size):
                neu_sum += self.weights[i] * self.inputs[i]
        return neu_sum + self.bias

    def sigmoid(self, inputs):
        """
        Calculates the sigmoid function of the neuron.
        :return: the actual output of the neuron for a given input.
        """
        return 1 / (1 + npy.exp(-self.sum(inputs)))



class Layer(object):
    def __init__(self, neuron_size, layer_size):
        """
        Creates a new layer of neurons
        :param neuron_size: number of weights and inputs per neuron
        :param layer_size: number of neurons in the layer.
        """
        self.size = layer_size
        self.neurons = []
        for _ in range(0, self.size):
            self.neurons.append(Neuron(neuron_size))


class Network(object):
    def __init__(self, hidden_l_size, layers_size, input_size, output_size):
        """
        Creates a new network
        :param hidden_l_size: number of neurons in the hidden layers
        :param layers_size: number of layers
        :param input_size: number of inputs
        :param output_size: number of outputs
        """

        self.input_size = input_size
        self.hidden_l_size = hidden_l_size
        self.layers_size = layers_size
        self.output_size = output_size
        self.layers = []
        if self.layers_size > 1:  # More than one layer
            first_hidden_layer = Layer(self.input_size, self.hidden_l_size)  # First layer
            self.layers.append(first_hidden_layer)
            for _ in range(0, self.layers_size - 2):  # for every layer except first and output
                a_hidden_layer = Layer(self.hidden_l_size, self.hidden_l_size)
                self.layers.append(a_hidden_layer)
            output_layer = Layer(self.hidden_l_size, self.output_size)  # Last Layer
            self.layers.append(output_layer)
        else:  # Just one layer, as input and output
            self.layers = [Layer(self.input_size, self.output_size)]

    def forward_propagation(self, inputs):
        """
        Forward Propagation method viewed in class
        :param inputs: inputs for the network
        :return: the output for the given input
        """
        current_input = inputs
        for layer in self.layers:
            layer_output = []
            for neuron in layer.neurons:
                neuron.output = neuron.sigmoid(current_input)
                layer_output.append(neuron.output)
            current_input = layer_output  # on the last layer, current_input it the output of the NW
        return current_input

    def backward_propagation(self, desired_output):
        """
        Backward Propagation of errors method
        :param desired_output: expected output for the output layer
        :return:
        """
        for i in reversed(range(len(self.layers))):  # reading layers backwards
            errors = []
            current_layer = self.layers[i]
            if i == len(self.layers) - 1:  # if current_layer == the output layer
                for j in range(len(current_layer.neurons)):
                    current_neuron = current_layer.neurons[j]
                    error = desired_output[j] - current_neuron.output
                    errors.append(error)
            else:  # for every other layer
                for j in range(len(current_layer.neurons)):
                    previous_layer = self.layers[i + 1]
                    neuron_error = 0.0
                    for n in previous_layer.neurons:
                        neuron_error += n.weights[j] * n.delta
                    errors.append(neuron_error)
            for k in range(len(current_layer.neurons)):  # updating the deltas in every neuron of the layer
                n = current_layer.neurons[k]  # for every neuron in the layer
                n.delta = errors[k] * (n.output * (1.0 - n.output))  # error * transfer_derivative(output)

    def updating_values(self, inputs, rate):
        """
        updates weights an bias on the neurons of the network
        :param inputs: network input
        :param rate: network learning rate.
        :return:
        """
        current_input = inputs
        for i in range(len(self.layers)):  # reading layers forward
            current_layer = self.layers[i]
            if i != 0:  # if the layer readed isnt the first one
                current_input = []  # emptying current_input for next layer.
                for n in self.layers[i - 1].neurons:  # for every neuron in the previous layer
                    current_input.append(n.output)  # input for the current_layer
            for n in current_layer.neurons:
                for j in range(len(current_input)):
                    n.weights[j] += current_input[j] * n.delta * rate
                n.bias += rate * n.delta

    def training(self, epochs, rate, input_set, desired_output_set):
        """
        training the network
        :param epochs: number of epochs to train the network
        :param rate: learning rate
        :param input_set: set of inputs
        :param desired_output_set: set of disired output for the input_set.
                Its assumed that it has the same number of elements that input_set
        :return:
        """
        for e in range(epochs):
            sum_error = 0
            sum_error_sqr = 0
            i = 0
            for input in input_set:  # for every input
                actual_output = self.forward_propagation(input)  # predict an output set with the network
                for j in range(len(desired_output_set[i])):  # and for every desired output in the set
                    sum_error += npy.abs(desired_output_set[i][j] - actual_output[j])  # get mean absolute error
                    sum_error_sqr += (desired_output_set[i][j] - actual_output[j]) ** 2  # get mean sqr error
                    self.backward_propagation(desired_output_set[i])
                    self.updating_values(input, rate)
                i += 1
            print(
                '## epoch = %d, rate = %.3f, abs_error = %.3f, sqr_error = %.3f' % (e, rate, sum_error, sum_error_sqr))


inputs = [[0, 0], [0, 1], [1, 1], [1, 0]]
answers = [[0], [0], [1], [0]]
AND = Network(1, 1, 2, 1)
AND.forward_propagation(inputs[0])
AND.training(1000, 0.1, inputs, answers)
