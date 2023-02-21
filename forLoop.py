# while loop can be unlimited
# for loop is always limited
import time

for i in range(10):
    print(i)
print()

for i in range(50, 100, 2):
    print(i)
print()

for i in "Cristian Casali":
    print(i)
print()

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
