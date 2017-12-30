/*
 * Codeforces Round #323 (Div. 2)
 * D. Once Again...
 *
 * 1、T<=n
 * DP求最长递增子序列nlog(n)，n<=100，可接受
 *
 * 2、T>n
 * n*n最长递增子序列一定是数组[a1,a2,,,,an]
 * 那么T>n的时候，在n*n的基础上，每增加一个数组，LIS增加的长度是max(cnt(ai))
 * 也即：一个数组中相同数值出现的最多次数
 * 也即：ans = LIS(n*n) + (T-n)*max(cnt(ai))
 *
 * */

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

const int maxN = 310;


int n, T, T_ForLIS;
vector<int> vecArray;
vector<int> dp;
vector<int> cntOfNum;


int getLisLen()
{
    dp.assign(T_ForLIS, 0);

    int lisLen = 0;
    for (vector<int>::iterator it = vecArray.begin(); it != vecArray.end(); ++it)
    {
        int pos = upper_bound(dp.begin(), dp.begin() + lisLen, *it) - dp.begin();
        dp[pos] = *it;
        // cout << pos << ": " << dp[pos] << endl;
        lisLen = max(lisLen, pos + 1);
    }
    return lisLen;

}

int solve()
{
    int ans = getLisLen();
    if (T > n)
    {
        ans += (T-n)*(*max_element(cntOfNum.begin(), cntOfNum.end()));
    }
    return ans;
}


int main()
{
    // freopen("in", "r", stdin);

    cntOfNum.assign(maxN, 0);

    cin >> n >> T;
    for (int i = 0; i != n; ++i)
    {
        int tmp;
        cin >> tmp;
        vecArray.push_back(tmp);
        ++cntOfNum[tmp];
    }

    if (T > n)
    {
        T_ForLIS = n*n; 
    }else
    {
        T_ForLIS = T*n;
    }

    for (int i = n; i != T_ForLIS; ++i)
    {
        vecArray.push_back(vecArray[i - n]);
    }

    cout << solve() << endl;

    return 0;
}
