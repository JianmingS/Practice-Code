#include <iostream>
#include <queue>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int MAX_NUM = 10005;
bool visited[MAX_NUM];
bool isPrime[MAX_NUM];
string source;
string purpose;
int ans = -1;

class Node {
	public:
		string num;
		int layer;
		Node(string _num, int _layer) {
			num = _num;
			layer = _layer;
		}
};

void update_prime() {
	for (int i=2; i!=MAX_NUM; ++i) {
		if (!isPrime[i]) {
			continue;
		}
		int cnt = 2;
		while (cnt * i <= MAX_NUM) {
			isPrime[cnt * i] = false;
			cnt += 1;
		}
	}
}

void solve(string source, string purpose) {
	queue<Node> que;
	que.push(Node(source, 0));
	visited[atoi(source.c_str())] = true;
	while (!que.empty()) { 
		Node nd = que.front();
		que.pop();
		if (nd.num == purpose) {
			ans = nd.layer;
			return;
		}
		for (int i = 0; i!=4; ++i) {
			char digit = nd.num[i];
			for (int j=0; j!=10; ++j) {
				if ((i==0 && j==0) || (j == (int)(digit - '0'))) {
					continue;
				}			
				string next = nd.num;
				next[i] = (char)('0' + j);
				if (!isPrime[atoi(next.c_str())] || visited[atoi(next.c_str())]) {
					continue;
				}
				que.push(Node(next, nd.layer+1));
				visited[atoi(next.c_str())] = true;
			}
		}
	}
}

int main() {
	// freopen("in", "r", stdin);
	int n;
	cin >> n;
	memset(isPrime, true, sizeof(isPrime));
	update_prime();
	for (int i=0; i!=n; ++i) {
		ans = -1;
		memset(visited, false, sizeof(visited));
		cin >> source >> purpose;
		solve(source, purpose);
		if (ans != -1) {
			cout << ans << endl;
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
