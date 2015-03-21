from parameter import ParameterNames
from single_layer_perceptron import *


class Learner:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.pn = ParameterNames()

    def run(self, alg):

        # SINGLE_LAYER_PERCEPTRON
        if alg == 1:
            self.runSingleLayerPerceptron()

    # Domain: {Sex, Age, PClass}
    def runSingleLayerPerceptron(self):
        data_domain = []
        data_label = []

        for instance in self.raw_data:
            inst_age = int(instance[self.pn.age])
            inst_pclass = int(instance[self.pn.pclass])
            inst_sex = 1
            if instance[self.pn.sex] == 'female':
                inst_sex = 0
            data_domain.append([
                inst_sex,
                inst_age,
                inst_pclass
            ])
            data_label.append([
                instance[self.pn.survival]
            ])

        minMax = self.getMinMaxValues(data_domain)

        # Train and Test
        slp = SingleLayerPerceptron(data_domain, data_label, minMax)
        slp.test(None)



    def getMinMaxValues(self, data_domain):
        domain_size = len(data_domain[0])
        minMax = []
        for i in range(0, domain_size):
            curr_min = 99999
            curr_max = -1
            for inst in data_domain:
                if inst[i] < curr_min:
                    curr_min = inst[i]
                if inst[i] > curr_max:
                    curr_max = inst[i]
            minMax.append([curr_min, curr_max])
        return minMax
