"""
Implementing Matrix Operations Addition and Substraction
"""

x = [[1,2,3],
    [4,5,6],
    [7,8,9]]

y = [[9,10,11],
    [12,13,14],
    [15,16,17]]

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range (len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
print(result)

for i in range(len(x)):
    for j in range (len(x[0])):
        result[i][j] = x[i][j] - y[i][j]
print(result)