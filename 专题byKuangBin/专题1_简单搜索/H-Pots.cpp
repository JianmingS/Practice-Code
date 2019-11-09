//
//  main.cpp
//  Cpp
//
//  Created by Jianming Shi on 2019/11/10.
//  Copyright © 2019 Jianming Shi. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;
int A, B, C;
bool visited[110][110];

class Node {
public:
    int X;
    int Y;
    vector<string> opt_list;
    Node(int _x, int _y , vector<string> _opt_list) {
        X = _x;
        Y = _y;
        opt_list = _opt_list;
    }
};

void solve() {
    queue<Node> que;
    vector<string> opt_list;
    que.push(Node(0, 0, opt_list));
    while (!que.empty()) {
        Node nd = que.front();
        que.pop();
        if (visited[nd.X][nd.Y]) {
            continue;
        }
        visited[nd.X][nd.Y] = true;
        if (nd.X == C || nd.Y == C) {
            cout << nd.opt_list.size() << endl;
            for (int i=0; i!=nd.opt_list.size(); ++i) {
                cout << nd.opt_list[i] << endl;
            }
            return;
        }
        for (int i=0; i!=6; ++i) {
            switch (i) {
                case 0:
                    if (nd.X < A) {
                        vector<string> opt_list = nd.opt_list;
                        opt_list.push_back("FILL(1)");
                        que.push(Node(A, nd.Y, opt_list));
                    }
                    break;
                case 1:
                    if (nd.X > 0) {
                        vector<string> opt_list = nd.opt_list;
                        opt_list.push_back("DROP(1)");
                        que.push(Node(0, nd.Y, opt_list));
                    }
                    break;
                case 2:
                    if (nd.X!=0 && nd.Y!=B) {
                        vector<string> opt_list = nd.opt_list;
                        opt_list.push_back("POUR(1,2)");
                        int x = (B-nd.Y) >= nd.X ? 0 : nd.X - (B-nd.Y);
                        int y = (B-nd.Y) >= nd.X ? nd.Y + nd.X : B;
                        que.push(Node(x, y, opt_list));
                    }
                    break;
                case 3:
                    if (nd.Y < B) {
                        vector<string> opt_list = nd.opt_list;
                        opt_list.push_back("FILL(2)");
                        que.push(Node(nd.X, B, opt_list));
                    }
                    break;
                case 4:
                    if (nd.Y > 0) {
                        vector<string> opt_list = nd.opt_list;
                        opt_list.push_back("DROP(2)");
                        que.push(Node(nd.X, 0, opt_list));
                    }
                    break;
                case 5:
                    if (nd.Y!=0 && nd.X!=A) {
                        vector<string> opt_list = nd.opt_list;
                        opt_list.push_back("POUR(2,1)");
                        int x = (A-nd.X) >= nd.Y ? nd.X + nd.Y : A;
                        int y = (A-nd.X) >= nd.Y ? 0 : nd.Y - (A-nd.X);
                        que.push(Node(x, y, opt_list));
                    }
                    break;
                default:
                    break;
            }
        }
    }
    cout << "impossible" << endl;
}

int main() {
    //freopen("in", "r", stdin);
    cin >> A >> B >> C;
    solve();
    return 0;
}
