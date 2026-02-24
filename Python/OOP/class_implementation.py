class Student:
    # constructor for Student class, two attributes
    def __init__(self, name, house):
        self.name = name
        self.house = house
    

    # allows us to print out objects of this class
    def __str__(self):
        return f"{self.name} from {self.house}"
    

    # this allows us to not have to create a Student object
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


    # gets the student object and prints its attributes out
def main():
    student = Student.get()
    print(student)


    # only run main function if this file is explicitly executed in terminal
if __name__ == "__main__":
    main()