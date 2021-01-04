#Filename : FAIRELCT.py

t = int(input())

for i in range(t):
    
    #Accept inputs
    n, m = map(int,input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    #Max_swaps that can be performed is min(n,m)
    max_swaps = min(n, m)

    #Function to calculate total number of votes
    def total_votes(a):
        votes = 0
        for i in range(len(a)):
            votes += a[i]
        return votes
    
    #Calculate total number of votes before rigging
    total_votes_a = total_votes(a)
    total_votes_b = total_votes(b)

    for i in range(max_swaps):
        tmp = min(a)
        tmp2 = max(b)

        a.remove(tmp)

        a.append(tmp2)
        b.remove(tmp2)

        b.append(tmp)

        total_votes_a -= tmp
        total_votes_a += tmp2
        total_votes_b -= tmp2
        total_votes_b += tmp

        if total_votes_a > total_votes_b:
            print(i+1)
            break
        
        elif i == max_swaps - 1:
            print(-1)
            break


        
    

