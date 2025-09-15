//hw2; reconstruct binary tree
#include <stdio.h>
using namespace std; 
#include <iostream> 

void postorder(int* preorderptr, int* inorderptr, int numnodes)
{
    //base case; if there are no nodes , then stop 
    if(numnodes<= 0)
    {
        return; 
    }
    
    //first element in preorder is the root 
    int rootval= preorderptr[0]; 
    
    //find the root in the inorder part 
    int leftsubtreesize = 0; 
    while(leftsubtreesize < numnodes && inorderptr[leftsubtreesize] != rootval)
    {
        leftsubtreesize++; //find index of same value as rootval
                            //this separates the left and right subtrees
    }
    
    //recusively process the left subtrees
    postorder(preorderptr+1, inorderptr, leftsubtreesize); 
    
    //recursively process the right subtree
    postorder(preorderptr+1+leftsubtreesize, inorderptr+1+leftsubtreesize, numnodes - 1 -leftsubtreesize); 
    
    //print the root 
    cout<<rootval<<' '; 
}

int main()
{
    //get the inputs 
    int numnodes; 
    cin>>numnodes; 
    
    int* preorder = new int[numnodes]; 
    int* inorder = new int[numnodes];
    
    for(int i =0; i<numnodes; i++)
    {
        cin>> preorder[i]; 
    }
    
    for(int i = 0; i<numnodes; i++)
    {
        cin>>inorder[i]; 
    }
    
    //make function call here 
    postorder(preorder, inorder,numnodes); 

    delete[]preorder; 
    delete[]inorder; 

    return 0;
}