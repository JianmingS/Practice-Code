#include <iostream>
#include <cstring>
#include <climits>

using namespace std;
int M, N;
const int MAX_LEN = 20;
int source[MAX_LEN][MAX_LEN];
int ans[MAX_LEN][MAX_LEN];
int tmp_flip[MAX_LEN][MAX_LEN];
int step[5][2] = {{0, -1}, {-1, 0}, {0, 0}, {0, 1}, {1, 0}};


int get_color(int x, int y) {
	int val = source[x][y];
	for (int i=0; i!=5; ++i) {
		int new_x = x + step[i][0];
		int new_y = y + step[i][1];
		if (x>=0 && x<M && y>=0 && y<N) {
			val += tmp_flip[new_x][new_y];
		}
	}
	return val%2;
}


int flip() {
	for (int i=1; i!=M; ++i) {
		for (int j=0; j!=N; ++j) {
			if (get_color(i-1, j) != 0) {
				tmp_flip[i][j] = 1;
			}
		}
	}
	for (int j=0; j!=N; ++j) {
		if (get_color(M-1, j) != 0) {
			return INT_MAX;
		}
	}
	int ret = 0;
	for (int i=0; i!=M; ++i) {
		for (int j=0; j!=N; ++j) {
			ret += tmp_flip[i][j];
		}
	}
	return ret;
}
	

void solve() {
	int flip_cnt = INT_MAX;
	for (int i=0; i!=(1<<N); ++i) {
		memset(tmp_flip, 0, sizeof(tmp_flip));
		for (int j=0; j!=N; ++j) {
			tmp_flip[0][N-(j+1)] = (i>>j) & 1;
		}
		int cnt = flip();
		if (cnt < flip_cnt) {
			flip_cnt = cnt;
			memcpy(ans, tmp_flip, sizeof(tmp_flip));
		}
	}
	if (flip_cnt == INT_MAX) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		for (int i=0; i!=M; ++i) {
			for (int j=0; j!=N; ++j) {
				cout << ans[i][j] << ((j!=N-1)? " " : "\n");
			}
		}
	}		
}

int main() {
	//freopen("in", "r", stdin);
	cin >> M >> N;
	for (int i=0; i!=M; ++i) {
		for (int j=0; j!=N; ++j) {
			cin >> source[i][j];
		}
	}
	solve();
	return 0;
}