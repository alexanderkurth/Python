import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

del lines[0]
i = 0

for line in lines:
    temp = list(map(float, line.split()))

    if(temp[0] > 56.00 and temp[1] > 45.00 and temp[2] > 25.00 or temp[3] > 7.00 or temp[0]+temp[1]+temp[2]+temp[3]>125):
        print (0)
    else:
        print (1)
        i += 1
print (i)    