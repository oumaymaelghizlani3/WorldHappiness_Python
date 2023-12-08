import csv

chemin_fichier_csv = 'WorldHappiness.csv'
liste_donnees = []
dict_moyennes = {}
chemin_fichier_sortie = 'Top10Happiness.csv'

# Sauvegarder dans une liste de listes
with open(chemin_fichier_csv, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)
    for ligne in lecteur_csv:
        liste_donnees.append([ligne['Country'], float(ligne['happiness_score']), float(ligne['freedom']),
                              float(ligne['gdp_per_capita'])])

# Créer un dictionnaire avec les moyennes
for data in liste_donnees:
    country = data[0]
    happiness_score, freedom, gdp_per_capita = data[1:]

    if country not in dict_moyennes:
        dict_moyennes[country] = {'Happiness Score': [], 'Freedom': [], 'GDP': []}

    dict_moyennes[country]['Happiness Score'].append(happiness_score)
    dict_moyennes[country]['Freedom'].append(freedom)
    dict_moyennes[country]['GDP'].append(gdp_per_capita)

# Calculer les moyennes pour chaque pays
for country, values in dict_moyennes.items():
    moyenne_happiness = sum(values['Happiness Score']) / len(values['Happiness Score'])
    moyenne_freedom = sum(values['Freedom']) / len(values['Freedom'])
    moyenne_gdp = sum(values['GDP']) / len(values['GDP'])

    # Mettre à jour le dictionnaire avec les listes de moyennes
    dict_moyennes[country] = [moyenne_happiness, moyenne_freedom, moyenne_gdp]

# Afficher le dictionnaire final des moyennes par pays
print("Dictionnaire des moyennes par pays:")
print(dict_moyennes)

# Trouver le pays avec les meilleures moyennes sur les 6 années
pays_meilleures_moyennes = max(dict_moyennes, key=lambda x: sum(dict_moyennes[x]))
print(f"\nLe pays avec les meilleures moyennes sur les 6 années est : {pays_meilleures_moyennes}")

# Créer une liste de tuples pour le continent, la valeur maximale de CPI et le pays correspondant
max_cpi_par_continent = {}

with open(chemin_fichier_csv, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)

    for ligne in lecteur_csv:
        continent = ligne['continent']
        cpi_score = float(ligne['cpi_score'])
        country = ligne['Country']

        if continent not in max_cpi_par_continent or cpi_score > max_cpi_par_continent[continent][0]:
            max_cpi_par_continent[continent] = (cpi_score, country)

# Créer une liste de tuples contenant le continent, la valeur maximale de CPI et le pays correspondant
liste_max_cpi = [(continent, max_cpi, country) for continent, (max_cpi, country) in max_cpi_par_continent.items()]

# Trouver le maximum de CPI parmi tous les continents
max_cpi_global = max(liste_max_cpi, key=lambda x: x[1])

# Afficher le résultat
print("\nListe des tuples (continent, max CPI, pays correspondant):")
print(liste_max_cpi)
print("\nContinent et pays avec le plus grand CPI:")
print(max_cpi_global[0], max_cpi_global[2])

# Trier la liste des données par le "Happiness Score" de manière décroissante
liste_donnees.sort(key=lambda x: x[1], reverse=True)

# Sélectionner les 10 premiers pays
top_10_pays = liste_donnees[:10]

# Écrire les informations des 10 meilleurs pays dans un nouveau fichier CSV
with open(chemin_fichier_sortie, 'w', newline='', encoding='utf-8') as fichier_csv_sortie:
    champs = ['Country', 'happiness_score', 'freedom', 'gdp_per_capita']
    ecrivain_csv = csv.writer(fichier_csv_sortie)

    # Écrire l'en-tête dans le fichier de sortie
    ecrivain_csv.writerow(champs)

    # Écrire les données des 10 meilleurs pays dans le fichier de sortie
    for pays in top_10_pays:
        ecrivain_csv.writerow(pays)

print(f"Les informations des 10 meilleurs pays ont été sauvegardées dans {chemin_fichier_sortie}.")
