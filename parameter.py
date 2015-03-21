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
