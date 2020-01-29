employeds = [['Jack Nelson', 32, 'Sales'],
            ['Paola Gonzalez', 33, 'Service'],
            ['Oscar', 36, 'Customer']
            ]
for employ in employeds:
    print(employ)

print("-"*10)

for employ in employeds:
    print("Nombre: {}".format(employ[0])),
    print("Age: {}".format(employ[1])),
    print("Department: {}".format(employ[2]))
    print("*" * 20)