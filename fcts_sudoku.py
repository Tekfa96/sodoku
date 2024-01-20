#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Programme Sudoku
fait le 07/01/2020
Python 3.6.9
"""

import numpy as np
import time

# ============================================================================
# Classes
# ============================================================================
class Sudoku():
    """
    Permet de définir et résoudre un sudoku
    """

    def __init__(self, data):
        """
        initialise le sudoku
        """
        self.tableau = data # tableau initiale - celui à résoudre
        self.solution = np.zeros((9, 9)) # initialisation - tableau solution
        self.iteration = 0 # nb d'itérations avant résultat final

#        self.solve()
    def __repr__(self):
        """
        permet d'affichier le tableau initiale et la solution
        """
        txt = ""
        txt += "\nTableau initial\n"
        txt += repr_tab(self.tableau)
        txt += "\nSolution\n"
        txt += repr_tab(self.solution)
        txt += "\nNb d'itérations : " + str(self.iteration)
        return txt

    def ligne(self, i):
        """
        liste des nb dans une ligne
        """
        return self.solution[i, :]

    def colonne(self, j):
        """
        liste des nb dans une colonne
        """
        return self.solution[:, j]

    def pos_carre(self, i, j):
        """
        retourne la position d'un sous tableau sudoku
        """
        return 3*(i//3), 3*(j//3)

    def carre(self, i, j):
        """
        retourne l'ensemble de nb d'un sous tableau
        """
        pos_i, pos_j = self.pos_carre(i, j)
        sous_tableau = self.solution[pos_i:pos_i+3, pos_j:pos_j+3]
        return sous_tableau

    def presence_valeur(self, i, j, val):
        """
        test booleen pour savoir si un chiffre est déjà dans le tableau
        """
        return (val in self.ligne(i)) \
                or (val in self.colonne(j)) \
                or (val in self.carre(i, j))

    def case_vide(self, i, j):
        """
        test pour savoir si la case est rempli ou non
        """
        return self.tableau[i, j] == 0

    def avance(self, i, j, val):
        """
        détermine les indices de la case suivante pour la recherche
        """
        # on avance
        j = j+1
        val = 1
        if j > 9:
            i = i+1
            j = 1
        return i, j, val

    def recule(self, i, j, val):
        """
        détermine les indices de la case précédente pour la recherche
        """
        # on recule
        j = j-1
        if j < 0:
            j = 8
            i = i-1
        # on efface la valeur precedente
        # puis on teste la valeur suivante
        val = self.solution[i, j]+1
        if self.case_vide(i, j):
            self.solution[i, j] = 0
        else:
            i, j, val = self.recule(i, j, val)
        return i, j, val


    def deplacement(self, i, j, val):
        """
        gère le suivi de la case de recherche
        """
        if val < 10:
#            print "en avant"
            return self.avance(i, j, val)
        else:
#            print "en arrière"
            return self.recule(i, j, val)

    def solve(self):
        """
        resolution récursive du sudoku
        ne gère pas les sudokus sans solution
        """
        self.solution = np.copy(self.tableau)
        # on parcours tout le self.tableau
        i = 0
        while i < 9:
            j = 0
            val = 1
            while j < 9:
                # on teste toutes les valeurs
                if self.case_vide(i, j) and val < 10:
                    if self.presence_valeur(i, j, val):
                        val = val+1
                    else:
                        self.solution[i, j] = val
                        self.iteration = self.iteration + 1
#                        affiche_tab(self.solution)
#                        time.sleep(0.1)
                        i, j, val = self.deplacement(i, j, val)
                else:
                    i, j, val = self.deplacement(i, j, val)
            i = i + 1

# ============================================================================
# Fonctions
# ============================================================================
def repr_tab(tableau):
    """
     représente le sudoku en console
     """
    txt = ""
    i, j = 0, 0
    for i in range(9):
        if i%3 == 0:
            txt += "-------------------------\n"
        for j in range(9):
            if j%3 == 0:
                txt += "| "
            if tableau[i, j] == 0:
                txt += "_ "
            else:
                txt += str(tableau[i, j]) + " "
        txt += "|\n"
    txt += "-------------------------"
    return txt
    
# ============================================================================
# Programme
# ============================================================================

if __name__ == '__main__':

#    tab_inconnu = [[0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0]]

#    tab_inconnu = [[3,1,4,0,7,6,8,0,0],
#                   [0,6,5,0,4,3,0,7,0],
#                   [9,0,0,8,0,0,0,0,3],
#                   [0,0,2,6,0,0,0,8,0],
#                   [0,3,9,0,8,0,2,6,0],
#                   [0,8,0,0,0,7,5,0,0],
#                   [5,0,0,0,0,2,0,0,7],
#                   [0,4,0,7,1,0,9,5,0],
#                   [0,0,6,5,9,0,0,0,8]]

#    tab_inconnu = [[0,2,0,1,0,0,0,0,0],
#                   [0,0,5,0,2,0,4,0,0],
#                   [1,3,0,0,4,8,0,0,0],
#                   [0,6,0,0,8,0,0,0,1],
#                   [0,1,0,2,0,4,0,9,0],
#                   [4,0,0,0,7,0,0,2,0],
#                   [0,0,0,8,9,0,0,5,2],
#                   [0,0,9,0,1,0,6,0,0],
#                   [0,0,0,0,0,6,0,7,0]]

    tab_inconnu = [[1,0,0,0,0,7,0,9,0],
                   [0,3,0,0,2,0,0,0,8],
                   [0,0,9,6,0,0,5,0,0],
                   [0,0,5,3,0,0,9,0,0],
                   [0,1,0,0,8,0,0,0,2],
                   [6,0,0,0,0,4,0,0,0],
                   [3,0,0,0,0,0,0,1,0],
                   [0,4,0,0,0,0,0,0,7],
                   [0,0,7,0,0,0,3,0,0]]

    tab_inconnu = np.array(tab_inconnu)
    mSudok = Sudoku(tab_inconnu)
    start_time = time.time()
    mSudok.solve()
    elapsed_time = time.time() - start_time
    print(mSudok)
    print("Temps de calcul : ",round(elapsed_time,3), " s")
