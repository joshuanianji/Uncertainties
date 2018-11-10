class Values:
    def __init__(self, actual, absolute_unc):
        self.actual = actual
        self.absolute_unc = absolute_unc
        self.percent_unc = abs(absolute_unc / actual)

    def output_absolute(self):
        return (str(self.actual) + " ± " + str(self.absolute_unc))

    def output_relative(self):
        return (str(self.actual) + " (" + str(self.percent_unc * 100) + "%)")

    def output_range(self):
        upper = self.actual + self.absolute_unc
        lower = self.actual - self.absolute_unc
        return ("[" + str(lower) + ", " + str(upper) + "]")
