nombre = int(input("Entrez un nombre entier supérieur à 1 : "))
diviseurs = []
for i in range(2, nombre):
    if nombre % i == 0:
        diviseurs.append(i)
if diviseurs:
    print("Les diviseurs de", nombre, "sont :", diviseurs)
else:
    print(nombre, "Premier")