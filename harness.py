import csv
from learner import Learner


def main():

    # Initialize learner
    learner = Learner()

    print('PassengerId,Survived')
    f = open("output.csv", "w")
    f.truncate()
    f.close()
    with open('output.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, 
                             quoting=csv.QUOTE_NONNUMERIC)
            spamwriter.writerow(['PassengerId' , 'Survived'])
            
    with open('train.csv', 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in data_reader:
            # Send data to learner
            learner.processInput(row)
            # print(result)

    learner.printAccuracy()
    learner.printWeight()

if __name__ == "__main__":
    main()
