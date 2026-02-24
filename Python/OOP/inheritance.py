# class with one attribute
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


# inherits from Wizard, inherits its name attribute, and adds a new attribute
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


# inherits from Wizard, inherits its name attribute, and adds a new attribute
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# an object from each class is instantiated here
wizard = Wizard("Sam")
student = Student("Lebron", "Kobe")
professor = Professor("Shaq", "Winning the Championship 101")