import sys

lines = sys.stdin.readlines()

articles = {}
resultat = 0.00
avantEspace = True
valide = True

gap = 0

for line in lines:
    temp = list(map(str, line.split()))

    if temp == []:
        avantEspace = False

    if(avantEspace):
        articles[temp[0]] = temp[1]
    else:
        if(temp != []):
            if(temp[1] in articles):

                resultat = resultat + float(temp[0]) * float(articles.get(temp[1]))
            else:
                valide = False

if(valide):
    print('{:.2f}'.format(resultat))
else:
    print("Panier invalide")

