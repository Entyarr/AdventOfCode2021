X = 0 #forwards
Y = 0 #depth
Z = 0 #aim

f = open("input2.txt", 'r')

for x in f:
    cmd = x.split()
    key = cmd[0]
    val = int(cmd[1])
    if key == "forward":
        X += val
        Y += val * Z
    if key == "down":
        Z += val
    if key == "up":
        Z -= val
print(X*Y)

#WHAT I LEARNED
#Doing this program I learned:
#Lists can be made up of various elements
#How to split strings into lists
