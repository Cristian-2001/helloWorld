animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format("cow", "moon"))
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))   # positional arguments
# print("The {1} jumped over the {1}".format(animal, item))   # positional arguments
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))   # keyword arguments
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))   # keyword arguments

# text = "The {} jumped over the {}"
# print(text.format(animal, item))


# name = "Cri"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you.".format(name))    # add left padding
# print("Hello, my name is {:<10}. Nice to meet you.".format(name))   # left align
# print("Hello, my name is {:>10}. Nice to meet you.".format(name))   # right align
# print("Hello, my name is {:^10}. Nice to meet you.".format(name))   # center

number = 3.14159
number2 = 1000
print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number2))
print("The number is {:b}".format(number2))
print("The number is {:o}".format(number2))
print("The number is {:x}".format(number2))
print("The number is {:X}".format(number2))
print("The number is {:e}".format(number2))
print("The number is {:E}".format(number2))
