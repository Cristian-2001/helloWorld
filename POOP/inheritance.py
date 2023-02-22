class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Prey:
    def flee(self):
        print("This animal flees")


class Rabbit(Animal, Prey):  # multiple inheritance
    def run(self):
        print("This rabbit is running")

    def eat(self):  # to override a mathod it needs the same signature (name and parameters)
        print("This rabbit is eating a carrot")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
rabbit.flee()
rabbit.eat()
fish.swim()
hawk.fly()
