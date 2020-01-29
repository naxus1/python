import math
import os
import random
import re
import sys

"""
"""

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if n < 0 or n > 100:
        return
         
    count_num = 0
    socks_pair = 0

    set_list = list(set(ar))
    for i in set_list:
        count_num = ar.count(i)
        socks_pair += count_num // 2
    return(socks_pair)


n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)