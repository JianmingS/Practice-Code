#include <iostream>
#include <string>
#include <cstdio>
#include <climits>
#include <cmath>
#include <cstring>
#include <queue>
using namespace std;

const int max_size = 35;
int L, R, C;
string dungeon[max_size][max_size];
int visited[max_size][max_size][max_size];
int step[][3] = {
	{1, 0, 0}, {-1, 0, 0},
	{0, 1, 0}, {0, -1, 0},
	{0, 0, 1}, {0, 0, -1}
};
struct node { int x, y, z, t; };
node s, e;


int solve() {
	queue<node> que;
	que.push(s);
	visited[s.x][s.y][s.z] = 1;
	int ans = 0;
	while (!que.empty()) {
		node current_nd = que.front();
		que.pop();
		node next_nd;
		for (int i=0; i!=6; ++i) {
			int _x = current_nd.x + step[i][0];
			int _y = current_nd.y + step[i][1];
			int _z = current_nd.z + step[i][2];
			if ((_x<0 || _x>=L) || (_y<0 || _y>=R) || (_z<0 || _z>=C) || dungeon[_x][_y][_z]=='#' || visited[_x][_y][_z]) {
				continue;
			}
			if (_x==e.x && _y==e.y && _z==e.z) {
				return current_nd.t + 1;
			}
			next_nd.x = _x;
			next_nd.y = _y;
			next_nd.z = _z;
			next_nd.t = current_nd.t + 1;
			visited[next_nd.x][next_nd.y][next_nd.z] = 1;
			que.push(next_nd);
		}
	}
	return ans;
}


int main() {
	//freopen("in", "r", stdin);
	while (cin>>L>>R>>C && !(L==0 && R==0 && C==0)) {
		memset(visited, 0, sizeof(visited));
		for (int i=0; i!=L; ++i) {
			for (int j=0; j!=R; ++j) {
				cin >> dungeon[i][j];
				for (int k=0; k!=dungeon[i][j].size(); ++k) {
					if (dungeon[i][j][k] == 'S') {
						s.x = i;
						s.y = j;
						s.z = k;
						s.t = 0;
					}
					if (dungeon[i][j][k] == 'E') {
						e.x = i;
						e.y = j;
						e.z = k;
					}
				}

			}			
		}
		int ans = solve();
		if (!ans) {
			cout << "Trapped!" << endl;
		} else {
			cout << "Escaped in " << ans << " minute(s)." << endl;
		}
	}
	return 0;
}