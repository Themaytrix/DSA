matrix = [[112, 42, 83, 119], 
        [56, 125, 56, 49], 
        [15, 78, 101, 43], 
        [62, 98, 114, 108]]

# find the largest sum of the upper quadrant. i.e flip matrix till you have the largest sum of the upper quadrant


def flippingMatrix(matrix):
    # square matrix so row=column
    n = len(matrix)
    sum = 0 
    
    for i in range(n//2):
        for j in range(n//2):
            print(i,j)
            largest_in_mirror = max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j],matrix[n-i-1][n-j-1])
            sum = sum + largest_in_mirror
    return sum


print(flippingMatrix(matrix))
