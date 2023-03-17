# *args =   parameters that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of positional arguments

# def add(*numbers):
def add(*args):
    sum = 0
    # changing the first number
    # numbers[0] = 0 ERROR
    numbers = list(args)
    numbers[0] = 0
    for i in numbers:
        sum += i
    return sum


print(add(1, 2, 3, 4))
tup = (1, 2, 3, 4)
print(add(*tup))  # l'operatore unario * esplode la collection e inserisce ogni elemento come parametro


# **kwargs =    parameters that will pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments
def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Cristian", middle="Ciccio", last="Casali")
