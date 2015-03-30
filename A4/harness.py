import csv
import sys
from learner import Learner
from parameter import ParameterNames


def loadData(file_name, is_training):
    pn = ParameterNames()
    data_list = []
    # WARNING: FOR TRAINING, INSTANCE IS OMITTED IF MISSING VALUE(S)
    with open(file_name, 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in data_reader:
            data = {
                pn.product:   float(row[0]),
                pn.ethanol:   float(row[1]),
                pn.malic_acid:   float(row[2]),
                pn.ash:   float(row[3]),
                pn.alcal:   float(row[4]),
                pn.mag:   float(row[5]),
                pn.phenols:   float(row[6]),
                pn.flava:   float(row[7]),
                pn.nonflava:   float(row[8]),
                pn.proant:   float(row[9]),
                pn.color:   float(row[10]),
                pn.hue:   float(row[11]),
                pn.od280:   float(row[12]),
                pn.proline:   float(row[13]),
            }
            data_list.append(data)

    return data_list


def main():

    train_file = sys.argv[1]
    test_file = sys.argv[2]
    alg_id = int(sys.argv[3])

    training_data = loadData(train_file, True)
    testing_data = loadData(test_file, False)

    # Send Training Data to Learner
    learner = Learner(training_data, testing_data)
    learner.run(alg_id)


if __name__ == "__main__":
    main()
