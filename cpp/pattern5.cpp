#include<bits/stdc++.h>
using namespace std;
int main(){
    int val;
    cin >> val;
    for(int i=1; i<=val; i++){
        for(int j=0; j<val-i+1; j++){
            cout<< "*"<< " ";
        }
        cout<<"\n";
    }
    
    return 0;
}