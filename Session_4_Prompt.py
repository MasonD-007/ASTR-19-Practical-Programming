"""
Write a Python program that declares a class describing your favorite animal. 
Have the data members of the class represent the following physical parameters of the animal: 
    length of the arms (float), 
    length of the legs (float), 
    number of eyes (int), 
    does it have a tail? (bool), 
    is it furry? (bool). 
Write an initialization function that sets the values of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
"""
class favorateAnimal:
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
    def printInfo(self):
        print("My favorite animal has", self.arms, "arms,", self.legs, "legs,", self.eyes, "eyes,", self.tail, "tail,", "and is", self.furry, "furry.")

if __name__ == "__main__":
    panda = favorateAnimal(2, 2, 2, True, True)
    panda.printInfo()