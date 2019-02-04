import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

for line in lines:

    temp = list(map(int, line.split()))

    i = 1
    verif = 0
    

    for i in range(1, temp[0]):
        if(1 <= abs(temp[i]-temp[i+1]) <= temp[0]-1):
            verif = 0
        else:
            verif = 1

    if(verif == 0):
        print("Jolly")
    else :
        print("Not jolly")



