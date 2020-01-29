
sentence = "Hello Perfect World in the world forever"
col = 7
a = sentence.replace(" ", "")

i, jump = 0, col

while i < len(a) - 1:
    if (i < len(a) - 1):
        print(a[i:jump])
        i += col
        jump += col
print(a[i:])