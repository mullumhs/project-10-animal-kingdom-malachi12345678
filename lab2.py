"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the Animal Kingdom program from Lab 1 to include polymorphism,
               demonstrating method overriding in derived classes.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Paste your base class Animal and the derived classes from Lab 1 here.
class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        return(f"{self.name} is eating")
        
    def sleep(self):
        return(f"{self.name} is sleeping")
    
    def display_info(self):
        return f"{self.name} is {self.age} and lives in a{self.habitat}."

class Fish(Animal):
        def __init__(self, name, age, habitat, fish_rating):
             super().__init__(name, age, habitat)
             self.fish_rating = fish_rating

        def swim(self):
            return(f"{self.name} is swimming")
           
        def display_info(self):
            return f"{self.name} is a fish that is {self.age} and lives in a{self.habitat} , {self.name} is also {self.fish_rating}."

class Bird(Animal):
        def __init__(self, name, age, habitat, bird_rating):
             super().__init__(name, age, habitat)
             self.bird_rating = bird_rating

        def fly(self):
            return(f"{self.name} is flying")

        def display_info(self):
            return f"{self.name} is a bird that is {self.age} and lives in a{self.habitat} , {self.name} is also {self.bird_rating}."
        







# Modify the classes to demonstrate polymorphism through method overriding.
# Each derived class should override at least one method from the Animal class.
# For instance, you might want to override a 'make_sound' method to reflect the specific sound each animal makes.





# Create at least two instances of your derived classes
shark = Fish("shark",34,"ocean","somewhat fishlike")
parrot = Bird("parrot","2","forest","extremely birdlike")




# Call the overridden methods on the instances.
print(shark.display_info())
print(parrot.display_info())



