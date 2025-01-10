def spiralmatrix(matrix):
    # define boundaries
    i,j = 0,0
    left,right = -1,len(matrix[0])
    bottom = len(matrix)
    top = 0
    ans = []
    m_right,m_left,m_down,m_up = 0,1,2,3

    direction = m_right

    while len(ans) != len(matrix[0]) * len(matrix):
        if direction == m_right:
            while j<right:
                print("right")
                ans.append(matrix[i][j])
                j+=1
            # update 
            direction = m_down
            right -= 1
            i,j = i+1, j-1
        elif direction == m_down:
            while i < bottom:
                print("down")
                ans.append(matrix[i][j])
                i += 1
            direction = m_left
            i,j = i-1, j-1
            bottom -= 1
        elif direction == m_left:
            while j>left:
                print("left")
                ans.append(matrix[i][j])
                j -= 1
            direction = m_up
            i,j = i-1,j+1
            left += 1
        else:
            while i>top:
                print("up")
                ans.append(matrix[i][j])
                i -= 1
            direction = m_right
            i,j = i+1, j+1
            top += 1
    return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralmatrix(matrix))