#include <bits/stdc++.h>

using namespace std;
 
int linearSearch(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}

int binarySearch(int arr[], int l, int r, int x)  // This method of searching requires 
{                                                 // the array to be sorted in increasing order
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
        if (arr[mid] == x) 
            return mid;  
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid - 1, x);  
        return binarySearch(arr, mid + 1, r, x); 
    } 
    return -1; 
} 

int main(){
    int arr[] = {1,4,5,9,11,16,19,51};
    int n = sizeof(arr)/sizeof(int);
    cout<<linearSearch(arr, n, 51)<<"\n"
        <<binarySearch(arr, 0, n, 51);
    return 0;
}