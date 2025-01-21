""""task 1"""

def fuse(fitmons):
    """
    function description: thhis function calculates the max combined cutness score 
    that can be achieved by the fusing fitmonds. the code considers the affinity values on both the left 
    and right of each fitmon to calculate the cuteness value when two or more fitmons are combined. 
    the method uses dynamic programming to find the most optimal combination of fusions.

    input: the input is 'fitmons' which is list of lists where each inner list is a fitmon and contains:
    - affinity_left. this  is a float value. it is the affintity of the fitmon with the one to its left. 
    this value ranges from 0.1-0.9 unless it is the leftmost fitmon (in that case it is 0).
    - affinity_right. this  is a float value. it is the affintity of the fitmon with the one to its right. 
    this value ranges from 0.1-0.9 unless it is the rightmost fitmon (in that case it is 0).
    -cuteness_score. this is an integer. it is the inherent score of cutness of the fitmon. 
    the value has to be greater than 0. 

    output: the output is the max cuteness score that can be acheived by fusing all fitmons in the list.

    time complexity: the time complexity is O(n^3) where n is the number of fitmons. 
    this is because the function uses 3 nested loops to calculate the max cuteness.

    space complexity: the space complexity is O(n^2) where n is the number of fitmons. 
    this is because of the use of 2d matrix to store the data of fusions between every pair of fitmons.
    """

    N=len(fitmons)
    matrix = [[0]*N for _ in range(N)]#setting up the matrix to store the scores

    #setting up the diagonal of the matrix
    #uses base case(the signle fitmons that cant be difused bc they are singular)
    for i in range(N):
        matrix[i][i]=fitmons[i][1]

    #to fill the matrix
    #length of the path starting from 2 bc we start fusing 2 fitmons first
    for length in range(2, N+1): 
        for i in range(N-length+1):#starting index is i and ending is j
            j=i+length-1
            for k in range(i,j):
            #fuses every possible pair with the path from i-j
            #right affinity of the left and left affinity of the right and respective max scores
                cuteness_now= int(matrix[i][k]* fitmons[k][2] +matrix[k+1][j]* fitmons[k+1][0])
                matrix[i][j]= max(matrix[i][j], cuteness_now)#then updated the max score with new one after comparisons

    return matrix[0][N-1]#the whole array of all possible fusions

print(fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]]))
print(fuse([[0, 48, 0.8], [0.8, 91, 0.9], [0.9, 29, 0]]))
print(fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 50, 0]]))
print(fuse([[0, 50, 0.6], [0.6, 50, 0.3], [0.3, 50, 0]]))
print(fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 80, 0]]))
print(fuse([[0, 50, 0.6], [0.6, 98, 0.4], [0.4, 54, 0.9], [0.9, 6, 0.3],
[0.3, 34, 0.5], [0.5, 66, 0.3], [0.3, 63, 0.2], [0.2, 52, 0.5],
[0.5, 39, 0.9], [0.9, 62, 0]] ))


