#include<bits/stdc++.h>
using namespace std;
int main(){
    int val;
    cin >> val;
   for (int i = val; i>0; i--){
    for (int j=1; j<=i; j++){
        cout<<j<<" ";
    }
    cout<<"\n";
   }
    return 0;
}