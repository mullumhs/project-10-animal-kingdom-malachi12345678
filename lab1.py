"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.
class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        return(f"{self.name} is eating")
        
    def sleep(self):
        return(f"{self.name} is sleeping")


# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
class Fish(Animal):
        def __init__(self, name, age, habitat, fish_rating):
             super().__init__(name, age, habitat)
             self.fish_rating = fish_rating

        def swim(self):
            return(f"{self.name} is swimming")
        
        def __str__(self):
            return(self.name , self.age , self.habitat , self.fish_rating)

class Bird(Animal):
        def __init__(self, name, age, habitat, bird_rating):
             super().__init__(name, age, habitat)
             self.bird_rating = bird_rating

        def fly(self):
            return(f"{self.name} is flying")

        def __str__(self):
            return(self.name , self.age , self.habitat , self.bird_rating)

# Give each of the derived classes at least one specific behavior. E.g. fly and swim.
# Create at least two instances of the Animal derived classes with different data.


shark = Fish("shark",34,"ocean","somewhat_fishlike")
parrot = Bird("parrot","2","forest","extremely_birdlike")


# Write code that prints out the details of each animal and calls their specific behaviors.

print(shark.__str__)
print(parrot.__str__)

print(shark.swim())
print(parrot.fly())


