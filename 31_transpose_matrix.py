import os
os.system('cls')
os.system('prompt $G')
os.system('mode con: cols=60 lines=20')
##############################transpose matrix########################################

def transposeMatrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    result=[[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i]=matrix[i][j]
            
    
    return result

print(transposeMatrix([[1, 2, 3], [4, 5, 6]]))