listOfStrings = list()

numberOfInput = int(input("How many entities? "))

for x in range(0, numberOfInput):
    userEntry = input("Enter your string: ")
    listOfStrings.append(userEntry)

findPhrase = input("What do you want to search for? ")

for x in listOfStrings:
    if x == findPhrase:
        print("Found!")
        break
    else:
        print("Not found!");