class Food:

    # class variable that is shared by class and all its instances
    base_hearts = 1

    # constructor with an attribute, and a class method for another one
    def __init__(self, ingredients):
        self.ingredients = ingredients
        # uses a class method to initalize an attribute of the Food object
        self.hearts = Food.calculate_hearts(ingredients)

    # class method that defines how all Food objects get their amount of hearts
    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    # alternative constructor that creates a Food object with a specified amount of hearts
    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food

# makes a Food object, prints its hearts
def main():
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

# makes a Food object, specifies its hearts with .from_nothing, and prints its hearts
    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")



main()