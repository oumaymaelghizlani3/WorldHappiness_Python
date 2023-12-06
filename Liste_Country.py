import csv
chemin_fichier_csv = 'WorldHappiness.csv'
liste_de_listes = []

with open(chemin_fichier_csv, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)
    # Sauvegarder dans une liste de listes toutes ses données où le premier élément des sous listes est le « Country » les autres éléments contient toutes les informations du country.
    for ligne in lecteur_csv:

        sous_liste = [ligne["Country"]] + list(ligne.values())[1:]

        liste_de_listes.append(sous_liste)

print(liste_de_listes)
