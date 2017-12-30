/*
    C. GCD Table
    g++ -std=c++11 C.cpp
*/
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <functional>
#include <map>
#include <vector>
using namespace std;

int n;
vector<int> numbers;
map<int, int> num_to_cnt;
vector<int> ans;

int gcd(int x, int y)
{
    return (0 == x)? y : gcd(y%x, x);
}

void solve()
{
    sort(numbers.begin(), numbers.end(), greater<int>());
    for (int i = 0; i != numbers.size(); ++i)
    {
        if (num_to_cnt[numbers[i]] != 0)
        {
            num_to_cnt[numbers[i]] -= 1;
            for (int j = 0; j != ans.size(); ++j)
            {
                num_to_cnt[gcd(ans[j], numbers[i])] -= 2;
            }
            ans.push_back(numbers[i]);
        }
    }

    for (auto i : ans)
    {
        cout << i << " ";
    }
    cout << endl;
}


int main()
{
    //freopen("in", "r", stdin);
    cin >> n;
    for (int i = 0; i != (n*n); ++i)
    {
        int tmp;
        cin >> tmp;
        numbers.push_back(tmp);
        if (num_to_cnt.end() == num_to_cnt.find(tmp))
        {
            num_to_cnt[tmp] = 1;
        }else
        {
            num_to_cnt[tmp] += 1;
        }
    }
    solve();
    return 0;
}
