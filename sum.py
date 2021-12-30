sampleList = list(())
sumOfValues = 0

for x in range(0, 3):
    ui = int(input("What is your number? "))
    sampleList.append(ui)

for x in sampleList:
    sumOfValues += x

print(sumOfValues)
