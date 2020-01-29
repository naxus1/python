a = 'asdfkjeghfalawefhaef'
sort_string = sorted(list(set(a)))
len_s, len_srt = len(sort_string), len(a)

while len_s <= len_srt:
    for i in range(0,len_srt):
        sub_st1 = list(a[i:len_s + i])
        sub_st = sorted(list(set(sub_st1)))
        if sort_string == sub_st:
            print(''.join(sub_st1))
            break
    len_s = len_s + 1

