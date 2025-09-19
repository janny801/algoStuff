#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <cassert>
using namespace std; 

struct Node {
    Node* left; 
    Node* right;
    int   val; 
};

// insert the val into leaves of the tree rooted at `root`
// if root is nil, allocate a node for val
// returns the root of the tree (new tree if root==null)
Node* insert(Node* root, int val) {
    if (root == NULL) {
    	Node* node = new Node;
    	node->left = NULL;
    	node->right = NULL;
    	node->val = val;
    	return node;
    }

    if (val < root->val)
	    root->left = insert(root->left, val); 
    else
	    root->right = insert(root->right, val);

    return root;
}

// debug utility
void print(Node* root, int indent) {
    if (root == NULL) return;
    print(root->right, indent+4);
    for (int i=0; i<indent; i++) printf(" ");
    printf("%d\n", root->val);
    print(root->left, indent+4);
}


//return number of edges for shortest path between n1 and n2 
int dist(Node*root, int n1, int n2) 
{
    // check incase tree is empty(there is no path) 
    if(root ==nullptr)
    {
        return -1; 
    }
    
    //find lowest common ancestor (lca) 
    Node *lca = root; 
    while(lca!=nullptr)
    {
        if(n1 < lca->val && n2 < lca->val)
        {
            // if both smaller then lca should be in left subtree
            lca = lca-> left; 
        }
        else if(n1> lca-> val && n2> lca-> val)
        {
            //if both larger then lca should be in right subtree 
            lca = lca -> right; 
        }
        else
        {
            //values diff on either side or equal 
            // this node becomes the lca (break out of this loop) 
            break; 
        }
    }
    
    
    //find distance from lca to n1 
    int distn1 = 0; 
    Node* curr = lca; 
    while(curr!= nullptr && curr-> val != n1)
    {
        if(n1 < curr-> val)
        {
            //n1 value is smaller so go left 
            curr = curr-> left; 
        }
        else
        {
            //n1 value larger, go right 
            curr = curr-> right; 
        }
        distn1++; //increment distance for lca to n1 
    }
    
    //find distance from lca to n2 
    int distn2 = 0; 
    curr = lca; 
    while(curr!=nullptr && curr-> val != n2)
    {
        if(n2<curr-> val)
        {
            //n2 less so check left 
            curr = curr-> left; 
        }
        else
        {
            //n2 larger , check right 
            curr = curr-> right; 
        }
        distn2++; //increment for lca to n2 
    }
    
    
    return distn1+ distn2; 
    
}




int main() {
    std::vector<int> A;
    int a;
    std::string line;
    std::getline(std::cin, line);
    std::stringstream ss(line);
    while (ss >> a) {
	    A.push_back(a); 
    }
    int n1, n2; 
    std::cin >> n1 >> n2;

    Node* root = NULL;
    for (int i=0; i<A.size(); i++) {
	    root = insert(root, A[i]); 
    }


    //print statement test to show whole tree
    //print(root,0);

    // TODO: Implement your dist function and output its result to stdout
    std::cout << dist(root, n1, n2) << "\n";
}


/* 
example input ; 

3 1 5 7 2 4
1 7

*/ 


