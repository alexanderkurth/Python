import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

for line in lines:
    x,y = list(map(int,line.split()))

    if(x > y):
        print(">")
    elif(x < y):
        print("<")
    elif(x==y) :
        print("=")
    else:
        print("")