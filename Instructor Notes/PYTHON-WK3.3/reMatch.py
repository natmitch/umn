#!/usr/bin/python
import re

# https://docs.python.org/2/library/re.html
# https://docs.python.org/2/howto/regex.html#regex-howto

# r raw string
# . matches any character except a newline
# * matches >= 0 occurrences in the preceding RE
# ? matches 0 or 1 occurrence of the preceding RE
# M matches multiline
# I matches case-insensitive
# + matches >= 1 occurrences of the one-character regular expression
# ( ) define a group
# group() == group(0)
"""
#-------------------------------------------------------------
line = "Most cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#matchObj = re.match( r'(.*) are (.*?) (.*)', line, re.M|re.I)


if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   #print ("matchObj.group(3) : ", matchObj.group(3))
else:
   print ("No match!!")
#-------------------------------------------------------------

"""
def titlecase(str):
	return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",	# + is not string concatenation
		lambda mo: mo.group()[0].upper() +		# + is string concatenation
		mo.group()[1:].lower(),str)

print(titlecase("they're bill's friends.")) 

#==========================================================================
"""
input = "abcdefghi jklmnop"
print(input)

print("\nre.sub(r'\s+', '',   input) # Eliminate duplicate whitespaces")
print( re.sub(r'\s+', ' ',   input) )
print('-' * 40)
print("re.sub('abc',  '',    input)	# Delete pattern abc")
print( re.sub('abc',  '',    input) )
print('-' * 40)
print("\nre.sub('abc',  'def', input) # Replace pattern abc -> def")
print( re.sub('abc',  'def', input) )
print('-' * 40)
print("\nre.sub('abc(def)ghi', r'\1', 'abcdefghi')	# Replace a string with a part of itself")
print( re.sub('abc(def)ghi', r'\1', 'abcdefghi') )
"""

"""
the examples below show no difference between
re.replace() and re.sub() functions

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

print('=' * 40)

newstr2 = str.replace("David", "Amy")
print (newstr2)
"""
