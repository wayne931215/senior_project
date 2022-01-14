#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
#define F first
#define S second
#define MP make_pair
#define PB emplace_back
using namespace std;
using ll = long long;
using pii = pair<ll, ll>;
void debug() {cout << '\n';}
template<class T, class ...U> void debug(T a, U... b){cout << a << ' '; debug(b...);}

int t, q;
vector<string> vc, qq;
vector<int> dir;
unordered_map<char, int> mp;

bool cmp(string a, string b){
    if(a[1] != b[1]) return mp[a[1]] < mp[b[1]];
    return a[0] < b[0];
}

void del(string s){
    for(int i = 0; i < vc.size(); i++){
        if(vc[i] == s){
            for(int j = i; j < vc.size(); j++) vc[j] = vc[j + 1];
            break;
        }
    }
    vc.pop_back();
}

void print(){
    for(int i = 0; i < vc.size(); i++) cout << vc[i][0];
    for(int i = qq.size() - 1; i >= 0; i--){
        if(dir[i] == 0) cout << "..";
        else cout << qq[i][0];
    }
    cout << '\n';
    for(int i = 0; i < vc.size(); i++) cout << vc[i][1];
    for(int i = qq.size() - 1; i >= 0; i--){
        if(dir[i] == 0) cout << qq[i];
        else cout << qq[i][1];
    }
    cout << '\n';
}

signed main(){
    cin >> t;
    string s, s1, s2, s3, s4;
    mp['m'] = 1; mp['p'] = 2; mp['s'] = 3; mp['z'] = 4;
    while(t--){
        vc.clear();
        qq.clear();
        dir.clear();
        for(int i = 0; i < 13; i++){
            cin >> s;
            vc.PB(s);
        }
        cin >> q;
        sort(vc.begin(), vc.end(), cmp);
        print();
        while(q--){
            cin >> s;
            if(s == "pon"){
                cin >> s1 >> s >> s2 >> s >> s3;
                del(s1); del(s1); del(s3);
                qq.PB(s1); qq.PB(s1); qq.PB(s1);
                if(s2 == "left") dir.PB(1), dir.PB(1), dir.PB(0);
                else if(s2 == "right") dir.PB(0), dir.PB(1), dir.PB(1);
                else dir.PB(1), dir.PB(0), dir.PB(1);
            }
            else if(s == "chi"){
                cin >> s1 >> s >> s2 >> s >> s3 >> s >> s4;
                del(s2); del(s3); del(s4);
                qq.PB(s3); qq.PB(s2); qq.PB(s1);
                dir.PB(1); dir.PB(1); dir.PB(0);
            }
            else{
                cin >> s1 >> s >> s2;
                vc.PB(s1);
                sort(vc.begin(), vc.end(), cmp);
                del(s2);
            }
            print();
        }
    }
}
