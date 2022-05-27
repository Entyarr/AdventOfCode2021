def RemoveItem(listy, position, check):
    i = 0
    if len(listy) == 1: return
    while i < len(listy):
        test = list(listy[i])
        if int(test[int(position)]) == int(check):
            listy.remove(listy[i])
            i=i-1
        i=i+1
    return listy

def CalcNum(listy, position, num):
    cnt = 0
    for x in listy:
        x.strip()
        x = list(x)
        if int(x[position]) == int(num):
               cnt = cnt+1
    return cnt

file = "input2.txt"
f = open(file, 'r')
nums = f.read()
f.close()

nill = 0
uno = 0
check = 0

nums = nums.split()
oxy = nums.copy()
co = nums.copy()

for x in range(len(nums[0])):

    nill = CalcNum(oxy, x, '0')
    uno = CalcNum(oxy, x, '1')

    if nill > uno:
        RemoveItem(oxy, x, '1')
    elif uno > nill:
        RemoveItem(oxy, x, '0')
    elif uno == nill:
        RemoveItem(oxy, x, '0')

    nill = CalcNum(co, x, '0')
    uno = CalcNum(co, x, '1')
    
    if nill > uno:
        RemoveItem(co, x, '0')
    elif uno > nill:
        RemoveItem(co, x, '1')
    elif uno == nill:
        RemoveItem(co, x, '1')
print(int(oxy[0], base=2)*int(co[0], base=2))



#WHAT I LEARNED
#Making this program I learned:
#If you're insane, it's ok to open and close the file repeatedly :pepe_pray:
#How to turn string of binary into a binary or decimal integer
#When creating an int binary variable, it must be preceded by 0b or 0o
#This program is a mess
#How to define a class/function/method
#WHY CANT YOU ITERATE BACK IN A FOR LOOP??? WHO THOUGHT THIS IS A GOOD IDEA
#When you equal a list to a variable, they are linked. Forever. WHY?
#How to copy lists so theyre not dumb and connected
#This was not a fun experience, it was long and grueling
