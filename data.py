class Data:

    def __init__(self, input):
        self.id = input[0]
        self.survival = input[1]    # Survival (0 = No; 1 = Yes)
        self.pclass = input[2]      # Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
        self.name = input[3]
        self.sex = input[4]
        self.age = input[5]
        self.sibsp = input[6]       # Number of Siblings/Spouses Aboard
        self.parch = input[7]       # Number of Parents/Children Aboard
        self.ticket = input[8]
        self.fare = input[9]
        self.cabin = input[10]
        self.embarked = input[11]   # Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
