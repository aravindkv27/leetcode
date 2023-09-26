#include<bits/stdc++.h>
using namespace std;

int main()
{
    int age;
    cout<<"Enter the age: ";
    cin >> age;

    if (age <= 18){
        cout<<"Not Eligible to work";
    }
    else if( age <= 57){
        cout<<"Eligible to work";
        if (age >=55){
            cout << ", But retire soon";
        }
    }
    else{
        cout<<"Retrie Soon";
    }
    return 0;
}