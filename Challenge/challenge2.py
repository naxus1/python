a = 25
cont = 0

while(str(a).__len__() > 1):
    string_a = str(a)
    b = 1
    for word in string_a:
        b = b * int(word)
    a = b
    cont += 1

print(cont)



