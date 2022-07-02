#Filename : VOTERSDI.py

n1, n2, n3 = map(int, input().split())

#Count number of occurences in a map

d = {}

res = []

for i in range(n1+n2+n3):
    n = int(input())
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
print(d)

#Keys with value >= 2 

for k in d:
    if d[k] >= 2:
        res.append(k)

#Print output as required

print(len(res))

res.sort()
for n in res:
    print(n)








