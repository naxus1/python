

def calculate_jump(c):

    n = len(c)
    res = 0
    i = 0
    while i < n-1:
        if i+2<n and c[i+2] == 0:
            i = i+2
            res += 1
        else:
            i = i+1
            res += 1
    return(res)

    

print('-' * 10)
print(calculate_jump([0, 0, 1, 0, 0, 0, 0, 1, 0, 0])) #6
# print('-' * 10)
print(calculate_jump([0, 0, 1, 0, 0, 1, 0])) #4
# print('-' * 10)
print(calculate_jump([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])) #53





#Misolucion1
# def calculate_jump(c):
#     jump, cont, index = 0, 0, 0
#     recorrido = 2 if (len(c) - 1)%2 == 0 else 3


#     while index < len(c)-1:
#             if c[index + 2] != 1:
                
#                 jump = 2 + jump
#                 index = jump
#                 cont += 1
#             elif  c[index + 1] != 1:
#                 jump = 1 + jump
#                 index = jump
#                 cont += 1
#     num = 1 if (len(c) - 1)%2 else 0
#     return(cont + num)