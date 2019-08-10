/*
D. Kefa and Dishes
状态压缩DP
 O((2^n)*(n^2))
 
 转移过程：
    new_status = status|(1<<j);
 
 转移方程：
    dp[new_status][j] = max(dp[new_status][j], dp[status][i] + val[j] + extra_val[i][j]);
 
 答案：
    所有选择数量达到m的状态的最大值
 
 参考：
    https://blog.csdn.net/u013371163/article/details/60469234
 */

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

const int max_n = 20;
long long dp[1<<max_n][max_n], ans;
int val[max_n];
int extra_val[max_n][max_n];
int n, m, k;

long long solve() {
    ans = 0;
    for (int i = 0; i != n; ++i) {
        dp[1<<i][i] = val[i];
        ans = max(ans, dp[1<<i][i]);
    }
    // 枚举所有状态
    for (int status = 0; status != (1<<n); ++status) {
        int cnt = 0;
        // 在已选定的状态中，选一道菜i在j前面吃
        // （也即：将i认为是status状态时的最后一道菜）
        for (int i = 0; i != n; ++i) {
            if (0 == (status&(1<<i))) {
                continue;
            }
            ++cnt;
            // 从未选定的菜中选一道j出来，在i后面吃
            for (int j = 0; j != n; ++j) {
                if (status&(1<<j)) {
                    continue;
                }
                int new_status = status|(1<<j);
                dp[new_status][j] = max(dp[new_status][j], dp[status][i] + val[j] + extra_val[i][j]);
            }
        }
        // status已选了m道菜，m道菜中任意一个为最后一道菜，从中选择最大的
        if (cnt == m) {
            for (int i = 0; i != n; ++i) {
                if (status & (1<<i)) {
                    //cout << status << " " << i << "---" << dp[status][i] << endl;
                    ans = max(ans, dp[status][i]);
                }
            }
        }
    }
    return ans;
}

int main()
{
    //freopen("in", "r", stdin);
    cin >> n >> m >> k;
    for (int i=0; i!=n; ++i)
    {
        cin >> val[i];
    }
    for (int j=0; j!=k; ++j)
    {
        int x, y, c;
        cin >> x >> y >> c;
        extra_val[x-1][y-1] = max(extra_val[x-1][y-1], c);
    }
    cout << solve() << endl;
}
