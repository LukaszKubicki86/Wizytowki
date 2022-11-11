class Player():
    """Class to represent a player."""
    def __init__(self, name):
        self.name = name
        self.hit = 0
        self.bats = 0
        self.freePass = 0
        self.out = 0
        self.defenseError = 0

    def increment_hit(self):
        """Increase hit count by one when called."""
        self.hit += 1

#  instantiate your class
steve = Player("steve")
print("Hits for '{}' after instantiate your class: {}\n".format(steve.name, steve.hit))

# call the increase_hit method 3 times
for i in range(3):
    steve.increment_hit()
    print("Hits for player {}: {}".format(steve.name, steve.hit))