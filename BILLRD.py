#Filename : BILLRD.py

t = int(input())

for t in range(int(input())):
    n ,k, x, y = map(input().split())
    if x == y:
        print(n,n)
    else:
        l = []
        if x < y:
            poc = [[x+n-y, n],[n, n-y+x],[y-x, 0],[0, y-x]]
            if x < y:
                poc = []
                pass
            else:
                poc = [[n, y+n-x], [y+n-x,n],[0, x-y], [x-y, 0]]
        fp = poc[(k-1)%4]
        print(fp[0], fp[1])











