def analyser_phrases(phrases):

    #  Nettoyage + découpage
    liste_mots = []
    for p in phrases:
        p = p.strip()          
        p = p.lower()         
        mots = p.split()       

        for m in mots:
            liste_mots.append(m)

    #  Ensemble des mots uniques
    mots_uniques = set(liste_mots)

    #  Total des mots
    total_mots = len(liste_mots)

    #  Total des mots uniques
    total_uniques = len(mots_uniques)

    #  Mot le plus long
    mot_plus_long = ""
    for m in mots_uniques:
        if len(m) > len(mot_plus_long):
            mot_plus_long = m

    #  Mot le plus fréquent
    mot_freq = ""
    max_count = 0
    for m in liste_mots:
        if liste_mots.count(m) > max_count:
            max_count = liste_mots.count(m)
            mot_freq = m

    #  Retourner les résultats
    return total_mots, total_uniques, mot_plus_long, len(mot_plus_long), mot_freq



phrases = []

n = int(input("Combien de phrases voulez-vous saisir ? "))

for i in range(n):
    phrase = input(f"Entrez la phrase {i+1} : ")
    phrases.append(phrase)

# afficher résultat
print(analyser_phrases(phrases))