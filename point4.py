a = []
c = []
for i in range(int(input())):
    name = input()
    score = float(input())
    a.append([score, name])

b = sorted(a)
print("--"*10)
print(b)
note_med = (b[1][0])
max_num = (b[0][0])
print(max_num)

for num, name in b:
    if num < max_num:
        c.append(b[name])
        break
print(c)

















# for val, name in b:
#     if note_med == val and note_med != max_num :
#         c.append(name)

# c = sorted(c)

# for position, name in enumerate(c):
#     print(c[position])