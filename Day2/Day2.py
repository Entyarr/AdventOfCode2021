X = 0
Y = 0

f = open("input2.txt", 'r')

for x in f:
    cmd = x.split()
    key = cmd[0]
    val = int(cmd[1])
    if key == "forward":
        X += val
    if key == "down":
        Y += val
    if key == "up":
        Y -= val
print(X*Y)

#WHAT I LEARNED
#Doing this program I learned:
#Lists can be made up of various elements
#How to split strings into lists

