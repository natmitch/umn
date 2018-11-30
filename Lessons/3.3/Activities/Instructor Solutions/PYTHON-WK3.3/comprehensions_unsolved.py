"""
* Run the provided program. Note that nothing forces you to write the name
  "properly"—e.g., as "Jane" instead of "jAnE".
  You will use list comprehensions to fix this.

  * First, use list comprehensions to create a new list that contains
    the lowercase version of each of the names your user provided.

  * Then, use list comprehensions to create a new list that contains
    the title-cased versions of each of the names in your lower-cased list.

  **Bonuses**
	Instead of creating a lower-cased list and _then_ a title-cased list, create the title-cased list in a single comprehension.
    Hints https://docs.python.org/3/library/stdtypes.html#str.title
"""

names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = ["YOUR CODE HERE!"]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = ["YOUR CODE HERE!"]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)

names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = ["YOUR CODE HERE!"]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = ["YOUR CODE HERE!"]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
