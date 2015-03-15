from parameter_config import ParameterConfig
from distribution import Distribution


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


class Parameter:

    def __init__(self, param_name):
        self.weight = 1
        self.distr_interval = self.getDistrInterval(param_name)
        self.distribution = Distribution(self.distr_interval)

    def getDistrInterval(self, param):
        params = ParameterNames()
        config = ParameterConfig()
        if(param == params.fare):
            return config.FARE_DISTR_KEY_INTERVAL_RANGE
        elif(param == params.age):
            return config.AGE_DISTR_KEY_INTERVAL_RANGE
        else:
            return -1
