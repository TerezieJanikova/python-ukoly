import pandas as pd
import json

# Načtení dat
df = pd.read_csv('netflix_titles.tsv', sep='\t', dtype=str)

# Vybereme jen požadované sloupce
df = df[['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']]

# Výstupní seznam
output = []

# Projdeme každý řádek tabulky
for index, row in df.iterrows():
    # Název filmu
    title = row['PRIMARYTITLE']

    # Zpracování režisérů
    if pd.isna(row['DIRECTOR']) or row['DIRECTOR'].strip() == '':
        directors = []
    else:
        directors = []
        for director in row['DIRECTOR'].split(','):
            director = director.strip()
            if director != '':
                directors.append(director)

    # Zpracování herců
    if pd.isna(row['CAST']) or row['CAST'].strip() == '':
        cast = []
    else:
        cast = []
        for actor in row['CAST'].split(','):
            actor = actor.strip()
            if actor != '':
                cast.append(actor)

    # Zpracování žánrů
    if pd.isna(row['GENRES']) or row['GENRES'].strip() == '':
        genres = []
    else:
        genres = []
        for genre in row['GENRES'].split(','):
            genre = genre.strip()
            if genre != '':
                genres.append(genre)

    # Výpočet dekády
    if pd.isna(row['STARTYEAR']) or not row['STARTYEAR'].isdigit():
        decade = None
    else:
        year = int(row['STARTYEAR'])
        decade = (year // 10) * 10

    # Sestavení slovníku pro film
    record = {
        "title": title,
        "directors": directors,
        "cast": cast,
        "genres": genres,
        "decade": decade
    }

    # Přidání do výstupního seznamu
    output.append(record)

# Uložení do JSON souboru
with open('hw02_output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)