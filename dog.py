from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
# TODO: Initialize the Dog class and add the breed attribute.
# The constructor should accept name, species, and breed as parameters.
    def __init__(self, name, species, breed):
        self.name = name
        self.species = species
        self.breed = breed

    def speak(self):
        return "The dog barks."


# TODO: Override the __str__ method to include the breed.
# Example output:
# Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    
# TODO: Add a method for the dog to make a specific sound. 
# Call the method `speak` and make it output a specific message like 
# "The dog barks.