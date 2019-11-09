//
//  main.cpp
//  Cpp
//
//  Created by Jianming Shi on 2019/9/22.
//  Copyright © 2019 Jianming Shi. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
int N = 0;
int C = 0;
string target_s12 = "";
vector<string> visited;

int solve(string s1, string s2, int cnt) {
	string s12 = "";
	for (int i=0; i!=s1.length(); ++i) {
		s12 += s2[i];
		s12 += s1[i];
	}
	if (s12 == target_s12) {
		return cnt;
	}
	if (find(visited.begin(), visited.end(), s12) != visited.end()) {
		return -1;
	}
	visited.push_back(s12);
	return solve(s12.substr(0, C), s12.substr(C, C), cnt + 1);
}

int main() {
	freopen("in", "r", stdin);
	cin >> N;
	string s1, s2;
	for (int i=0; i!=N; ++i) {
		cin >> C;
		cin >> s1;
		cin >> s2;
		cin >> target_s12;
		cout << i+1 << " " << solve(s1, s2, 1) << endl;
		visited.clear();
	}
	return 0;
}
