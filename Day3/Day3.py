file = "input2.txt"
f = open(file, 'r')
starter = f.readline().strip()
f.close()

nill = 0
uno = 0

gamma = ""
epsilon = ""

for x in range(len(starter)):
    f = open(file, 'r') #i dont think this is good coding practice
    for y in f:
        y = y.strip()
        y = list(y)
        
        if int(y[x]) == 0:
            nill += 1
        if int(y[x]) == 1:
            uno += 1
    
    if nill > uno:
        gamma += '0'
        epsilon += '1'
    elif uno > nill:
        gamma += '1'
        epsilon += '0'
        
    nill = 0
    uno = 0
    f.close()

    
print(int(gamma, base=2)*int(epsilon, base=2))
        
#WHAT I LEARNED
#Making this program I learned:
#If you're insane, it's ok to open and close the file repeatedly :pepe_pray:
#How to turn string of binary into a binary or decimal integer
#When creating an int binary variable, it must be preceded by 0b or 0o
#This program is a mess

