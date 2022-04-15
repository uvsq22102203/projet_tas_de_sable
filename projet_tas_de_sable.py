#######################################################
# Groupe  BITD04
# Léa GALLOIS
# Lucas TOURNOUX
# Vianney MOURLON
# Nhu LE
# https://github.com/uvsq22107184/projet_tas_de_sable
######################################################
#projet "jeu de taquin"


#import de librairies
import tkinter as tk
import random as rd

from setuptools import Command



#definition des constantes
LARGEUR = 600
HAUTEUR = 400


#####################################################
#fonctions
def sauvegarde():
    pass

def recharge():
    pass
def undo():
    pass

#definition des widgets
racine = tk.Tk()
racine.title("Jeu de taquin")
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg="black")
bouton_sauv=tk.Button(racine, text="sauvegarder", command= sauvegarde)
bouton_rechar=tk.Button(racine, text="Recharger",command = recharge)
bouton_undo= tk.Button(racine, text="Undo", command = undo)



#placement des widgets

bouton_undo.grid(row= 0, column =0)
bouton_sauv.grid(row = 0, column=1)
bouton_rechar.grid(row=0, column=2)

canvas.grid(row = 1, column=0,columnspan=3)


#boucle principale
racine.mainloop()

