"""
Real state ofert for house
"""

print("Una casa en el área de Bahia esta listada en $599,000")
print("Ingrese su primera oferta por la casa")

offert = abs(int(input()))
print("Ingrese su mejor oferta por la casa")
best_offert = abs(int(input()))
print("Cuanto mas quieres ofrecer cada vez")
increment = abs(int(input()))
offert_accepted = False

while offert <= best_offert:
    if offert >= 650000:
        offert_accepted = True
        print('Your offer has been accepted!')
        break
    else:
        print("We\'re sorry, you\'re offer of", offert, "has not been accepted")
        offert += increment
