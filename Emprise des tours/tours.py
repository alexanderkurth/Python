import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

cote = lines[0]
del(lines[0])

cases = int(cote) * int(cote)


X = set()
Y = set()

pX = 0
pY = 0

compteur = 0

for line in lines:
    x,y = list(map(int, line.split()))
    X.add(x)
    Y.add(y)

for i in range(1,len(X)+2) :
    if i not in X :
        pX = i
        break

for i in range(1,len(Y)+2):
    if i not in Y:
        pY = i
        break


if(pX >= int(cote)+1 and pY >= int(cote)+1 or pX >= int(cote)+1 and pY == 2 or pX == 2 and pY >= int(cote)+1) :

    print("Emprise totale")
else:
    print(pX,pY)