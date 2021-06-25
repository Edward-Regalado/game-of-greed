class Banker:
    """
    used for tracking/saving points from dice rolls
    """
    def __init__(self, balance=0, shelved=0):
        """
        initializes a new instance of Banker
        """
        self.balance = balance
        self.shelved = shelved

    def shelf(self, amount_of_points):
        """
        takes in an amount of points and adds to shelf
        """
        self.shelved = self.shelved + amount_of_points

    def bank(self):
        """
        takes value of shelved variable and adds to balance variable, then resets shelved variable
        """
        self.balance = self.balance + self.shelved
        self.shelved = 0

    def clear_shelf(self):
        """
        resets shelved variable to 0
        """
        self.shelved = 0

