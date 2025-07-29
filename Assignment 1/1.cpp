#include<bits/stdc++.h>
using namespace std;

int main()
{
    int m ;
    cout<<"Enter the size of the array ";
    cin>>m;
    int arr[m];
    for(int i = 0 ; i < m ; i++)
    {
        cin>>arr[i];
    }
    int avg = 0;
    for(int i = 0 ; i<m; i++)
    {
        avg += arr[i];
    }
    cout<<"Average: "<<float(avg)/m;
    return 0;
}
