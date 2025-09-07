#include <stdio.h> 
#include <iostream> 
using namespace std; 
#include <algorithm> 

int findMaxDiff(int arr[], int left, int right, int &minVal, int &maxVal )
{
    //pass minVal and maxVal by reference 
        //allow for changes to be reflected each recursive step
    //recursive divide and conquer 
    
    if(left == right) 
    {
        //base case: subarray has only one element
        minVal = arr[left]; 
        maxVal = arr[left]; 
        return 0; 
        //if subarray size =1 ; that number is both the min and the max 
    }
    int mid = (left + right) /2; 
    
    
    //values for left and right halves 
    int leftMin, leftMax, rightMin, rightMax; 
    
    //recurse 
    int leftDiff = findMaxDiff(arr, left, mid, leftMin, leftMax); 
    int rightDiff = findMaxDiff(arr, mid+1, right, rightMin, rightMax); 
    
    
    //cross difference
    int crossDiff = rightMax - leftMin; 
    
    //best difference for this segment 
    int best = max({leftDiff, rightDiff, crossDiff}); 
    if(best<0)
    {
        best =0; 
    }
    
    //update min and max for this segment 
    minVal = min(leftMin, rightMin); 
    maxVal = max(leftMax,rightMax); 
    
    return best; 
    
    
    
    
}

int main()
{
    int arraySize; 
    cin>>arraySize; 
    
    int*arr = new int[arraySize]; //allocate dynamic array 
    for(int i = 0; i<arraySize; i++)
    {
        cin>>arr[i]; 
    }
    int minVal, maxVal; 
    
    
    
    int ans = findMaxDiff(arr, 0, arraySize-1, minVal, maxVal); 
    cout<<ans<<"\n"; 
    
    delete[] arr; //free mem 
    return 0; 
    
    
    
}