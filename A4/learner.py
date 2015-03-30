from parameter import ParameterNames
from single_layer_perceptron import *
from multi_layer_feed_forward_perceptron import *
from learning_vector_quantization import *


class Learner:
    def __init__(self, train_raw_data, test_raw_data):
        self.train_raw_data = train_raw_data
        self.test_raw_data = test_raw_data
        self.pn = ParameterNames()

    def run(self, alg):
        data_domain = []
        data_label = []

        for instance in self.train_raw_data:
            data_domain.append([
                instance[self.pn.ethanol],
                instance[self.pn.malic_acid],
                instance[self.pn.ash],
                instance[self.pn.alcal],
                instance[self.pn.mag],
                instance[self.pn.phenols],
                instance[self.pn.flava],
                instance[self.pn.nonflava],
                instance[self.pn.proant],
                instance[self.pn.color],
                instance[self.pn.hue],
                instance[self.pn.od280],
                instance[self.pn.proline]
            ])
            data_label.append([
                instance[self.pn.product]/10
            ])

        test_domain = []
        test_true_label = []

        for instance in self.test_raw_data:
            test_domain.append([
                instance[self.pn.ethanol],
                instance[self.pn.malic_acid],
                instance[self.pn.ash],
                instance[self.pn.alcal],
                instance[self.pn.mag],
                instance[self.pn.phenols],
                instance[self.pn.flava],
                instance[self.pn.nonflava],
                instance[self.pn.proant],
                instance[self.pn.color],
                instance[self.pn.hue],
                instance[self.pn.od280],
                instance[self.pn.proline]
            ])
            test_true_label.append([
                instance[self.pn.product]/10
            ])

        minMax = self.getMinMaxValues(data_domain)
        # print "learner", minMax

        # Train and Test

        if(alg == 1):
            # Single Layer Perceptron
            slp = SingleLayerPerceptron(data_domain, data_label, minMax)
            test_label = slp.test(test_domain)
            self.analyzeTest(test_domain, test_label, test_true_label)
        elif(alg == 2):
            # Multi Layer Feed Forward Perceptron
            mlffp = MultiLayerFeedForwardPerceptron(data_domain, data_label, minMax, test_domain)
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
            test_label_int = self.activationFunction(float(test_label[i][0]))
            true_label_int = float(true_label[i][0])

            print test_label_int
            print true_label_int

            if test_label_int == true_label_int:
                total_correct += 1
            else:
                print(str(domain[i]) + " -> True:" + str(true_label[i][0]))
            total_count += 1
        accuracy = float(total_correct) / float(total_count)
        print(str(total_correct) + " / " + str(total_count))
        print(str(accuracy))

    def activationFunction(self, label):
        print label
        if label < 0.15:
            return 0.1
        elif label > 0.25:
            return 0.3
        else:
            return 0.2

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
