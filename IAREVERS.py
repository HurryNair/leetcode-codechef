#Filename : IAREVERS.py

n = int(input())

los = []

for i in range(n):
    los.append(input())

for i in range(n-1, -1, -1):
    s = ' '.join([''.join(x) for x in los[i].split()[::-1] if x not in ["'", ":", ";", '.', " ", ","]])
    print(s.replace("'", "").replace(":", "").replace(";", "").replace(".", "").replace(" ", " ").replace(",", ""))
