#finding path with minimum cost 

def pathmincost(costmatrix, totalrows, totalcols): 
    
    #mincost ; mincost to reach (row,col) 
    mincost=[]
    for row in range(totalrows): #initial 2d matrix filled with all 0s
        mincost.append([0] * totalcols)
    
    #start w/ first column ; same as mincost 
    for row in range(totalrows): 
        mincost[row][0] = costmatrix[row][0] 
        #copies first col (as it is) into mincost matrix 
    
    #fill in rest of table column by column 
    for col in range(1,totalcols): 
        for row in range(totalrows): 
            #get positions we can come from in previous column 
                #mod incase need to wrap around 
            upperrow = (row - 1) %totalrows
            samerow = row 
            lowerrow = (row +1) % totalrows 
            
            #assume we come from upper row 
            bestprevrow = upperrow 
            
            #check if coming from same row gives smaller cost 
            if mincost[samerow][col-1] < mincost[bestprevrow][col-1]:
                bestprevrow = samerow 
            
            #check if coming from lowerrow gives smaller cost 
            if mincost[lowerrow][col-1] < mincost[bestprevrow][col-1]: 
                bestprevrow = lowerrow
            
            #bestprevrow now properly stored (add to mincost matrix)
            mincost[row][col] = costmatrix[row][col] + mincost[bestprevrow][col-1]
            
    #after filling all rows 
    #last col has total cost for all possible endings 
        #then get smallest value in last column -> return it
    besttotalcost = mincost[0][totalcols-1] #assume row 0 is the lowest initially
    for row in range(1,totalrows):
        if mincost[row][totalcols-1] < besttotalcost: 
            besttotalcost = mincost [row][totalcols-1]
    
    return besttotalcost

#main program 
if __name__ == "__main__": 
    
    #read input to get numbers of rows and cols 
    userinput = input().split()
    totalrows = int(userinput[0])
    totalcols = int(userinput[1])
    
    #read 'totalrows' lines to build the matrix 
    costmatrix = []
    for i in range(totalrows): 
        rowvalues = list(map(int, input().split()))
        costmatrix.append(rowvalues)
    #call the func and print result  
    result = pathmincost(costmatrix, totalrows, totalcols)
    print(result)