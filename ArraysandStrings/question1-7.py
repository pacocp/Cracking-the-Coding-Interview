'''Question 1.7

@author: Francisco Carrillo-Perez
'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
N = len(matrix) - 1
new_matrix = [[0,0,0],[0,0,0],[0,0,0]]

for j in range(N+1):
    for i in range(N+1):
        new_matrix[i][N-j] = matrix[j][i]

print(new_matrix)
