/*
88418 paths between the upper left & lower left corners in a 7x7 grid
Each path corresponds to a 48 char description [U, D, L, R, ?]
Calculate the number of paths that match your description
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long

string s;
bool vis[7][7];
int ans;

bool e(int i, int j) {
    return i>=0&&i<7&&j>=0&&j<7&&!vis[i][j];
}

void dfs(int i, int j, int a = 0) {
    if(a==6&&j==6){
        if(a==48){
            ++ans;
        }
        else{
            return;
        }
    }

    vis[i][j] = 1;

    // move left
    if(s[a]=='?' || s[a]=='L') {
        if(j&&!vis[i][j-1]) { //j>=1 for left movement to happen
            if(!(!e(i,j-2)&&e(i-1,j-1)&&e(i+1, j-1)))
            dfs(i, j-1, a+1);
        }
    }

    // move right
    if(s[a]=='?' || s[a] == 'R') {
        if(j<6&&!vis[i][j+1]) {//j must be in range(0, 6) for right move to happen
            if(!(!e(i, j+2)&&e(i+1, j+1)&&e(i-1, j+1)))
            dfs(i, j+1, a+1);
        }
    }

    //move up
    if(s[a]=='?'|| s[a] == 'U') {
        if(i&&!vis[i-1][j]) {
            if(!(!e(i-2, j)&&e(i-1, j-1)&&e(i-1, j+1)))
            dfs(i-1, j, a+1);
        }
    }

    //move down
    if(s[a] == '?' || s[a] == 'D') {
        if(i<6&&!vis[i+1][j]) {
            if(!(!e(i+2, j)&&e(i+1, j-1)&&e(i+1, j+1)))
            dfs(i+1, j, a+1);
        }
    }

    vis [i][j] = 0;
}

int main() {
    cin >> s;
    dfs(0, 0);
    cout << ans;
}