# A string w of parentheses ( and ) and brackets [ and ] is balanced 
#if it satisfies one of the following conditions:

    # w is the empty string
    
    # w = (x) for some balanced string x
    
    # w = [x] for some balanced string x
    
    # w = xy (concatenation) for some balanced strings x and y

# For example, the string
# w=([()][]())[()()]() is balanced, because w=xy, where x=([()][]()) and y=[()()]()

# 1. Describe and analyze an algorithm to determine 
    # whether a given string of parentheses and brackets is balanced.

# 2. Describe and analyze an algorithm to compute the length of 
    # a longest balanced subsequence of a given string of parentheses and brackets.
    
#helper funcs _____________________
def isopeningsymbol(ch): 
    if ch == '(' or ch == '[': 
        return True 
    return False 
    
def isclosingsymbol(ch): 
    if ch == ')' or ch == ']': 
        return True
    return False 
    
def isvalidpair(openingch, closingch): 
    if openingch == '(' and closingch == ')': 
        return True
    if openingch == '[' and closingch == ']': 
        return True 
    return False 
#helper funcs ___________________

def isbalancedstring(inputstring): 
    #use stack to keep track of parentheses and brackets
    symbolstack = [] 
    
    for currsymbol in inputstring: 
        if isopeningsymbol(currsymbol): 
            symbolstack.append(currsymbol) 
        else: 
            #case; closing symbol 
            if len(symbolstack) == 0: 
                return False 
            topsymbol = symbolstack.pop()
            if isvalidpair(topsymbol, currsymbol) == False:
                return False
    
    #if stack is empty then all openings were correctly matched 
    if len(symbolstack) ==0: 
        return True
    return False #if not empty 

def longbalanlen(inputstring): 
    #dp sol 
    inputlength = len(inputstring)
    
    #stores longest balanced length for every subseq starting from the index 
        #checks all  subseq starting from that index 
    longestbalancedeach = []
    #initialize table with 0  
    for i in range (inputlength): 
        row = [0] * inputlength
        longestbalancedeach.append(row)
    #build results bottom up - increase subseq len 
    for subseqlen in range(2, inputlength +1): #iterate thru possible subseq lens
        for startind in range(0, inputlength - subseqlen +1): #check each subseq of given len
            endind = startind + subseqlen -1 #last possible check before out of bounds 
            
            #opt1: skip;  already checked in smaller subseq length 
                #also allows us to move the window we check across 
            bestlen = longestbalancedeach[startind+1][endind]
            
            #opt2 : if starting symbol is open -> try find closing pair 
            if isopeningsymbol(inputstring[startind]): 
                for maybematch in range(startind+1, endind+1): 
                    #iterate from start to end to find match 
                    if isclosingsymbol(inputstring[maybematch]) and isvalidpair(inputstring[startind], inputstring[maybematch]):
                        #get length of balanced subseq between 
                        innerlen = longestbalancedeach[startind+1][maybematch-1]
                        
                        #length of balanced subseq after the pair
                            #to the right of the closing symbol 
                        rightlen = 0
                        if maybematch +1<= endind: 
                            rightlen = longestbalancedeach[maybematch+1][endind]
                            #looks up best balanced subseq after the current pair 
                        
                        #total candidate len if we use this pair 
                        totallen = innerlen + 2+ rightlen 
                        
                        #update if better than current best
                        if totallen> bestlen: 
                            bestlen = max(bestlen, totallen) 
            
            #store best result for the subseq inputstring[startind, endind] 
            longestbalancedeach[startind][endind] = bestlen #ie put into dp table 
    
    #get the longest balanced subsequence for the entire input string 
    if inputlength ==0: 
        return 0
    return longestbalancedeach[0][inputlength -1]



#main function 
if __name__ == "__main__": 
    #read input string from user 
    inputstring = input().strip()
    
    #check if balanced 
    result = isbalancedstring(inputstring)
    if result: 
        print("it is balanced")
    else: 
        print("it is not balanced")
        
    #compute and print the len of the longest balanced subseq 
    longestlen = longbalanlen(inputstring)
    print("longest len = ", longestlen)
    
    
    