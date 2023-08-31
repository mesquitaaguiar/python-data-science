frutas = ['banana', 'maçã', 'pêra', 'kiwi', 'mamão']

print("Count = {}".format(len(frutas)))

print("Count Kiwi = {}".format(frutas.count("kiwi")))

frutas.sort()
print("Sort Frutas = {}".format(frutas))

frutas.append("uva")
frutas.insert(0,"laranja")
print("Append Frutas = {}".format(frutas))

print("Posição Banana = {}".format(frutas.index("banana")))

frutas.sort()
frutas.reverse()
print("Reverse Frutas = {}".format(frutas))

frutas.remove("banana")
frutas.sort()
print("Frutas = {}".format(frutas))

print("Frutas = {}".format(frutas[-4:4:1]))