from custom_distribution import CustromDistribution
from adaline import Adaline
from parameter import ParameterNames


class Learner:

    def __init__(self):
        self.param_names = ParameterNames()

        self.total_count = 0
        self.total_correct = 0

        self.custom_distribution = CustromDistribution()
        self.adaline = Adaline()

    def printAccuracy(self):
        if(self.total_count > 0):
            accuracy = float(self.total_correct) / float(self.total_count)
            print(str(self.total_correct) + " / " + str(self.total_count))
            print(str(accuracy))

    def printWeight(self):
        print(self.adaline.weight)

    def processInput(self, input):
        data = {
            self.param_names.pid:       input[0],
            self.param_names.survival:  int(input[1]),
            self.param_names.pclass:    input[2],
            self.param_names.name:      input[3],
            self.param_names.sex:       input[4],
            self.param_names.age:       input[5],
            self.param_names.sibsp:     input[6],
            self.param_names.parch:     input[7],
            self.param_names.ticket:    input[8],
            self.param_names.fare:      input[9],
            self.param_names.cabin:     input[10],
            self.param_names.embarked:  input[11],
        }

        result = self.runAlgorithm(data)
        # print(str(data[self.param_names.pid]) + "," + str(result))

        self.total_count += 1
        if(data[self.param_names.survival] == result):
            self.total_correct += 1

        return result

    # Run algorithm
    def runAlgorithm(self, data):

        pr_age = self.custom_distribution.age.getProb(data[self.param_names.age])
        pr_pclass = self.custom_distribution.pclass.getProb(data[self.param_names.pclass])
        pr_sex = self.custom_distribution.sex.getProb(data[self.param_names.sex])
        pr_fare = self.custom_distribution.fare.getProb(data[self.param_names.fare])

        survival = data[self.param_names.survival]
        if(not(pr_age == -1 or pr_pclass == -1 or pr_sex == -1 or pr_fare == -1)):
            self.adaline.run([pr_age, pr_pclass, pr_sex, pr_fare], survival)

        # Learning Rate 0.01, 0 theta
        # output = self.adaline.activationFunction(
        #     [-0.22046440073361248, 0.5018039889900953, 0.8296801455781263],
        #     [pr_age, pr_pclass, pr_sex]
        # )

        # Learning Rate 0.01, 0 theta
        # output = self.adaline.activationFunction(
        #     [-0.04215897610620154, 0.3415493987698125, 0.7733980199678574, 0.07126931277513224],
        #     [pr_age, pr_pclass, pr_sex, pr_fare]
        # )

        output = self.adaline.activationFunction(
            [-0.2936669007818634, 0.5132057650194437, 0.8358729210347197, 0.03630963825040645],
            [pr_age, pr_pclass, pr_sex, pr_fare]
        )

        return output
