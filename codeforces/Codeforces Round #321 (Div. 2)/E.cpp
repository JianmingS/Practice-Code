/*
E. Kefa and Watch
*/

#define DEBUG
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int n, m, k;
vector<vector<int>> opt_vec;
string number;

void solve() {
    
}

int main()
{
#ifdef DEBUG
    freopen("in", "r", stdin);
#endif
    cin >> n >> m >> k;
    cin >> number;
    for (int i=0; i<(m+k); ++i) {
        vector<int> opt(4);
        for (int j=0; j<4; ++j) {
            cin >> opt[j];
        }
    }
    solve();
}
