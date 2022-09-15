#créer une liste ui va stocker des pseudos pour simuler un jeu en ligne
online_players = ["Pagna","Anana","Cleymax","Bob"]
print(online_players)
print(online_players[0])
print(online_players[2])
#ou
print(online_players[len(online_players) - 1])

#modifier 'Pagna' ->'Rasmeipagna'
online_players[0] = "Rasmeipagna"

online_players[2:4] = ["Paul", "Jacques"]
print(online_players[2:4])

#en ajouter d'autres
online_players.append("Gamer123")
online_players.extend(["Gogum1er"])

#virer un joueur
del online_players[1]
#ou
online_players.remove("Paul")
#ou
online_players.clear("Paul")


print(online_players)

#exemple : jouer à la maitresse

notes = [8, 12, 10, 9, 4, 20]
print(notes)
