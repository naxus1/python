"""
Addition Matrix
"""

x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

y = [[10, 11, 12],
    [13, 14 , 15],
    [16, 17, 18]]
    
# Initialize a result placeholder
result = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
]

#iterate trought rows
for i in range(len(x)):
# Iterate trought columns
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]
print(result)