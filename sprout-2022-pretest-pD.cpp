#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
#define F first
#define S second
#define MP make_pair
#define PB emplace_back
#define fastio ios::sync_with_stdio(0);cin.tie(0)
using namespace std;
using ll = long long;
using pii = pair<ll, ll>;
void debug() {cout << '\n';}
template<class T, class ...U> void debug(T a, U... b){cout << a << ' '; debug(b...);}

ll arr[101][101], n, m, q;

signed main(){
    fastio;
    cin >> n >> m >> q;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++) cin >> arr[i][j];
    }
    string s; int x;
    int lb = 1, rb = m, ub = 1, db = n;
    while(q--){
        cin >> s >> x;
        if(s == "U"){
            ub += x;
            for(int i = 0; i < x; i++){
                for(int j = lb; j <= rb; j++) arr[ub + i][j] += arr[ub - i - 1][j];
            }
        }
        else if(s == "D"){
            db -= x;
            for(int i = 0; i < x; i++){
                for(int j = lb; j <= rb; j++) arr[db - i][j] += arr[db + i + 1][j];
            }
        }
        else if(s == "L"){
            lb += x;
            for(int i = 0; i < x; i++){
                for(int j = ub; j <= db; j++) arr[j][lb + i] += arr[j][lb - i - 1];
            }
        }
        else if(s == "R"){
            rb -= x;
            for(int i = 0; i < x; i++){
                for(int j = ub; j <= db; j++) arr[j][rb - i] += arr[j][rb + i + 1];
            }
        }
        else if(s == "LD"){
            for(int i = x; i >= 0; i--){
                for(int j = x; j >= 0; j--){
                    if(i + j < x) arr[db - i][lb + j] = 0;
                    else if(i + j > x) arr[db - i][lb + j] += arr[db - (x - j)][lb + (x - i)];
                }
            }
        }
        else if(s == "LU"){
            for(int i = x; i >= 0; i--){
                for(int j = x; j >= 0; j--){
                    if(i + j < x) arr[ub + i][lb + j] = 0;
                    else if(i + j > x) arr[ub + i][lb + j] += arr[ub + x - j][lb + x - i];
                }
            }
        }
        else if(s == "RU"){
            for(int i = x; i >= 0; i--){
                for(int j = x; j >= 0; j--){
                    if(i + j < x) arr[ub + i][rb - j] = 0;
                    else if(i + j > x) arr[ub + i][rb - j] += arr[ub + x - j][rb - (x - i)];
                }
            }
        }
        else if(s == "RD"){
            for(int i = x; i >= 0; i--){
                for(int j = x; j >= 0; j--){
                    if(i + j < x) arr[db - i][rb - j] = 0;
                    else if(i + j > x) arr[db - i][rb - j] += arr[db - (x - j)][rb - (x - i)];
                }
            }
        }
    }
    cout << db - ub + 1 << ' ' << rb - lb + 1 << '\n';
    for(int i = ub; i <= db; i++){
        for(int j = lb; j <= rb; j++) cout << arr[i][j] << ' ';
        cout << '\n';
    }
}
