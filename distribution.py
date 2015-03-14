class Interval:
    def __init__(self, survived_count, total_count):
        self.survived_count = survived_count
        self.total_count = total_count


class Distribution:
    def __init__(self, interval_size):
        self.distribution = {}

    def update(self, domain_value, survival):
        
        self.distribution[key] = distr_data

    def get(self):
        return self.distribution
