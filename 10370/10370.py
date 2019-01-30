import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

del lines[0]

for line in lines:
    temp = list(map(int, line.split()))

    i = 1
    somme = 0
    compteur = 0

    for i in range(1, temp[0]+1) : 
        somme = somme + temp[i]
    
    somme = somme / temp[0]

    for i in range(1, temp[0] + 1):
        if(temp[i] > somme):
            compteur += 1

    compteur = (compteur*100)/temp[0]
    print('{:.3f}%'.format(compteur))
