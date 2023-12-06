import csv
chemin_fichier_csv = 'WorldHappiness.csv'

liste_de_listes = []

with open(chemin_fichier_csv, newline='', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv)

    for ligne in lecteur_csv:

        sous_liste = [ligne["Country"]] + list(ligne.values())[1:]

        liste_de_listes.append(sous_liste)

print(liste_de_listes)
