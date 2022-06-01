f = open("input2.txt", 'r')
prevDepth = int(f.readline())
count = 0
print(prevDepth,"Nothing to measure")
for x in f:
    x = x.strip()
    if int(x) > prevDepth:
        print(x, "Increased")
        count += 1
    elif int(x) == prevDepth:
        print(x, "Didnt change")
    else:
        print(x, "Decreased")
    prevDepth = int(x)
print("Depth increased", count, " times")

#LEARNED
#As a person coming from C#, this is what I learned:
#How to read from files
#How to create variables (apparently they are assigned automatically what the heck?
#How to print multiple variables
#How for loops work (seriously what the hell is this
#count++ doesn't work :pepehands:
