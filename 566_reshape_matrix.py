
    
def matrixReshape(mat, r, c):
    
    m, n = (len(mat), len(mat[0]))

        
    if m * n != r * c:
        return mat
        
    output = [[0 for _ in range(c)] for _ in range(r)]
        
    temp = []        
        
    for i in range(m):
            
        for j in range(n):

            temp.append(mat[i][j])
        
    k =0
    for i in range(r):
            
        for j in range(c):
                
            output[i][j] = temp[k]
            k +=1
                
    return output


mat = list(map(int, input().split()))
c = int(input())
r = int(input())

result = matrixReshape(mat,r,c)
print(result)