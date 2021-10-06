from personnage import *
import random, math, re, os

class FinDePartieException(Exception):
    def __init__(self):
        super().__init__("FIN DE LA PARTIE")


class Combat:
    def __init__(self, personnage1, personnage2):
        self.personnage1 = personnage1 if personnage1.vitesse >= personnage2.vitesse else personnage2
        self.personnage2 = personnage2 if personnage2.vitesse <= personnage1.vitesse else personnage1

    def combattre(self):
        tour = 1
        print("=======================================================")
        print("Que le combat commence !",
              self.personnage1.nom, "contre", self.personnage2.nom)
        print("=======================================================")

        try:
            while self.personnage1.hp > 0 and self.personnage2.hp > 0:
                print("***** Début du tour", tour, "*****")
                if tour % 2 != 0:
                    if isinstance(self.personnage1, Heros):
                        gestionTourHeros(self.personnage1, self.personnage2)
                    else:
                        calculDegats(self.personnage1, self.personnage2)
                else:
                    if isinstance(self.personnage2, Heros):
                        gestionTourHeros(self.personnage2, self.personnage1)
                    else:
                        calculDegats(self.personnage2, self.personnage1)
                tour += 1

                if self.personnage1.hp < 0:
                    self.personnage1.hp = 0
                if self.personnage2.hp < 0:
                    self.personnage2.hp = 0

                print(self.personnage1.nom,
                      "a", self.personnage1.hp, "points de vie")
                print(self.personnage2.nom,
                      "a", self.personnage2.hp, "points de vie")

            if self.personnage1.hp == 0:
                gagnant = self.personnage2
                perdant = self.personnage1
            else:
                gagnant = self.personnage1
                perdant = self.personnage2

            print("=======================================================")
            print("Le combat est terminé,",
                  gagnant.nom, "est victorieux !")
            print("=======================================================")

            if isinstance(gagnant, Heros):
                calculRecompenses(gagnant, perdant)

        except FinDePartieException:
            print("=======================================================")
            print("Le combat est terminé")
            print("=======================================================")
        finally:
            if isinstance(self.personnage1, Heros):
                heros = self.personnage1
            else:
                heros = self.personnage2

            heros.hp = heros.max_hp
            heros.mana = heros.max_mana
            save(heros)


def calculDegats(attaquant, defenseur, magie=False):
    randomized_attaque = random.randint(
        math.ceil(attaquant.attaque*0.4), attaquant.attaque)
    if magie:
        degats = randomized_attaque if randomized_attaque > 0 else 1
        attaquant.mana -= 5
    else:
        degats = randomized_attaque - \
            defenseur.armure if randomized_attaque - defenseur.armure > 0 else 1
    print(attaquant.nom, "a infligé", degats,
          "points de dégâts à", defenseur.nom)
    defenseur.hp -= degats


def calculRecompenses(heros, monstre):
    gain_pieces = random.randint(1, (10 + monstre.niveau) ^ 2)
    gain_xp_temp = random.randint(math.floor(
        monstre.niveau*0.9), math.ceil(monstre.niveau*1.1))
    gain_xp = gain_xp_temp if gain_xp_temp > 0 else 1
    heros.bourse += gain_pieces
    heros.experience += gain_xp
    print(heros.nom, "a gagné", gain_pieces,
          "pièces d'or et", gain_xp, "points d'expériences")


def gestionTourHeros(heros, monstre):
    choix = ""
    while (choix != "1" and choix != "2" and choix != "3" and choix != "4"):
        choix = input(
            "Saisir l'action à effectuer\n1) Attaquer\n2) Magie\n3) Inventaire\n4) Fuir\n")
        if choix == "2" and heros.mana < 5:
            print("Vous n'avez pas assez de mana (" + str(heros.mana) + "/" +
                  str(heros.max_mana) + "), veuillez choisir une autre action")
            choix = ""
        elif choix == "3":
            choix = input(
                "Saisir l'action à effectuer\n1) Attaquer\n2) Magie\n3) Inventaire\n4) Fuir\n")

    if choix == "1":
        calculDegats(heros, monstre)
    elif choix == "2":
        calculDegats(heros, monstre, True)
    elif choix == "4":
        if random.randint(1, 100) > 50:
            print("------------------------------")
            print("Vous prenez la fuite")
            print("------------------------------")
            raise FinDePartieException
        else:
            print("------------------------------")
            print("Fuite impossible !")
            print("------------------------------")


def save(heros):
    list_temp_saves = []
    heros_existant = False
    heros_string = heros.nom + "|" + str(heros.max_hp) + "|" + str(heros.attaque) + "|" + str(heros.armure) + "|" + str(heros.vitesse) + "|" + str(heros.max_mana) + "|" + str(heros.experience) + "|" + str(heros.bourse) + "\n"
    with open("projetRPG/saves/data.save", "r+") as save:
        try:
            for ligne in save :
                if heros.nom == re.split("\|", ligne)[0] :
                    list_temp_saves.append(heros_string)
                    heros_existant = True
                elif len(ligne) != 0 :
                    list_temp_saves.append(ligne)
            if not heros_existant :
                list_temp_saves.append(heros_string)
            
            save.truncate(0)
            save.seek(0)
            for saved_line in list_temp_saves :
                save.write(saved_line)
        except:
            save.write(heros_string)

def load(nom):
    with open("projetRPG/saves/data.save", "r+") as save:
        try:
            for ligne in save :
                if nom == re.split("\|", ligne)[0] :
                    infos = re.split("\|", ligne)
                    return Heros(infos[0], int(infos[1]), int(infos[2]), int(infos[3]), int(infos[4]), int(infos[5]), int(infos[6]), int(infos[7]))
        except:
            print("Aucune données à charger")