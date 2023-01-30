## given a square matrix of integers (array of array
## integer value
## [[1,2,3][4,5,6][7,8,9]] ---> 2
##
## loop over [0][0], [1][1], [2][2] and [2][0], [1][1], [0,2]
## sum those forward/backward diagonals
## take absolute difference

def diagonalDifference(arr):
    diag_i = 0
    diag_j = 0
    l = len(arr)
    for i in range(l):
        diag_i += arr[i][i]
            
    for j in range(l-1, -1, -1):
        diag_j += arr[l-1-j][j]
        
    return abs(diag_j - diag_i)
