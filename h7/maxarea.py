#Maximum area of solid square blocks

def max_solid_square_area(bitmap):
    number_of_rows = len(bitmap)
    number_of_columns = len(bitmap[0])
    
    # dp[] stores the side length of the largest solid square
    dp = []
    for row_index in range(number_of_rows):
        row = [0] * number_of_columns
        dp.append(row)
    
    maximum_square_side = 0
    
    for row_index in range(number_of_rows):
        for col_index in range(number_of_columns):
            
            # start by assuming largest square ends at this cell 
            dp[row_index][col_index] = 1
            
            # check if current cell has same value as 
                #cell above, cell to the left , cell to the top left of the current
            if row_index > 0 and col_index > 0:
                # if all match --> extend 
                if bitmap[row_index][col_index] == bitmap[row_index-1][col_index] and \
                   bitmap[row_index][col_index] == bitmap[row_index][col_index-1] and \
                   bitmap[row_index][col_index] == bitmap[row_index-1][col_index-1]:
                    
                    # find smallest neighbor
                    smallestneighbor = min(
                        dp[row_index-1][col_index],      # top
                        dp[row_index][col_index-1],      # left
                        dp[row_index-1][col_index-1]     # cell top left of curr
                    )

                    #extend that square +1 
                    dp[row_index][col_index] = 1+ smallestneighbor
            
            # compare to current max 
            if dp[row_index][col_index] > maximum_square_side:
                maximum_square_side = dp[row_index][col_index]
    
    # square for max area 
    maximum_area = maximum_square_side * maximum_square_side
    return maximum_area



if __name__ == "__main__":
    # get rows and col size 
    number_of_rows = int(input("rows: "))
    number_of_columns = int(input("cols: "))
    
    bitmap = []
    
    print("enter bitmap:")
    
    # read bitmap 
    for row_index in range(number_of_rows):
        row_input = input().strip().split()
        
        # conv to int
        current_row = []
        for value in row_input:
            current_row.append(int(value))
        
        bitmap.append(current_row)
    
    result = max_solid_square_area(bitmap)
    print("Maximum solid square area:", result)

