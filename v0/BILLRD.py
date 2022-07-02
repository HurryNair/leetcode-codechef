#Filename : BILLRD.py

#Accept inputs
for t in range(int(input())):
    n ,k, x, y = map(int,input().split())
    
    #Check if ball is on 
    #a coordinate that would
    #pot the ball
    
    if x == y:
        print(n,n)
    
    else:
        #List all 4 points that 
        #the ball would collide
        poc = []
        
        
        if x < y:
            poc = [[x+n-y, n],[n, n-y+x],[y-x, 0],[0, y-x]]
        
        else:
            poc = [[n, y+n-x], [y+n-x,n],[0, x-y], [x-y, 0]]
        
        # k%4 = k since the ball rotates within these points
        fp = poc[(k-1)%4]
        
        print(fp[0], fp[1])
