

# Classe permettant d'instancier la boutique
class Boutique:
    def __init__(self):
        # {objet : [prix, quantité]}
        self.contenu = {
            "potion de soin mineur" : [10, 99],
            "potion de soin" : [100, 99],
            "potion de soin majeur" : [1000, 99],
            "potion de mana mineur" : [10, 99],
            "potion de mana" : [100, 99],
            "potion de mana majeur" : [1000, 99]
        }
    
    def affichageBoutique(self) :
        print("--------------------\nObjet : prix (quantité)\n--------------------")
        for key,value in self.contenu.items() :
            print(key, ":", value[0], "pièces d'or (" + str(value[1]) + ")")
        print("--------------------")

    def acheterObjet(self, heros) :
        
        print("Bourse du joueur :", heros.bourse, "pièces d'or")
        self.affichageBoutique()

        print("RETOUR pour revenir au menu principal")

        achat = ""
        while achat not in self.contenu.keys() and achat != "RETOUR" :
            achat = input("Saisissez le nom exact de l'objet à acheter l'objet à acheter\n")

        if achat.upper == "RETOUR" :
            return

        quantite = -1
        while not quantite >= 0:
            quantite = input("Veuillez entrer la quantite de " + achat + " a acheter\n")
            try :
                quantite = int(quantite)
            except :
                print(quantite, "- N'est pas un nombre valide")
                pass
            if self.contenu[achat][1] >= quantite and heros.bourse >= quantite*self.contenu[achat][0] :
                self.contenu[achat][1] -= quantite
                heros.bourse -= quantite*self.contenu[achat][0]
            else :
                print("Achat impossible")
                break
