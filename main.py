from animal import Animal
from dog import Dog

if __name__ == "__main__":
# TODO: Create an instance of the Animal class
    animal1 = Animal("Simba", "Lion")

# TODO: Print the Animal instance
    print(animal1)

# TODO: Call the method to make a generic animal sound
    print(animal1.speak())
    print("-----")

# TODO: Create an instance of the Dog class
    dog1 = Dog("Buddy", "Canine", "Golden Retriever")

# TODO: Print the Dog instance
    print(dog1)

# TODO: Call the method to make the dog-specific sound
    print(dog1.speak())
    print("-----")

# TODO print out all the animals
    print("All animals:")
    Animal.all_animals
    print(animal1)
    print(dog1) 