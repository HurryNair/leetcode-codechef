#Filename: DIVTHREE.py

t = int(input())

for i in range(t):
    #map input to variables
    n, k, d = map(int, input().split())

    problems = 0 #total number of problems
    s = input().split()
    
    #Find number of problems available
    for i in range(n):
        problems += int(s[i])

    #Check number of possible contests with available problems
    days_possible = problems//k

    #Compare required days with possible days
    if days_possible >= d:
        print(d)
    elif days_possible < d:
        print(days_possible)
