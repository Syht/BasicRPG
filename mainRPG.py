from personnage import *
from combat import *
from boutique import *
import re

#heros = Heros("Syht Rhonel", max_hp=420, attaque=53, armure=27, vitesse=12)
heros = load("Syht Rhonel")
monstre = Monstre("Kobold gris", max_hp=2, attaque=41, armure=19, niveau=20, vitesse=12)
boutique = Boutique()

# nom_heros = ""
# while not re.fullmatch("^[a-zA-Z0-9][ '\-a-zA-Z0-9]+[a-zA-Z0-9]$", nom_heros) :
#     nom_heros = input("---======---\nChoisissez le nom de votre héros\n---======---\n")

# heros = load(nom_heros)

# if not heros :
#     heros = Heros(nom_heros, max_hp=420, attaque=53, armure=27, vitesse=12)

print("`````````````````` Bienvenue aventurier ! ``````````````````")
choix = ""
while choix != "1" and choix != "2" and choix != "3":
    choix = input(
        "1) Combattre\n2) Boutique\n3) Quitter\n")
    if choix == "1" :
        combat = Combat(heros, monstre)
        combat.combattre()
    elif choix == "2" :
        boutique.acheterObjet(heros)
    elif choix == "3" :
        break
    
    choix = "" if choix == "1" or choix == "2" else choix

print("`````````````````` Au revoir aventurier ``````````````````")

