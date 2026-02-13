
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def speak(self):
        print(f"{self.name} the mammal makes a mammal sound.")


class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span  # in centimeters

    def speak(self):
       print(f"{self.name} the bird chirps.")

       
animal = Animal("Generic Animal")
animal.speak()

mammal = Mammal("Lion", "Golden")
mammal.speak()
print(mammal.fur_color)

bird = Bird("Eagle", 200)
bird.speak()
print(bird.wing_span)