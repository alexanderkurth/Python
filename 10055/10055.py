import sys

lines = sys.stdin.readlines()
del lines[-1]
if lines[-1] == ' ': del lines[-1]

for line in lines:
    x,y = list(map(int,line.split()))
    print(y-x)


    
