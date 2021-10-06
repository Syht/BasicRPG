import math

class Personnage :

    def __init__(self, nom, max_hp, attaque, armure, vitesse) :
        self.nom = nom
        self.max_hp = max_hp
        self.hp = max_hp
        self.attaque = attaque
        self.armure = armure
        self.vitesse = vitesse

class Heros(Personnage) :

    def __init__(self, nom, max_hp, attaque, armure, vitesse, max_mana=20, experience=0, bourse=0) :
        super().__init__(nom, max_hp, attaque, armure, vitesse)
        self.experience = experience
        self.bourse = bourse
        self.max_mana = max_mana
        self.mana = max_mana
        self.inventaire = {}

    def getNiveau(self) :
        niveau = math.floor(math.log2(self.experience/10)) if self.experience > 0 else 1
        return niveau if niveau > 0 else 1

class Monstre(Personnage) :

    def __init__(self, nom, max_hp, attaque, armure, vitesse, niveau=1) :
        super().__init__(nom, max_hp, attaque, armure, vitesse)
        self.niveau = niveau