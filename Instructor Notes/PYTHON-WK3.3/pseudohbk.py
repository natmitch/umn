"""
## Instructions
* Create a dictionary to store the following:
  * Your name
  * Your age
  * A list of a few of your hobbies
  * A dictionary of a few times you wake up during the week

* Print out your name, how many hobbies you have
        and a time you get up during the week.
"""
# Dictionary full of info
my_info = {"name": "john",
           "occupation": "engineer" ,
           "age": 25,
           "hobbies":['Sport', "Movies"],
           "wake-up": {'Mon': '06:00', 'Tue':'07:00','Sat':'13:00'}
           }

# Print out results are stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have how many hobbies! {len(my_info["hobbies"])}')

print(f'On the weekend I get up at ...{my_info["wake-up"]["Sat"]}')
# line 26-28 produce the same result as that of 28 
waketime = my_info["wake-up"]
onSat = waketime["Sat"]
print(onSat)

print(f'On the weekend I get up at ...{my_info["hobbies"][0]} {my_info["hobbies"][1]}')

print(f'On the weekend I get up at ...{my_info["hobbies"]}')
# line 33-36 each produces the same result as that of 32
newlist = [hobbie for hobbie in my_info["hobbies"] ]
print(f'On the weekend I get up at ...{newlist}')
print( [hobbie for hobbie in my_info["hobbies"] ] )

