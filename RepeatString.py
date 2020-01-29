def repeatedString(s, n):
    result = 0
    count_letters = len(s)
    count_begind_a = s.count('a')
    repeat_string = n / count_letters

    if repeat_string % 2 != 0:
        res = n % count_letters
        sub_string = s[:res]
        result = sub_string.count('a')

    return (repeat_string*count_begind_a) + result
        
  

print(repeatedString('bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc', 649606239668))
# print(repeatedString('aab', 882787))
# print(repeatedString('aba', 10))
