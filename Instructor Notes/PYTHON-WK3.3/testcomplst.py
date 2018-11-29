fish = "halibut"
letters = [ ]

# create a list by looping thru each char
# in the string and push to an array
for char in fish:
	letters.append(char.upper())

print(letters)

# List comprehensions provide
# concise syntax for creating lists
letters = [char for char in fish]	#where do we need to convert to upper?

print(letters)


# We can also add conditional logic (if statements) to a list comprehension
julyTemps = [87, 85, 92, 79, 106]
hotDays = []
for temp in julyTemps:
    if temp > 90:
        hotDays.append(temp)
print(hotDays)

# List Comprehension with conditional
hotDays = [temp for temp in julyTemps if temp > 90]
print(hotDays)