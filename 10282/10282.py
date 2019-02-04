import sys

lines = sys.stdin.readlines()

verif = 0
dictionnary = {}

for line in lines:

        temp = list(map(str, line.split()))
        
        

        if verif == 1:
                if temp[0] in dictionnary:
                        print(dictionnary.get(temp[0]))
                else:
                        print("eh")        

        
        if not temp :
                verif = 1

        if verif == 0:
                dictionnary[temp[1]] = temp[0]

