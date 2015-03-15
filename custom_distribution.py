class CustromDistribution:
    def __init__(self):
        self.fare = CustomFareDistribution()
        self.age = CustomAgeDistribution()
        self.pclass = CustomClassDistribution()
        self.sex = CustomSexDistribution()


class CustomFareDistribution:
    def __init__(self):
        self.distr = {
            1: 0.3192,
            51: 0.6481,
            101: 0.7917,
            151: 0.6667,
            201: 0.6364,
            251: 0.6667,
            301: 1,
            351: 1,
            401: 1,
            451: 1,
            501: 1
        }

    def getProb(self, fare_str):
        try:
            fare_int = int(fare_str)
            if(fare_int == 0):
                return self.distr[1]
            key = (int((fare_int-0.0001)/50) * 50) + 1
            return self.distr[key]

        except ValueError:
            return 0


class CustomAgeDistribution:
    def __init__(self):
        self.distr = {
            1: 0.7045,
            6: 0.3500,
            11: 0.5789,
            16: 0.3438,
            21: 0.3443,
            26: 0.3889,
            31: 0.4659,
            36: 0.4179,
            41: 0.3617,
            46: 0.4103,
            51: 0.4167,
            56: 0.3889,
            61: 0.2857,
            66: 0,
            71: 0,
            76: 1
        }

    def getProb(self, age_str):
        try:
            age_int = int(age_str)
            key = (int((age_int-0.0001)/5) * 5) + 1
            return self.distr[key]

        except ValueError:
            return 0.34


class CustomClassDistribution:
    def __init__(self):
        self.distr = {
            '1': 0.6296,
            '2': 0.4728,
            '3': 0.2424
        }

    def getProb(self, pclass_str):
        if(pclass_str == '1'):
            return self.distr['1']
        elif(pclass_str == '2'):
            return self.distr['2']
        elif(pclass_str == '3'):
            return self.distr['3']
        else:
            return 0


class CustomSexDistribution:
    def __init__(self):
        self.distr = {
            'male': 0.1889,
            'female': 0.7420
        }

    def getProb(self, sex_str):
        if(sex_str == 'male'):
            return self.distr['male']
        elif(sex_str == 'female'):
            return self.distr['female']
        else:
            return 0
