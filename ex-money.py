def main():
    #recolter une valeur porte monnaie
    wallet= int(input("Entrez le nombre d'€ que vous possédez"))
    print("Vous avez actuellement", wallet, "euros")
    #creer un produit qui aura pour valeur 50
    produit = 50
    print("Le produit vaut", produit, "euros")
    #afficher la nouvelle valeur du porte monnaie, apres son achat

    wallet = wallet - produit
    print("Produit acheté ! ")
    print ("Il ne vous reste plus que", wallet, "euros")

if __name__=='__main__':
    main() 