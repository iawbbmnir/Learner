class DecisionTreeNoLearn:
    # def __init__(self):

    # Only on sex and pclass - optimal configuration 78.67% (train)
    def runSexClass(self, sex, pclass, survival):
        pclass = int(pclass)
        if sex == 'female':
            if pclass == 1:
                return 1
            elif pclass == 2:
                return 1
            else:
                return 1
        elif sex == 'male':
            if pclass == 1:
                return 0
            elif pclass == 2:
                return 0
            else:
                return 0

    # Only on sex and age - optimal configuration 79.01% (train)
    def runSexAge(self, sex, age, survival):
        try:
            age = int(age)
        except ValueError:
            age = -1
        if sex == 'female':
            if age == -1:
                return 1
            elif age > 75:
                return 1
            else:
                return 1
        else:
            if age == -1:
                return 0
            elif age > 6:
                return 0
            else:
                return 1
