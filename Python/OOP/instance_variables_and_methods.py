class Package:

    # constructor with 5 instance variables that define a Package object
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    # defines how Package objects are directly printed out
    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, weight = {self.weight}"
    
    # calculates the cost of a package per kilogram
    def calculate_cost(self, cost_per_kg):
        return f"${float(cost_per_kg * self.weight):.2f}"


def main():
    # list that contains 2 Package objects
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]
    
    # iterates through each package in the packages list and prints them out
    for package in packages:
        print(f"{package} costs {package.calculate_cost(cost_per_kg=2)}")
        

main()