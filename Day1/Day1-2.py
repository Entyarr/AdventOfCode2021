f = open("input2.txt", 'r')
depth = [0, 0, 0]
for x in range(len(depth)):
    depth[x] = int(f.readline())
depthSum1 = sum(depth)
print(depthSum1, "Nothing to compare")
count = 0
for x in f:
    for y in range(2):
        depth[y] = depth[y+1]
    depth[2] = int(x.strip())    
    depthSum = sum(depth)
    if depthSum > depthSum1:
        print(depthSum, "Increased")
        count += 1
    elif depthSum == depthSum1:
        print(depthSum, "Didnt change")
    else:
        print(depthSum, "Decreased")
    depthSum1 = sum(depth)
print("Depth increased", count, " times")

#LEARNED
#As a person coming from C#, this is what I learned:
#How python for loops work regarding rage
#python for loops work awfully similarly to foreach loop in C#
#Unlike C#, everytime you read a line from file, it remembers you read it
