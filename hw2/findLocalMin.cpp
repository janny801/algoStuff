//hw2; find largest complete subtree in binary tree
//need to make into rhythm code 

#include <stdio.h>
#include <iostream> 
#include <algorithm> 
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
    
    int height = 1+ min(leftheight,rightheight); 
    
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
    
    /*
                n1
               /  \
             n2    n3
            /     /  \
          n4     n5    n6
                / \    / \
              n7  n8  n9 n10
             / \ / \  / \ / \
           n11 n12 n13 n14 n15 n16 n17 n18
    
    largest complete subtree should be rooted at n3 with depth = 3 (edges)
    root n1 is not balanced so its height will be smaller
    */
    
    treenode* n1 = new treenode(1);
    treenode* n2 = new treenode(2);
    treenode* n3 = new treenode(3);
    treenode* n4 = new treenode(4);
    treenode* n5 = new treenode(5);
    treenode* n6 = new treenode(6);
    treenode* n7 = new treenode(7);
    treenode* n8 = new treenode(8);
    treenode* n9 = new treenode(9);
    treenode* n10 = new treenode(10);
    treenode* n11 = new treenode(11);
    treenode* n12 = new treenode(12);
    treenode* n13 = new treenode(13);
    treenode* n14 = new treenode(14);
    treenode* n15 = new treenode(15);
    treenode* n16 = new treenode(16);
    treenode* n17 = new treenode(17);
    treenode* n18 = new treenode(18);
    
    n1->left = n2;   n1->right = n3;
    n2->left = n4;
    
    n3->left = n5;   n3->right = n6;
    n5->left = n7;   n5->right = n8;
    n6->left = n9;   n6->right = n10;
    
    n7->left = n11;  n7->right = n12;
    n8->left = n13;  n8->right = n14;
    n9->left = n15;  n9->right = n16;
    n10->left = n17; n10->right = n18;
    
    treenode* root = n1;

    
    //change this to test diff inputs 
    
    
    
    
    
    
    //pass to function and output 
    treenode *bestnode = nullptr; 
    int bestdepth = 0; 
    int height = findlargestsubtree(root, bestnode, bestdepth); 

    cout<<"largest perfect subtree depth: "<<bestdepth<<endl; 
    cout<<"root of perfect subtree: "<<bestnode->value<<endl; 

    return 0;
}
