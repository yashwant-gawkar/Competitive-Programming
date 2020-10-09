#include<bits/stdc++.h>
using namespace std;


#define ff              first
#define ss              second
#define int             long long
#define pb              push_back
#define mp              make_pair
#define pii             pair<int,int>
#define vi              vector<int>
#define mii             map<int,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define setbits(x)      __builtin_popcountll(x)
#define zrobits(x)      __builtin_ctzll(x)
#define mod             1000000007
#define inf             1e18
#define ps(x,y)         fixed<<setprecision(y)<<x
//#define rv(v,n)           while(n){int x;cin>>x; v.push_back(x);n=n-1;}
#define mk(arr,n,type)  type *arr=new type[n];
#define w(x)            int x; cin>>x; while(x--)
#define fo(x,s,n)       for(int x=s;x<n;x++)
#define deb(x)          cout<<#x<<"="<<x<<'\n';
/*

auto soe(int a,int n){
	int ret[n+1];
	fill_n(ret,n+1,1);

	ret[0]=0;
	ret[1]=0;

	FOR(i,2,n+1){
		if (ret[i]==1){
			int j=i;
			while(j*i<=n){
				ret[j*i]=0;
				++j;

			}
		}
	}*/



template<typename...T>
void read(T&... args) {
	((cin >> args), ...);
}

template<typename...T>
void write(T ... args) {
	((cout << args << ' '), ...);
}

void solve() {
	int n, a, b;
	read(n);
	vi arr(3);
	for (int&i : arr) {
		scanf("%d", &i);
	}
	deb(arr[0]);



}

int32_t main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	w(x) {
		solve();
	}




	return 0;

}