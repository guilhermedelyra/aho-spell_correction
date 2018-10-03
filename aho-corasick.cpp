#include <vector>
#include <string>
#include <queue>
#include <string.h>
#include <iostream>
#include <locale>
#include <codecvt>
#include <map>
#include "aho.h"

using namespace std;

int buildMatchingMachine(const vector<string> & words, int (&f)[310], int (&g)[310][224], int (&out)[310]) {

	memset(out, 0, sizeof out);
	memset(f, -1, sizeof f);
	memset(g, -1, sizeof g);
	int states = 1;
	const int MAXC = 224; 
	const int MAXS = 6 * 50 + 10; 

	wstring_convert<codecvt_utf8_utf16<char16_t>, char16_t> utf16conv;

	for (int i = 0; i < words.size(); ++i) {
		u16string utf16 = utf16conv.from_bytes(words[i]);
		const u16string &keyword = utf16;
		int currentState = 0;
		for (int j = 0; j < keyword.size(); ++j) {
			int c = keyword[j] - ' ';
			if (g[currentState][c] == -1) {
				g[currentState][c] = states++;
			}
			currentState = g[currentState][c];
		}
		out[currentState] |= (1 << i);
	}

	for (int c = 0; c < MAXC; ++c) {
		if (g[0][c] == -1) {
			g[0][c] = 0;
		}
	}

	queue<int> q;
	for (int c = 0; c < MAXC; ++c) {
		if (g[0][c] != -1 and g[0][c] != 0) {
			f[g[0][c]] = 0;
			q.push(g[0][c]);
		}
	}

	while (q.size()) {
		int state = q.front();
		q.pop();
		for (int c = 0; c < MAXC; ++c) {
			if (g[state][c] != -1) {
				int failure = f[state];
				while (g[failure][c] == -1) {
					failure = f[failure];
				}
				failure = g[failure][c];
				f[g[state][c]] = failure;

				out[g[state][c]] |= out[failure]; 
				q.push(g[state][c]);
			}
		}
	}

	return states;
}

int findNextState(int currentState, int nextInput, int (&f)[310], int (&g)[310][224]) {
	int answer = currentState;
	int c = nextInput - ' ';
	while (g[answer][c] == -1) {
		answer = f[answer];
	}
	return g[answer][c];
}

map < string, vector <int> > search (vector<string> keywords, string text) {
	const int MAXC = 224; 
	const int MAXS = 6 * 50 + 10; 
	int f[MAXS];
	int g[MAXS][MAXC];
	int out[MAXS];
	wstring_convert<codecvt_utf8_utf16<char16_t>, char16_t> utf16conv;
	u16string utf16 = utf16conv.from_bytes(text);

	map < string, vector <int> > result;

	buildMatchingMachine(keywords, f, g, out);

	for (int i = 0, currentState = 0; i < utf16.size(); ++i) {
		currentState = findNextState(currentState, (int)utf16[i], f, g);
		if (out[currentState] == 0) continue;
		for (int j = 0; j < keywords.size(); ++j) {
			if (out[currentState] & (1 << j)) {
				int size = utf16conv.from_bytes(keywords[j]).size();
				result[keywords[j]].push_back(i - size + 1);
			}
		}
	}

	return result;
}

// int main(){
// 	vector<string> keywords(4);
// 	string text = "n oi ÿhishers é isso oq vei he is é isso";
// 	keywords[0] = "é isso"; keywords[1] = "she"; keywords[2] = "hers"; keywords[3] = "oi ÿhis";

// 	auto ans = search(keywords, text);

// 	for (auto & [u, v] : ans) {
// 		cout << u << " - ";
// 		for (auto & k : v)
// 			cout << k << " ";
// 		cout << endl;
// 	}
// }