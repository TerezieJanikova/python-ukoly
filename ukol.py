import json

# Přečtení obsahu souboru
with open("alice.txt", mode="r", encoding="utf-8") as file:
    data = file.read()

# Spočítání četnosti znaků (velká písmena jako malá, ignorování mezer a nových řádků)
pocet_znaku = {}
for znak in data:
    if znak not in [' ', '\n']:  # Ignorovat mezery a nové řádky
        znak = znak.lower()  # Převedu všechny písmena na malé
        if znak in pocet_znaku:
            pocet_znaku[znak] += 1
        else:
            pocet_znaku[znak] = 1

# Seřazení slovníku
serazeny_slovnik_znaku = dict(sorted(pocet_znaku.items()))

# Uložení slovníku do JSON souboru
with open("janikova_terezie_hw01_.json", mode="w", encoding="utf-8") as json_file:
    json.dump(serazeny_slovnik_znaku, json_file, indent=4, ensure_ascii=False)
