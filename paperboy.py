class Paperboy:

    """ A class representing the main character in a 1985 arcade game called "Paperboy" """

    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return "Paperboy: {}".format(self.name)

    def quota(self):
        return 50 + (self.experience//2)

    def deliver(self, start_address, end_address):
        current_quota = self.quota()
        n_houses = abs(end_address - start_address) + 1
        if n_houses >= current_quota:
            self.earnings += 0.25 * (current_quota + 2 * (n_houses - current_quota))
        else:
            self.earnings += 0.25 * n_houses - 2
        self.experience += n_houses

    def report(self):
        return "I'm {}, I've delivered {} papers and I've earned ${:.2f} so far!".format(self.name, self.experience, self.earnings)


# instantiating the Paperboy class (creating an object of class Paperboy)
tommy = Paperboy("Tommy")
print(tommy)
# checking the quota for the day
print(tommy.quota())
# deliver to 60 houses today
tommy.deliver(101, 160)
print(tommy.earnings)
# report the status
print(tommy.report())

# check quota again
print(tommy.quota())
# deliver to 75 houses
tommy.deliver(1,75)
print(tommy.earnings)
# report the status
print(tommy.report())
