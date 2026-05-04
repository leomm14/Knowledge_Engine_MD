import csv

def clean(s):
    if not s or s.strip() == "":
        return "unknown"
    return (
        s.lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("'", "")
        .replace("é", "e")
        .replace("í", "i")
        .replace("á", "a")
        .replace("ó", "o")
        .replace("ú", "u")
    )

# --- PERSONAGENS ---
def gerar_personagens():
    with open('characters.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nome = clean(row['name'])
            especie = clean(row['species'])
            planeta = clean(row['homeworld'])

            print(f"personagem({nome}, {especie}, {planeta}).")

# --- PLANETAS ---
def gerar_planetas():
    with open('planets.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nome = clean(row['name'])
            populacao = row['population']

            if not populacao or not populacao.isdigit():
                populacao = "0"

            print(f"planeta({nome}, {populacao}).")

# --- ESPECIES ---
def gerar_especies():
    with open('species.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nome = clean(row['name'])
            classificacao = clean(row['classification'])
            lifespan = row['average_lifespan']

            # tratar valores desconhecidos
            if not lifespan or lifespan == 'unknown':
                continue  # ou pode usar 0 se preferir

            print(f"especie({nome}, {classificacao}, {lifespan}).")

# --- EXECUTAR TUDO ---
print("%%% PERSONAGENS %%%")
gerar_personagens()

print("\n%%% PLANETAS %%%")
gerar_planetas()

print("\n%%% ESPECIES %%%")
gerar_especies()