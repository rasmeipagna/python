def main ():
    #recolter une premiere note
    note1 = int(input("Entrer la premiere note"))
    #recolter la deuxieme note
    note2 = int(input("Entrer la seconde note"))
    #recolter la derniere note
    note3 = int(input("Entrer la derniere note"))
    #calculer la moyenne
    result = (note1 + note2 + note3)/ 3
    #afficher le resultat
    print("La moyenne de l'eleve est de " + str(result))


if __name__=='__main__':
    main()