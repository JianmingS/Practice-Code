/*
B. Robot's Task
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int n = 0;
vector<int> pieces;
vector<bool> isVisited;


int minNumOfChanges()
{
    int minNum = 0;
    int visNum = 0;

    while (visNum < n)
    {
        for (int i = 0; i != n; ++i)
        {
            if (!isVisited[i])
            {
                if (visNum >= pieces[i])
                {
                    ++visNum;
                    isVisited[i] = true;
                }
            }
        }
        if (visNum == n)
        {
            break;
        }
        ++minNum;

        for (int i = n - 1; i >= 0; --i)
        {
            if (!isVisited[i])
            {
                if (visNum >= pieces[i])
                {
                    ++visNum;
                    isVisited[i] = true;
                }
            }
        }
        if (visNum == n)
        {
            break;
        }
        ++minNum;
    }

    return minNum;
}


int main()
{
    // freopen("in", "r", stdin);
    cin >> n;
    for (int i = 0; i != n; ++i)
    {
        int tmp = 0;
        cin >> tmp;
        pieces.push_back(tmp);
        isVisited.push_back(false);
    }

    int minNum = minNumOfChanges();

    cout << minNum << endl;
    return 0;
}
