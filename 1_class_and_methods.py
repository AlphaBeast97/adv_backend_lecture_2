# Concept: class, __init__ constructor, and instance methods
# Example: a Recipe 

class Recipe:
    def __init__(self, name, cook_time_minutes, servings):
        # instance attributes - unique to each object
        self.name = name
        self.cook_time_minutes = cook_time_minutes
        self.servings = servings

    # instance method 1: simple display
    def show_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"  Cook time : {self.cook_time_minutes} minutes")
        print(f"  Servings  : {self.servings}")

    # instance method 2: works with the object's own data
    def time_per_serving(self):
        return self.cook_time_minutes / self.servings

    # instance method 3: changes the object's state
    def scale(self, factor):
        self.servings = self.servings * factor

        # bigger batch takes longer, smaller batch takes less time
        if factor > 1:
            self.cook_time_minutes = int(self.cook_time_minutes * 1.2)
        else:
            self.cook_time_minutes = int(self.cook_time_minutes * 0.8)

        print(f"  Scaled '{self.name}' -> now serves {self.servings}")


if __name__ == '__main__':
    # creating two objects (instances) of the same class
    biryani = Recipe("Chicken Biryani", 60, 4)
    omelette = Recipe("Masala Omelette", 10, 1)

    biryani.show_recipe()
    print(f"  Time per serving : {biryani.time_per_serving()} minutes\n")

    omelette.show_recipe()
    print(f"  Time per serving : {omelette.time_per_serving()} minutes\n")

    # calling a method that modifies the object
    biryani.scale(2)
    biryani.show_recipe()
    print(f"  Time per serving : {biryani.time_per_serving()} minutes\n")
