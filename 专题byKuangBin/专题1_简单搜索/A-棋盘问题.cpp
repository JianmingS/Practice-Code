#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
const int max_n = 8;

string chessboard[max_n];
int n, k;
int ans = 0;

void solve(int row, int used_col, int selected_cnt) {
	for (int col=0; col!=n; ++col) {
		if (chessboard[row][col]!='#' || (used_col & (1<<col))) {
			continue;
		}
		if (selected_cnt + 1 == k) {
			ans += 1;
			continue;
		}
		for (int i=row+1; i<n; ++i) {
			solve(i, used_col | (1<<col), selected_cnt + 1);
		}
	}
}

int main(){
//	freopen("in", "r", stdin);	
	while (cin >> n >> k && !(n==-1&&k==-1)) {
		ans = 0;
		string row;
		for (int i=0; i!=n; ++i){
			cin >> row;
			chessboard[i] = row;
		}
		for (int i=0; i<=(n-k); ++i) {
			solve(i, 0, 0);
		}
		cout << ans << endl; 
	}
}
