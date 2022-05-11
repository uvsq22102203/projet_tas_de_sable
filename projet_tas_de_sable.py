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


#definition des constances
LARGEUR = 400
HAUTEUR = 400


#Matrice en 2D du damier
matrice =[[0,1,2,3],
        [4,5,6,7],
        [8,9,10,11],
        [12,13,14,15]]



#####################################################
#Fonctions
#Deplacement du case
def clic(event):
    """Gestion du clic"""
    global i_vide, j_vide
    #coordonnees du clic
    i = event.x // 100
    j = event.y // 100
    case, num = id[matrice[j][i]]

    #lecture de la  position du case
    print("ligne = ", i, "colonne = ", j, matrice[i][j])   #ref: pascal.ortiz

    #movement des cases
    if i + 1 == j_vide and j == i_vide: 
        """deplacevers la droite"""
        canvas.move(case, 100, 0)
        canvas.move(num, 100, 0)
    elif i - 1 == j_vide and j == i_vide:
        """deplace vers la gauche"""
        canvas.move(case, -100, 0)
        canvas.move(num, -100, 0)
    elif i == j_vide and j + 1 == i_vide:
        """deplacement vers le haut"""
        canvas.move(case, 0, 100)
        canvas.move(num, 0, 100)
    elif i == j_vide and j - 1 == i_vide:
        """deplace vers le bas"""
        canvas.move(case, 0, -100)
        canvas.move(num, 0, -100)
    else:
        """pas de case vide approximite"""
        return - 1
    matrice[j][i] , matrice[i_vide][j_vide] = matrice[j_vide][i_vide], matrice[j][i]
    i_vide = j
    j_vide = i

#ref: pascal.ortiz pour la parite de la fonction melange
def voisines(n, i, j):
    """listes des voisines de la case vide"""
    return [(a,b) for (a,b) in [(i, j +1), (i, j- 1), (i-1, j), (i+1,j)] if a in range(n) and b in range(n)]

def echange(matrice,empty):
    i,j = empty
    V  = voisines(4, i, j)
    ii, jj = V[rd.randrange(len(V))]       #choisir une parmi 4 voisines de la case vide au hasard
    matrice[jj][ii], matrice[j][i] = matrice[j][i], matrice[jj][ii]
    return jj, ii

def melange(N):                            #N nomdre d'echanges entre la case vide et une de ses 4 voisine
    matrice= [[4*lin+1*col for col in range(4)] for lin in range(4)]
    print(*matrice, sep='\n')             #creation un plateau rempli avec les entiters de 0 a 15
    empty = (3,3)                         #position de la case vide
    for i in range(N):
        """echange de la case vide et une de ses voisines"""
        empty = echange(matrice, empty)
        print(*matrice, sep ='\n')
melange(1000)


def retourn():
    pass

####################################################

#definition des widgets
racine = tk.Tk()
racine.title("Jeu de taquin")
canvas = tk.Canvas(racine, width= LARGEUR, height= HAUTEUR, bg="black")
bouton_mel=tk.Button(racine, text="Melanger",command = melange)
bouton_ret= tk.Button(racine, text="retourner", command = retourn)


#definition du damier

id = [None for i in range(17)]                #ref: pascal.ortiz

for i in range(4): 
    for j in range (4):
        """coordonnees x,y d'un cadre"""
        x,  y = i*100, j*100
        case = canvas.create_rectangle((x,y), (x+100, y+100), fill = "white")

        """numero au milieu du cadre"""
        num = canvas.create_text((x+50, y+50),fill="black", font="arial", text= matrice[j][i])

        #id de chaque case
        id[matrice[j][i]] = (case, num)       #ref: pascal.ortiz


#Gestionnaire d'evenement
canvas.bind("<Button-1>",clic)

#case vide
canvas.delete(case,num)

#Coordonnees du case vide
i_vide = 3
j_vide = 3

#placement des widgets
bouton_ret.grid(row= 0, column =0)
bouton_mel.grid(row=0, column=2)


canvas.grid(row = 1, column=0,columnspan=3)

#boucle principale
racine.mainloop()

