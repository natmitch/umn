names = []
for _ in range(2):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# input = jOHn --> john
#lowercased = [name.lower() for name in names]

#john = John
#titlecased = [name.title() for name in lowercased]

titlecased =[name.lower().title() for name in names]
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased
    ]

for invitation in invitations:
    print(invitation)

print("jOHn AND amANDa".lower().title())