"""
Chef has three socks in his drawer. Each sock has one of 10 possible colours, which are represented by integers between 1 and 10. Specifically, the colours of the socks are A, B, and C.

Chef has to wear two socks which have the same colour. Help Chef find out if that is possible or not.

Input
The first and only line of the input contains three space-separated integers A, B and C.

Output
Print a single line containing the string "YES" if it is possible for Chef to wear two socks with the same colour or "NO" if it is impossible (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints
1≤A,B,C≤10
Subtasks
Subtask #1 (100 points): original constraints

Example Input 1
5 4 3
Example Output 1
NO
"""

# cook your dish here

# Accept input
# Split chars & convert them into strings

sock_list = map(int, input().split())
sock_list = sorted(sock_list)

sock_count = {}

for sock in sock_list:
    if sock not in sock_count:
        sock_count[sock] = 1
    else:
        print("YES")
        break
else:
    print("NO")