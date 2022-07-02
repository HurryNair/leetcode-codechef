"""
Chef found a matrix A with N rows (numbered 1 through N) and M columns (numbered 1 through M), where for each row r and column c, the cell in row r and column c (denoted by (r,c)) contains an integer Ar,c.

This matrix has two interesting properties:

The integers in each row form a non-decreasing sequence, i.e. for each valid i, Ai,1≤Ai,2≤…≤Ai,M.
The integers in each column also form a non-decreasing sequence, i.e. for each valid j, A1,j≤A2,j≤…≤AN,j.
A K-worthy submatrix is a square submatrix of A, i.e. a submatrix with l rows and l columns, for any integer l, such that the average of all the integers in this submatrix is ≥K.

Chef wants you to find the number of K-worthy submatrices of A.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains three space-separated integers N, M and K.
N lines follow. For each valid i, the i-th of these lines contains M space-separated integers Ai,1,Ai,2,Ai,3,…,Ai,M.
Output
For each test case, print a single line containing one integer ― the number of K-worthy submatrices of A.

Constraints
1≤T≤10
1≤N⋅M≤106
N≤M
0≤K≤109
0≤Ar,c≤109 for each valid r,c
the sum of N⋅M over all test cases does not exceed 106
Subtasks
Subtask #1 (15 points): the sum of N⋅M over all test cases does not exceed 103
Subtask #2 (25 points): the sum of N⋅M over all test cases does not exceed 4⋅105
Subtask #3 (60 points): original constraints

Example Input
1
3 3 4
2 2 3
3 4 5
4 5 5
Example Output
7
Explanation
Example case 1: The following are the seven 4-worthy submatrices:

[3445] with average 4; this matrix occurs only once
[4555] with average 4.75; this matrix also occurs only once
[4] with average 4; we find this matrix twice in A
[5] with average 5; we find this matrix 3 times in A
"""

#include <iostream>
using namespace std;

// void() funciton implementation

/*
1	2	3	4	5	6
3	4	5	6	7	8
9	10	11	12	13	14
10	11	12	13	14	15
15	16	17	18	19	20
*/

void solve()
{
    long long n,m,k;
    cin>>n>>m>>k;

    double arr[n+1][m+1];

    for(long long i=0;i<=n;i++)
    {
        for(long long j=0;j<=m;j++)
        {
            // Zero stuff row 0 & column 0 so as it avoid list 
            // index out of bounds error while retrieving original element

            if(i==0||j==0)
              arr[i][j]=0;
            else
              cin>>arr[i][j];
        }
    }

    // At this point we have a 0-stuffed row0 & 0 stuffed column0 added


    for(long long i=0;i<=n;i++)
    {
        double prev=0;
        for(long long j=0;j<=m;j++)
        {
            arr[i][j]+=prev;
            prev=arr[i][j];
        }
    }

    /*
    Add items rowise
    1	3	6	10	15	21
    3	7	12	18	25	33
    9	19	30	42	55	69
    10	21	33	46	60	75
    15	31	48	66	85	105
    */

    for(long long i=0;i<=m;i++)
    {
        double prev=0;
        for(long long j=0;j<=n;j++)
        {
            arr[j][i]+=prev;
            prev=arr[j][i];
        }
        
    }

    /*
    Add items column wise
    1	3	6	10	15	21
    4	10	18	28	40	54
    13	29	48	70	95	123
    23	50	81	116	155	198
    38	81	129	182	240	303
    */

    /*
    Zero stuffed
    0	0	0	0	0	0	0
    0	1	3	6	10	15	21
    0	4	10	18	28	40	54
    0	13	29	48	70	95	123
    0	23	50	81	116	155	198
    0	38	81	129	182	240	303
    */

    long long m_min = min(m,n);
    long long ans = 0;
    
    for(long long u=1;u<=m_min;u++)
    {
        for(long long i=u;i<=n;i++)
        {
            for(long long j=u;j<=m;j++)
            {
                if((arr[i][j]+arr[i-u][j-u]-arr[i][j-u]-arr[i-u][j])/(u*u)>=k)
                  ans++;
            }
        }
    }
    cout<<ans<<endl;
}

// Driver code

int main() {
	
	long long t;
	cin>>t;
	
	while(t--)
	{
	    solve();
	}
	return 0;
}