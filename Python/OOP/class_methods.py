import random

# class that intializes each object with a list
class Hat:
    houses = ["Lorton", "Gunston", "Pritchard", "NOVA"]

    # all hat objects share the same "houses" list and execute "sort" the same way
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# initializes a hat and calls the sort method with the name being Harry
Hat.sort("Harry")