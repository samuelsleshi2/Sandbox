# class with three attributes all set to zero
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # this allows attributes from objects of this class to be properly printed
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    # this allows attributes from objects of this class to be properly added
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

# Vault object made
potter = Vault(100, 50, 25)
print(potter)

# Vault object made
weasley = Vault(25, 50, 100)
print(weasley)

# dunder addition method is called here, first object is self, second is other
total = potter + weasley
print(total)