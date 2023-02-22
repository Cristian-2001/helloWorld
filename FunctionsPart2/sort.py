# sort() method     = used with lists
# sort() function   = uses with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

# students.sort()
# students.sort(reverse=True)
sorted_students = sorted(students)  # sort() function accepts an iterable as parameter and return a list
# sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)

print()
# students2 = [("Squidward", "F", 60),
#              ("Sandy", "A", 33),
#              ("Patrick", "D", 36),
#              ("Spongebob", "B", 20),
#              ("Mr.Krabs", "C", 78)]
students2 = (("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr.Krabs", "C", 78))

grade = lambda grades: grades[1]
# students2.sort()
# students2.sort(key=grade, reverse=True)
sorted_students2 = sorted(students2, key=grade)

for i in sorted_students2:
    print(i)
