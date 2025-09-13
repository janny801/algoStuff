//need make into rhythm code
//find local minimum in an array 


#include <stdio.h>
#include <iostream> 

using namespace std; 

int findLocalMin(int array[], int arraysize)
{
    // func 
    
    //step 1; find values for hi/low 
    int low = 1; 
    int high = arraysize-2; 
    
    //step 2; find value for mid 
    int mid = (low+high)/2; 
    
    //edge case; if the array has less than 3 elements
    if(arraysize<3)
    {
        return -1; 
    }

    //step 3; check values left and right of mid 
    //iterate similar to binary sear
    
    while(low<= high )
    {
        // udpate mid witheach iteration based on current values of low/high
        mid = (low+ high )/2; 
        
        //get values for neighbors and mid 
        int leftNeighbor = array[mid-1]; 
        int midValue = array[mid]; 
        int rightNeighbor = array[mid+1];
        
        
        //check if mid itself is a local minimum 
        if(leftNeighbor<= midValue && midValue<= rightNeighbor)
        {
            //if less than both leftNeighbor and rightNeighbor then it is local minima 
            //then return that index 
            return mid; 
        }
        else if(leftNeighbor < midValue)
        {
            //case 1(not local min); midValue greater than leftNeighbor
            
            
            //shift focus to check the left side of the array 
            high = mid -1; 
        }
        else
        {
            //case 2 (not local min); midValue greater than rightNeighbor
            low = mid +1; 
        }
        
    }
    //shouldnt reach here if i coded this right ; but need to include for c++ compilation
    
    return -1; 
    
}

int main()
{
        
    int arr[] = {9,7,7,2,1,3,7,5,4,7,3,3,4,8,6,9};
        
    //find the size of the array 
    int arraysize = sizeof(arr)/ sizeof(arr[0]); 
    
    //pass into function 
    int localMinIndex = findLocalMin(arr, arraysize); 
    
    cout<<"One of the local minima is located at..." <<endl
    <<"Index: "<<localMinIndex<<endl<<"Value: "<<arr[localMinIndex]<<endl; 
    

    return 0;
}