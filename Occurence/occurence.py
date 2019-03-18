import sys
import collections

lines = sys.stdin.readlines()
if lines[-1] == ' ':del lines[-1]

dictionnary = {}
result = ""

for line in lines:
    temp = list(map(str, line.split()))
  #  print(temp)

    for i in range(0, len(temp)):
        temp[i] = temp[i].rstrip(',')
        temp[i] = temp[i].rstrip('.')
        temp[i] = temp[i].lower()

        if temp[i] not in dictionnary:
            dictionnary[temp[i]] = 1
        else:
            dictionnary[temp[i]] += 1
        
dictionnary = collections.OrderedDict(sorted(dictionnary.items(), key=lambda t: t[0]))    

for key,value in dictionnary.items():
    if value == max(dictionnary.values()):
        result += (' ' + key)

print(str(max(dictionnary.values())) + result)