# Duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if the minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("The duck is walking")

    def talk(self):
        print("The duck is quacking")


class Chicken:
    def walk(self):
        print("The chicken is walking")

    def talk(self):
        print("The chicken is clucking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

# we can pass a different type of object as long as it has the same methods/attributes
person.catch(chicken)
