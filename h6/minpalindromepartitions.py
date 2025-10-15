#Find the minimum number of palindromes that make up the given string

#palindrome dynamic programming 

def minpartition(inputstring): 
    n= len(inputstring) 
    
    #initialize palindrome table with all false vals 
    ispalindrome =[]
    for i in range(n): 
        row = [False] *n
        ispalindrome.append(row) 
    
    #compute all palindrome substrings
    for endindex in range(n): 
        for startindex in range(endindex+1): 
            #check if substring is a palindrome 
            if inputstring[startindex] == inputstring[endindex]: 
                #if substring length less than or eq 2 ; automatically a palindrome
                if endindex-startindex<=2: 
                    ispalindrome[startindex][endindex] = True 
                elif ispalindrome[startindex+1][endindex-1]: 
                    #checks if inside is already a known palindrome
                    ispalindrome[startindex][endindex] =True
    #dp array to store amt of times we have to cut the string 
    minpartitions= [0]*n
    
    for i in range(n): 
        if ispalindrome[0][i]: 
            minpartitions[i]=1
        else: 
            #start with worst possible case 
            minpartitions[i] = i+1
            
            #try every possible split point 
            for j in range(1, i+1): 
                #if j-> i is a palindrome ,, find min partition
                if ispalindrome[j][i]: 
                    minpartitions[i] = min(minpartitions[i], minpartitions[j-1]+1)
                    #check if splitting before j gives smaller palindromic parts
    return minpartitions[n-1]

#main 
if __name__ == '__main__': 
    #read input values 
    n = int(input().strip())
    inputstring = input().strip()
    
    #compute and print results 
    result = minpartition(inputstring) 
    print(result) 


