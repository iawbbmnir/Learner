import csv
import sys
from learner import Learner

SINGLE_LAYER_PERCEPTRON = 1


class ParameterNames:
    def __init__(self):
        self.pid = "Passenger_Id"
        self.survival = "Survival"              # Survival (0 = No; 1 = Yes)
        self.pclass = "Passenger_Class"         # Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
        self.name = "Full_Name"
        self.sex = "Sex"
        self.age = "Age"
        self.sibsp = "Num_Siblings_Spouses"     # Number of Siblings/Spouses Aboard
        self.parch = "Num_Parents_Children"     # Number of Parents/Children Aboard
        self.ticket = "Ticket_Num"
        self.fare = "Fare_Price"
        self.cabin = "Cabin_Id"
        self.embarked = "Embarking_Port"        # Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)


def loadData(file_name, is_training):
    pn = ParameterNames()
    data_list = []
    # WARNING: FOR TRAINING, INSTANCE IS OMITTED IF MISSING VALUE(S)
    with open(file_name, 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in data_reader:
            try:
                int_age = int(row[5])
            except ValueError:
                int_age = 30  # Average Age
            data = {
                pn.pid:       int(row[0]),
                pn.survival:  int(row[1]),
                pn.pclass:    int(row[2]),
                pn.name:      row[3],
                pn.sex:       row[4],
                pn.age:       int_age,
                pn.sibsp:     int(row[6]),
                pn.parch:     int(row[7]),
                pn.ticket:    row[8],
                pn.fare:      row[9],
                pn.cabin:     row[10],
                pn.embarked:  row[11],
            }
            data_list.append(data)

    return data_list


def main():

    train_file = sys.argv[1]
    test_file = sys.argv[2]

    training_data = loadData(train_file, True)
    testing_data = loadData(test_file, False)

    # Send Training Data to Learner
    learner = Learner(training_data, testing_data)
    learner.run(SINGLE_LAYER_PERCEPTRON)


if __name__ == "__main__":
    main()
