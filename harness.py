import csv
from learner import Learner


def main():

    # Initialize learner
    learner = Learner()

    print('PassengerId,Survived')

    with open('test.csv', 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in data_reader:
            # Send data to learner
            learner.processInput(row)
            # print(result)

    learner.printAccuracy()
    learner.printWeight()

if __name__ == "__main__":
    main()
