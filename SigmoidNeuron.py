import numpy as np


class Sigmoid(object):

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.lr = 0.1

    def predict(self, p_input):
        p_sum = 0
        for i in range(len(p_input)):
            p_sum += p_input[i] * self.weights[i]
        sigma = 1.0 / (1.0 + np.exp(-p_sum))
        return sigma

    def train(self, inputt, answer):
        actual_output = self.predict(inputt)

        diff = answer - actual_output
        for j in range(len(self.weights)):
            self.weights[j] = self.weights[j] + (self.lr * inputt[j] * diff)
        self.bias = self.bias + (self.lr * diff)


weightsNAND = [-1, -1]
weightsOR = [1, 1]
weightAND = [1, 1]
input1 = [1, 1]
input2 = [1, 0]
input3 = [0, 1]
input4 = [0, 0]
AND = Sigmoid(weightAND, -1.0)
NAND = Sigmoid(weightsNAND, 1.5)
OR = Sigmoid(weightsOR, 0.0)

print(AND.predict(input1))
print(AND.predict(input2))
print(AND.predict(input3))
print(AND.predict(input4))

print("___________________")
print(NAND.predict(input1))
print(NAND.predict(input2))
print(NAND.predict(input3))
print(NAND.predict(input4))
print("___________________")
print(OR.predict(input1))
print(OR.predict(input2))
print(OR.predict(input3))
print(OR.predict(input4))
