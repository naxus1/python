"""
Exercise for calculate the least common multiple
"""

def mcm (num1, num2):
    num_max = max(num1, num2)
    while True:
        if (num_max % num1 == 0) and (num_max % num2 == 0):
            return(num_max)
        num_max += 1
print(mcm(2, 4))
print(mcm(4, 6))
print(mcm(24, 36))