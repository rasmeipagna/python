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