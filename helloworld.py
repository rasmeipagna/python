def main ():
    #creation d'une variable 'usename' ayant pour valeur le mot 'Pagna'
    username = "Pagna"
    username = "Youtube"
    #creation d'une variable 'age' ayant pour valeur '32'
    age = 32
    #le porte monnaie
    wallet = 125.7
    #booléen true/false
    is_happy = True
    #affiche la valeur du username et l'age
    print(username, age)
    #change la valeur de age de 32 à 25
    age = 25
    print(age)
    age = age + 1
    print(age)
    print("Salut " + username + ", vous avez " + str(age) + " ans !")


if __name__=='__main__':
    main()