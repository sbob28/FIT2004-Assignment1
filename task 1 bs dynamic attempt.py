
def fuse(fitmons):
    #N  is number of fitmons
    N = len(fitmons)
    matrix = [[0] * N for _ in range(N)] #setting up the matrix to store the maximum score 
    
    #setting up the diagonal of the matrix using base case 
    #(the single fitmons that cant be difused bc they are singular)
    for i in range(N):
        matrix[i][i] = fitmons[i][1]
    
    #to fill in the matrix
    #length of the path starting from 2 bc we start fusing 2 fitmons first 
    for length in range(2, N+1):  #path weight (length??)
        for i in range(N - length + 1): #starting index (i)
            j = i + length - 1 #ending index (j)
            # fuses every possible pair with the path from i to j [i...j]
            for k in range(i, j): 
                #new cuteness after fusing [i...k] and [k+1...j]
                #right affinity of the left and left affinity of the right 
                #respective maximum scores matrix[i][k] and matrix[k+1][j]
                current_cuteness = int(matrix[i][k] * fitmons[k][2] + matrix[k+1][j] * fitmons[k+1][0])
                #updates the maximum score with the new one
                matrix[i][j] = max(matrix[i][j], current_cuteness)
    
    #result for the whole array (after considering all possible fusions)
    return matrix[0][N-1]
    

print(fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]]))  #126
print(fuse([[0, 48, 0.8], [0.8, 91, 0.9], [0.9, 29, 0]]))  #126
print(fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 50, 0]]))  #24
print(fuse([[0, 50, 0.6], [0.6, 50, 0.3], [0.3, 50, 0]]))  #48
print(fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 80, 0]]))  #33
print(fuse([[0, 50, 0.6], [0.6, 98, 0.4], [0.4, 54, 0.9], [0.9, 6, 0.3],[0.3, 34, 0.5], [0.5, 66, 0.3], [0.3, 63, 0.2], [0.2, 52, 0.5], [0.5, 39, 0.9], [0.9, 62, 0]])) #132
