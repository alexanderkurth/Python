import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

del lines[0]
i = 0

for line in lines:
    x,y,z,g = list(map(float, line.split()))

    if(x > 56.00 and x+y+z > 125):
        print (0)
    elif(y > 45.00 and x+y+z > 125):
        print(0)
    elif(z >25.00 and x+y+z > 125):
        print(0)
    elif(g > 7.00):
        print(0)
    else:
        print(1)
        i+=1

print (i)    