#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef struct node {
	node* children[26];
	int cnt = 0;


} Trie;
Trie* root;
const int N = 1e5 + 3;
int n, k;
string a[N];

void insert(string& s) {
	Trie*curr = root;

	for (int i = 0; i < s.size(); i++) {
		char ch = s[i];
		int req = ch - 'A';
		if (!curr->children[req])
			curr->children[req] = new Trie();
		curr = curr->children[req];


	}
	curr->cnt++;



}
int ans = 0;
void dfs(Trie* cur, int lvl) {

	for (int i = 0; i < 26; i++) {
		if (cur->children[i]) {
			dfs(cur->children[i], lvl + 1);
			cur->cnt += cur->children[i]->cnt;
		}
	}
	while (cur->cnt >= k) {
		cur->cnt -= k;
		ans += lvl;

	}


}


int32_t main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		ans = 0;
		cin >> n >> k;
		root = new Trie();
		for (int i = 1; i <= n; i++) {
			cin >> a[i];
			insert(a[i]);

		}
		dfs(root, 0);
		cout << "Case #" << i << ": " << ans << '\n';


	}
	return 0;
}