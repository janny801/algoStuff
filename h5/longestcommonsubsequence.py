#Longest common subsequence

#Let A[0:m] and B[0:n] be two arbitrary arrays.

# A common subsequence of A and B is another sequence that is a subsequence of both A and B. 

# compute the length of the longest common subsequence of A and B.

def lcs(array1, array2): 
    #get lens of array 
    len1= len(array1)
    len2 = len(array2) 
    
    #create 2d table (initialized with 0 )
    lcstable = []
    for i in range(len1+ 1): 
        row = []
        for j in range(len2+ 1): 
            row.append(0)
        lcstable.append(row)
    
    #fill table up in bottom up manner
    for i in range(1, len1+1): 
        for j in range(1,len2+1): 
            if array1[i-1] == array2[j-1]:
                #case 1: chars match (extend lcs) 
                lcstable[i][j] = lcstable[i-1][j-1] + 1 
            else: 
                #case 2: chars dont match ; take best so far 
                lcstable[i][j] = max(lcstable[i-1][j], lcstable[i][j-1])
                    #ie ) skipping one of these would give us a better result 
                        #input the better result
    #result is stored in bottom right cell 
    return lcstable[len1][len2]


#main func 
if __name__ == '__main__': 
    array1 = [1, 3, 4, 1, 2, 3]
    array2 = [3, 4, 1, 2, 1, 3]
    
    #compute lcs length (call func) 
    lcslen = lcs(array1, array2)
    
    print(lcslen)