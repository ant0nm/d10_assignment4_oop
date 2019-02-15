import math

class Paperboy:

    """ A class representing the main character in a 1985 arcade game called "Paperboy" """

    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return "Paperboy: {}".format(self.name)

    def quota(self):
        # might have to round this to an integer
        return 50 + (self.experience/2)

    def deliver(self, start_address, end address):
        current_quota = self.quota()
        n_houses = abs(end_address - start_address) + 1
        if n_houses >= current_quota:
            self.earnings = 0.25 * (current_quota + 2 * (n_houses - current_quota))
        else:
            self.earnings = 0.25 * n_houses - 2


# instantiating the Paperboy class (creating an object of class Paperboy)
tommy = Paperboy("Tommy")
print(tommy)
# checking the quota for the day
print(tommy.quota())
