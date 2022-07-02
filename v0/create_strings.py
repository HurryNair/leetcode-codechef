"""
Given a string your task is to create all possible strings that can be created using its characters
"""

# Approach
# Calculate every possible permutation of the given string
# Print it

# next_permutation cpp built-in

"""
int main() {
    string s;
    cin >> s;
    sort(s.begin(), s.end());
    vector<string> ans;(
    do{
        ans.push_back(s);
    } while(next_permutation(s.begin(), s.end()))
    cout << ans.size() << "\n";
    for(string a : ans)
        cout << a << "\n";
}

"""

