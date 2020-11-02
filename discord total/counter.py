data = open("my_time.txt", "r").read().split("\n")



arrayNum = [] 

#numbers 1-9 (1, 2, 3, 4...)
for i in range(10):
    arrayNum.append(str(i))


# functions 

def numberGen(string):



    arrayCount = []

    for i in string:
            for x in arrayNum:
                     if i == x:
                        arrayCount.append(i)


    output = 0
    for i in arrayCount:
        output += int(i + "0" * (len(arrayCount) - (arrayCount.index(i) + 1)))



    return formFinder(string, output)



def formFinder(string, output):
    finalOutput = 0

    for i in string:
        if i == "-":
            if string[string.index(i) + 1] == "h":
                finalOutput = output * 60
            else:
                finalOutput = output

    return finalOutput

output = 0


# value finder

for i in data:
    if i == '':
        pass
    else:
        output += numberGen(data[data.index(i)])


#formatter

if output / 60 < 1:
    print(str(output) + " min")
else:
    print(str(output / 60) + " hours")