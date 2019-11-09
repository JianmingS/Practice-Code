/*
题意：
给出一个数n，求一个数m，只由0和1组成，且是n的倍数（存在多个可任意输出）

解决：
（1）避免大数
取余公式
(a+b)%n = (a%n + b%n)%n
(a*b)%n = ((a%n)*(b%n))%n

应用方法：
从x开始，接下来可能的值是(x*10)、(x*10 + 1)，以此类推。可通过检查每一个值%m是否为0，判断当前值是否为答案。
(x*10)%n <=> ((x%n)*10)%n
(x*10+1)%n <=> ((x*10)%n + 1)%n <=> ((x%n)*10 + 1)%n 765

（2）剪枝
已经遍历过的值，无需再次遍历   
*/


#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <queue>
using namespace std;
int n;
int visited[210];

struct Node {
    int mod;
    string val;
    
    Node(int _mod, string _val) {
        mod = _mod;
        val = _val;
    };
};

void solve() {
    queue<Node> que;
    que.push(Node(1, "1"));
    visited[1] = 1;
    while (!que.empty()) {
        Node nd = que.front();
        que.pop();
        if (nd.mod%n==0) {
            cout << nd.val << endl;
            return;
        }
        for (int i = 0; i!=2; ++i)  {
            int mod = i? (nd.mod*10 + 1)%n : (nd.mod*10)%n;
            if (visited[mod]) {
                continue;
            }
            string val = i? (nd.val + "1") : (nd.val + "0");
            que.push(Node(mod, val));
            visited[mod] = 1;
        }
    }
}

int main() {
//    freopen("in", "r", stdin);
    while (cin>>n && n) {
        memset(visited, 0, sizeof(visited));
        solve();
    }
    return 0;
}
