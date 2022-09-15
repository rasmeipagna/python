from statistics import mean
from random import shuffle
#créer une liste ui va stocker des pseudos pour simuler un jeu en ligne
online_players = ["Pagna","Anana","Cleymax","Bob"]

#que le joueur Anana de deconnecte
online_players.remove("Bob")
#supprimer tous les elements de votre liste
online_players.clear()

print(online_players)


#exemple : jouer à la maitresse

notes = [8, 12, 10, 9, 4, 20, 14, 3]
print(notes)
shuffle(notes)
print(notes)

#module : statistics
result = mean(notes)
print("La moyenne de l'eleve est {}".format(result))
