#include<bits/stdc++.h>
using namespace std;
int main(){
    int a;
    cin >> a;
    for (int i=0; i<a; i++){
        for(int j=0; j<a-i-1;j++){
            cout<<" ";
        }
        for(int k=0; k<2*i+1; k++){
            cout<<"*";
        }
        for(int l=0; l<a-i-1; l++){
            cout<<" ";
        }
        cout<<"\n";
    }

    return 0;
}