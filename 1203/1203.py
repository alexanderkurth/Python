import sys
import heapq

lines = sys.stdin.readlines()
if lines[-1] == ' ': del lines[-1]

heap = []
tab = []
result = 0
i = 100

for line in lines:
    
    temp = list(map(str,line.split()))

    if(temp[0] == 'Register'):
           # heapq.heappush(heap, (temp[2],temp[1]))
            tab.append((temp[2],temp[1]))

valeur = int(temp[0])
print(tab)


while valeur != result :

    for element in tab:
        i = i+1
        

    if(i % int(tab[0][0]) == 0):
        print(tab[0][1])
        result = result + 1

    if(i % int(tab[1][0]) == 0):
        print(tab[1][1])
        result = result + 1

    i = i +100



    