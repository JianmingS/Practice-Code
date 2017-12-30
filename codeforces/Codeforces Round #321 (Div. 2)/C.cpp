/*
 C. Kefa and Park
 DFS
 注意：
 1、保存树结构方式
 2、判断叶子结点方式
 */

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

const int max_n = 100010;

int n, m;
map<int, vector<int>> Tree;
int status[max_n];
vector<bool> used(max_n, false);

int ans = 0;


void num_of_rest(int root, int cst_cnt)
{
    used[root] = true;
    
    if (cst_cnt > m)
    {
        return;
    }
    
//    判断是否是叶子结点
    bool is_leaf = true;
    for (int node : Tree[root])
    {
        if (used[node])
        {
            continue;
        }
        
        if (is_leaf)
        {
            is_leaf = false;
        }
        
        if (1 == status[node])
        {
            num_of_rest(node, cst_cnt + 1);
        }else
        {
            num_of_rest(node, 0);
        }
    }
    if (is_leaf)
    {
        ans += 1;
    }
}


int main()
{
//    freopen("in", "r", stdin);
    cin >> n >> m;
    for (int i = 0; i != n; ++i)
    {
        cin >> status[i];
    }
    int father, child;
    while(cin >> father >> child)
    {
        --father;
        --child;
        Tree[father].push_back(child);
        Tree[child].push_back(father);
    }
    num_of_rest(0, (1 == status[0])? 1:0);
    cout << ans << endl;
}
