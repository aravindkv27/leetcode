#include<bits/stdc++.h>
using namespace std;

int main() {

    int mark ;
    cin >> mark;
    if (mark >=80 and mark <=100){
        cout<< "A"<<"\n";
    }
    else if (mark >= 60 and mark <= 79){
        cout<<"B\n";
    }
    else if (mark >= 50 and mark <= 59){
        cout<<"C\n";
    }
    else if (mark >= 40 and mark <= 49){
        cout<<"D\n";
    }
    else if (mark <=25){
        cout<<"F";
    }

    return 0;
}