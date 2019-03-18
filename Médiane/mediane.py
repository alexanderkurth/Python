import sys

lines = sys.stdin.readlines()
if lines[-1] == ' ':del lines[-1]

nombremediane = lines[0]
del(lines[0])

for line in lines:
    valeur = list(map(float, line.split()))
    nombre = valeur[0]
    del(valeur[0])
 #   print(valeur)

    if(nombre == 0):
        print("Vide")
    else:
      #  print(nombre)
        if(nombre % 2 == 0):
          #  print("pair")
            valeur = sorted(valeur)
            resultat = ((valeur[int(len(valeur) / 2 - 1)] + valeur[int(len(valeur) / 2 )]) / 2)
            print('{:.2f}'.format(resultat))

        else:
            valeur = sorted(valeur)
            resultat = (valeur[int(len(valeur) / 2)])
            print('{:.2f}'.format(resultat))

  
 


