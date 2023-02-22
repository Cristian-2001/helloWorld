# set = collection which is unordered, unindexed. No duplicated values

utensil = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensil.add("napkin")
# utensil.remove("fork")
# utensil.clear()
# utensil.update(dishes)
# dinner_table = utensil.union(dishes)
# print(utensil.difference(dishes))
# print(dishes.difference(utensil))
print(utensil.intersection(dishes))

for x in utensil:
    print(x)
print()

# for x in dinner_table:
#     print(x)
