# NOTIME.py
#! /usr/bin/python3

'''
Only x hours are left for the March Long Challenge and Chef is only left with the last problem unsolved. However, he is sure that he cannot solve the problem in the remaining time. From experience, he figures out that he needs exactly H hours to solve the problem.

Now Chef finally decides to use his special power which he has gained through years of intense yoga. He can travel back in time when he concentrates. Specifically, his power allows him to travel to N different time zones, which are T1,T2,…,TN hours respectively behind his current time.

Find out whether Chef can use one of the available time zones to solve the problem and submit it before the contest ends.

Example Input 1
2 5 3
1 2
Example Output 1
YES
Explanation
Chef already has 3 hours left. He can go to the 2-nd time zone, which is 2 hours back in time. Then he has a total of 3+2=5 hours, which is sufficient to solve the problem.
'''

# Accept inputs 
N, H, x = map(int, input().split())
arr = list(map(int, input().split()))

# Sort the time zones in decending order 
# to find impossible scenarios in O(1)
sorted(arr, reversed = True)

if x + arr[0] >= H:
    print("YES")
    
else:
    print("NO")

