#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cout<<"Enter the string : ";
    getline(cin, s);
    int m = s.length();
    for(int i = 0; i<m/2 + 1 ; i++)
    {
        char c = s[i];
        s[i] = s[m-i-1];
        s[m-i-1] = c;
    }
    cout<<s;
    return 0;
}

