a = [1,1,1,0,1,1,1,1]
#a = [1,0,0,0,0,1,0,0]
b = []
largo = len(a)
j = 0
day = 2

while j < day:

    if j > 0:
        a = b
        b = []

    for i in range(largo):
        pos_act = i
        if pos_act == 0:
            b.append(0 if a[i+1] == 0 else 1)
        elif pos_act == largo-1:
            b.append(0 if a[i-1] == 0 else 1)
        elif a[i-1] == a[i+1]:
            b.append(0)
        else:
            b.append(1)
    j += 1
print(b)
        