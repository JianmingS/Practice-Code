#include <iostream>
#include <queue>
#include <cstring>
using namespace std;
const int MIN_NUM = 0;
const int MAX_NUM = 100000;
int visited[MAX_NUM + 10];


struct Node {
	Node (int num, int step): num(num), step(step){}
	int num;
	int step;
};


int solve(int n, int k) {
	queue<Node> que;
	visited[n] = 1;
	que.push(Node(n, 0));
	while (!que.empty()) {
		Node nd = que.front();
		if (nd.num == k) {
			return nd.step;
		}
		que.pop();
		for (int i=0; i!=3; ++i) {
			int num= nd.num;
			switch (i) {
				case 0: {
					num -= 1;
					break;
				}
				case 1: {
					num += 1;
					break;
				}
				case 2: {
					num *= 2;
					break;
				}
				default:{}
			}
			if (num < MIN_NUM || num > MAX_NUM || visited[num]) {
				continue;
			}
			que.push(Node(num, nd.step + 1));
			visited[num] = 1;
		}
	}
	return -1;
}


int main() {
//	freopen("in", "r", stdin);
	int n, k;
	while (cin >> n >> k) {
		memset(visited, 0, sizeof(visited));
		cout << solve(n, k) << endl;
	}	
}