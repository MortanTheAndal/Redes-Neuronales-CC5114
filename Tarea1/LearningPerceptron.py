from Tarea1.Perceptron import Perceptron
import random as rd


class LearningPerceptron(Perceptron):

    def __init__(self, weights, bia):
        Perceptron.__init__(self, weights, bia)
        self.lr = 0.05

    def training(self, inputt, answer):
        actual_output = self.resolve(inputt)

        diff = answer - actual_output
        for j in range(len(self.weights)):
            self.weights[j] = self.weights[j] + (self.lr * inputt[j] * diff)
        self.bias = self.bias + (self.lr * diff)


def input_ans_generator(ans_size):
    inputs = list()
    ans_vector = list()
    for k in range(ans_size):
        in_vector = [rd.uniform(-50, 50), rd.uniform(-50, 50)]
        if in_vector[0] > in_vector[1]:
            ans_vector.append(0)
        else:
            ans_vector.append(1)
        inputs.append(in_vector)
    return [inputs, ans_vector]


lp = LearningPerceptron([rd.uniform(-2.0, 2.0), rd.uniform(-2.0, 2.0)], rd.uniform(-2.0, 2.0))

trainings = 0
size = 100
while True:
    g = 0
    new_generated = input_ans_generator(size)
    for l in range(size):
        real_output = lp.resolve(new_generated[0][l])
        expected = new_generated[1][l]
        if real_output != expected:
            lp.training(new_generated[0][l], expected)
        else:
            g += 1
    trainings += 1
    print(str(g), "****", trainings)
    if g == size:
        break
