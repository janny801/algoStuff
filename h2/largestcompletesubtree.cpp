//hw2; find largest complete subtree in binary tree
//need to make into rhythm code 

#include <stdio.h>
#include <iostream> 
using namespace std; 

struct treenode {
    int value;
    treenode* left;
    treenode* right;
    // constructor to easily create a new node
    treenode(int v) {
        value = v;
        left = nullptr;
        right = nullptr;
    }

};


int findlargestsubtree(treenode*currentnode, treenode* &bestnode, int &bestdepth) 
{
    //base case; empty subtree is considered perfect with height = 0
    if(currentnode == nullptr)
    {
        return -1; //empty = -1 edges ,, makes the leaf node 0 
    }
    
    //recursion ; check left and right subtrees and get heights
    int leftheight = findlargestsubtree(currentnode-> left, bestnode, bestdepth); 
    int rightheight = findlargestsubtree(currentnode-> right, bestnode, bestdepth); 
   
    
    //find the smaller height between the left and right subtrees
    int shorterheight = leftheight; 
    if(rightheight < shorterheight)
    {
        shorterheight= rightheight; 
    }
    
    int height = 1+ shorterheight; //or; 1+ min(leftheight, rightheight)
    
    //if this current node has largest perfect subtree so far; update bestdepth&bestnode
    if(height>bestdepth)
    {
        bestdepth = height; 
        bestnode = currentnode; 
    }
    
    
    //return this subtrees height to the parent call 
    return height; 
    
}


int main()
{
    
    //change this to test diff inputs 
    
    // build a small test tree manually:
    //        5
    //      /   \
    //     3     7
    //    / \   /
    //   1   4 6
    
    treenode* n5 = new treenode(5);
    treenode* n3 = new treenode(3);
    treenode* n7 = new treenode(7);
    treenode* n1 = new treenode(1);
    treenode* n4 = new treenode(4);
    treenode* n6 = new treenode(6);

    n5->left = n3;  n5->right = n7;
    n3->left = n1;  n3->right = n4;
    n7->left = n6;
    
    treenode*root = n5; 
    
    //change this to test diff inputs 
    
    
    
    
    
    
    //pass to function and output 
    treenode *bestnode = nullptr; 
    int bestdepth = 0; 
    int height = findlargestsubtree(root, bestnode, bestdepth); 

    cout<<"largest perfect subtree depth: "<<height<<endl; 
    cout<<"root of perfect subtree: "<<bestnode->value<<endl; 

    return 0;
}
