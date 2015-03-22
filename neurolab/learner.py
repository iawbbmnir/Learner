from parameter import ParameterNames
from single_layer_perceptron import *
from multi_layer_feed_forward_perceptron import *
from learning_vector_quantization import *


class Learner:
    def __init__(self, train_raw_data, test_raw_data):
        self.train_raw_data = train_raw_data
        self.test_raw_data = test_raw_data
        self.pn = ParameterNames()

    # Domain: {Sex, Age, PClass, Fare}
    def run(self, alg):
        data_domain = []
        data_label = []

        for instance in self.train_raw_data:
            inst_age = int(instance[self.pn.age])
            inst_pclass = int(instance[self.pn.pclass])
            inst_sex = 1
            inst_fare = instance[self.pn.fare]
            if instance[self.pn.sex] == 'female':
                inst_sex = 0
            data_domain.append([
                inst_sex,
                inst_age,
                inst_pclass,
                inst_fare
            ])
            data_label.append([
                instance[self.pn.survival]
            ])

        test_domain = []
        test_true_label = []

        for instance in self.test_raw_data:
            inst_age = int(instance[self.pn.age])
            inst_pclass = int(instance[self.pn.pclass])
            inst_sex = 1
            inst_fare = instance[self.pn.fare]
            if instance[self.pn.sex] == 'female':
                inst_sex = 0
            test_domain.append([
                inst_sex,
                inst_age,
                inst_pclass,
                inst_fare
            ])
            test_true_label.append([
                instance[self.pn.survival]
            ])

        minMax = self.getMinMaxValues(data_domain)

        # Train and Test

        if(alg == 1):
            # Single Layer Perceptron
            slp = SingleLayerPerceptron(data_domain, data_label, minMax)
            test_label = slp.test(test_domain)
            self.analyzeTest(test_domain, test_label, test_true_label)
        elif(alg == 2):
            # Multi Layer Feed Forward Perceptron
            mlffp = MultiLayerFeedForwardPerceptron(data_domain, data_label, minMax)
            test_label = mlffp.test(test_domain)
            self.analyzeTest(test_domain, test_label, test_true_label)
        elif(alg == 3):
            lvq = LearningVectorQuantization(data_domain, data_label, minMax)
            test_label = lvq.test(test_domain)
            self.analyzeTest(test_domain, test_label, test_true_label)

    def analyzeTest(self, domain, test_label, true_label):
        total_count = 0
        total_correct = 0
        for i in range(0, len(test_label)):
            test_label_int = int(test_label[i][0])
            true_label_int = int(true_label[i][0])
            if test_label_int == true_label_int:
                total_correct += 1
            else:
                print(str(domain[i]) + " -> True:" + str(true_label[i][0]))
            total_count += 1
        accuracy = float(total_correct) / float(total_count)
        print(str(total_correct) + " / " + str(total_count))
        print(str(accuracy))

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
