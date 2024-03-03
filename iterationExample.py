ite = int(input("Iteration: "))
x = 1
sum = 0
totalNum = 0
totalStr = " "
while x <= ite:
    usIn = input("Input" + str(x) + ":")
    x += 1
    if usIn.isalpha():
        totalStr += usIn
    else:
        sum += float(usIn)
        totalNum += 1
ave = sum / totalNum
print("Average: " + str(ave))
print("Phrase: " + totalStr)
