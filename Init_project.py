lista_zakupów = {"piekarnia": ["chleb", "pączek", "bułki",],
                "warzywniak": ["marchew", "seler", "rukola",]}

for sklep, rzeczy in lista_zakupów.items():
    rzeczy = [i.capitalize() for i in rzeczy]
    print(f"idę do {sklep.capitalize()}, kupuję: {rzeczy}")

    sum = 0
for i in lista_zakupów.values():
    sum = len(i)
    sum = sum + sum
print(f"W sumie kupuję {sum} produktów produktów, zjem je wszystkie")

print("Na pewno będą dobre")

print("godzinę później")
print("Zjedłem wszystko, boli mnie brzuch")


