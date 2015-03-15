class Adaline:

    def __init__(self):
        self.weight = [1, 1, 1, 1]
        self.learn_rate = 0.01
        self.threshold = 0.3486

    def run(self, input_data, label):

        output = self.calculateOutput(self.weight, input_data)
        delta_weight = self.calculateDeltaWeight(
            self.learn_rate, label,
            output, input_data)
        self.weight = self.calculateNewWeight(self.weight, delta_weight)

    def calculateOutput(self, w, i):
        return ((w[0]*i[0]) + (w[1]*i[1]) + (w[2]*i[2]) + (w[3]*i[3])+ self.threshold)

    def calculateDeltaWeight(self, n, t, r, x):
        c = n*(t-r)
        return [c*x[0], c*x[1], c*x[2], c*x[3]]

    def calculateNewWeight(self, w, dw):
        return [w[0]+dw[0], w[1]+dw[1], w[2]+dw[2], w[3]+dw[3]]

    def activationFunction(self, w, i):
        if (i[0]==-1):
            i[0]=self.threshold
            
        val = w[0]*i[0] + w[1]*i[1] + w[2]*i[2] + w[3]*i[3] + self.threshold
        # print(val)
        # if(val <= 0):
        #     print(w)
        if(val > 0.5):
            return 1
        else:
            return 0
