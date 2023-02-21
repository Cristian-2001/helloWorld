# [start:stop:step]

name = "Cristian Casali"

# first_name = name[0]
# first_name = name[0:8]
first_name = name[:8]
# last_name = name[9:15]
last_name = name[9:]

# funky_name = name[0:15:2]
funky_name = name[::3]

reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
