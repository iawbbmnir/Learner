from custom_distribution import CustromDistribution
from adaline import Adaline
from parameter import Parameter, ParameterNames
import random
import csv

class Learner:

    def __init__(self):
        self.param_names = ParameterNames()

        self.pclass_distr = Parameter(self.param_names.pclass)
        self.sex_distr = Parameter(self.param_names.sex)
        self.age_distr = Parameter(self.param_names.age)
        self.sibsp_distr = Parameter(self.param_names.sibsp)
        self.parch_distr = Parameter(self.param_names.parch)
        self.fare_distr = Parameter(self.param_names.fare)
        self.embarked_distr = Parameter(self.param_names.embarked)

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
#         with open('output.csv', 'a', newline='') as csvfile:
#              spamwriter = csv.writer(csvfile,  quoting=csv.QUOTE_NONNUMERIC)
#              spamwriter.writerow([str(data[self.param_names.pid]) , str(result)])

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






        # Update Distribution

        # return 0

        # return self.fuzzyNoLearning(data)

        # if(data[self.param_names.pclass] == '1'):
        #     return 1
        # elif(data[self.param_names.pclass] == '2'):
        #     survived = random.randrange(0, 2, 1)
        #     # print(survived)
        #     return survived
        # elif(data[self.param_names.pclass] == '3'):
        #     return 0

        # if(data[self.param_names.sex] == 'male'):
        #     return 0
        # else:
        #     return 1

        # Update Distribution for each Parameter
        # self.runNaiveDistribution(data)
        # Recalibrate Weight for each Parameter

        # Aggregate Chance of Survival Decision

        # return 0

    # def runNaiveDistribution(self, data):
    #     # self.pclass_distr =
    #     return None

    def fuzzyNoLearning(self, data):
        pr_sex = 0
        pr_pclass = 0
        pr_age = 0
        pr_sibsp = 0
        pr_parch = 0

        try:
            if(data[self.param_names.sex] == 'male'):
                pr_sex = 0
            else:
                pr_sex = 1

            if(data[self.param_names.pclass] == '1'):
                pr_pclass = 1
            elif(data[self.param_names.pclass] == '2'):
                pr_pclass = 0.5
            elif(data[self.param_names.pclass] == '3'):
                pr_pclass = 0

            age_int = int(data[self.param_names.age])
            if(age_int < 20):
                pr_age = 0.48
            elif(age_int < 40):
                pr_age = 0.38
            elif(age_int < 60):
                pr_age = 0.39
            elif(age_int < 80):
                pr_age = 0.27

            sibsp_int = int(data[self.param_names.sibsp])
            if(sibsp_int < 2):
                pr_sibsp = 0.394
            elif(sibsp_int < 4):
                pr_sibsp = 0.386
            elif(sibsp_int < 6):
                pr_sibsp = 0.13
            elif(sibsp_int < 8):
                pr_sibsp = 0

            parch_int = int(data[self.param_names.parch])
            if(parch_int < 2):
                pr_parch = 0.374
            elif(parch_int < 4):
                pr_parch = 0.506
            elif(parch_int < 6):
                pr_parch = 0.1

            w_sex = 0.5
            w_pclass = 0.25
            w_age = 0.125
            w_sibsp = 0.0625
            w_parch = 0.0625

            pr_aggregate = w_sex*pr_sex + w_pclass*pr_pclass + w_age*pr_age + w_parch*pr_parch + w_sibsp*pr_sibsp
            threshold = 0.383838

            # print(pr_aggregate)

            if(pr_aggregate - threshold > 0):
                # print("asdsad")
                return 1    # Alive
            else:
                return 0    # Dead
        except ValueError:
            return 0
