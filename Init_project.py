lista_zakupów = {"piekarnia": ["chleb", "pączek", "bułki",],
                "warzywniak": ["marchew", "seler", "rukola",]}


for sklep, rzeczy in lista_zakupów.items():
    rzeczy = [i.capitalize() for i in rzeczy]
    print(f"idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {rzeczy}")



sum = 0
for i in lista_zakupów.values():
    for z in i:
        sum = sum + 1

print(f"W sumie kupuję {sum} produktów")

list = []

for i in range(101):
    if i % 5 == 0:
        list.append(i)