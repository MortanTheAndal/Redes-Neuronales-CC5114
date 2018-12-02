class Perceptron(object):
    def __init__(self, w, b):
        self.weights = w
        self.bias = b

    def resolve(self, p_input):
        p_sum = 0
        for i in range(len(p_input)):
            p_sum += p_input[i] * self.weights[i]
        if p_sum + self.bias <= 0:
            return 0
        else:
            return 1




class SumPerceptron(object):
    def __init__(self):
        self.inPer = Perceptron(weights_nand, 3)
        self.outPer = Perceptron(weights_nand, 3)
        self.carryPer = Perceptron(weights_nand, 3)
        self.midOne = Perceptron(weights_nand, 3)
        self.midTwo = Perceptron(weights_nand, 3)

    def resolve(self, sum_input):
        common_response = self.inPer.resolve(sum_input)
        new_in_one = [sum_input[0], common_response]
        new_in_two = [sum_input[1], common_response]
        carry_in = [common_response, common_response]
        new_in_out = [self.midOne.resolve(new_in_one), self.midTwo.resolve(new_in_two)]
        out_list = [self.outPer.resolve(new_in_out), self.carryPer.resolve(carry_in)]
        return out_list
