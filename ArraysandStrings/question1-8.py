'''Question 1.8


@author: Francisco Carrillo-Perez
'''

matrix = [[1,2,3,0],[4,0,5,6],[7,8,9,10]]

idx1 = 0
idx2 = 0
M = len(matrix)
N = len(matrix[0])
if M > N:
    max_ = M
else:
    max_ = N
while (idx1 + idx2) != (max_ + 1):
    if matrix[idx1][idx2] == 0:
        for i in range(N):
            matrix[idx1][i] = 0
        for j in range(M):
            matrix[j][idx2] = 0

        idx2 += 2
        idx1 += 1
        if idx2 >= N:
            idx2 = 0
    else:
        idx2 += 1
        if idx2 >= N:
            idx1 += 1
            idx2 = 0

print(matrix)
