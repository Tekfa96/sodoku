#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Résoud des sudokus - interface
Python 3.6.9
"""

from fcts_sudoku import Sudoku
import tkinter
import numpy as np

# ============================================================================
# Classes
# ============================================================================
class Interface():
    """
    Définit l'interface du jeu sudoku
    """
    
    def __init__(self):
        """
        initialisation
        """
        # fenetre
        self.fenetre=tkinter.Tk()
        self.fenetre.title("Résolveur de Sudoku")
        self.fenetre.wm_attributes("-topmost", 1) # toujours au dessus
        
        # boutons
        self.bResoudre=tkinter.Button(self.fenetre, text = 'Résoudre', \
                            font=("Calibri",24), command = self.fResoudre)
        self.bResoudre.grid(column=0,row=10,columnspan=3)
        self.bRelancer=tkinter.Button(self.fenetre, text = 'Nouveau', \
                            font=("Calibri",24), command = self.fNouveau)
        self.bRelancer.grid(column=3,row=10,columnspan=3)
        self.bQuitter=tkinter.Button(self.fenetre, text = 'Quitter', \
                            font=("Calibri",24), command = self.fQuitter )
        self.bQuitter.grid(column=6,row=10,columnspan=3)
        
        # creation des 9x9 cases
        self.fcreation_entree()
    
    def start(self):
        """
        lance le jeu
        """
        self.fenetre.mainloop()
                
    def fcreation_entree(self):
        """
        initialisation des entrees (Entry) et ajout a la fenetre
        """
        self.entree = []
        for i in range(9):
            self.entree+=[[]]
            for j in range(9):
                self.entree[i]+=[tkinter.StringVar()]
        for i in range(9):
            for j in range(9):
                if (i//3==0 and j//3==0) or (i//3==0 and j//3==2) or (i//3==2 and j//3==0) or (i//3==2 and j//3==2) or (i//3==1 and j//3==1):
                    tkinter.Entry(self.fenetre, textvariable = self.entree[i][j], \
                                    width=3,font=("Calibri",24), justify='center', bg="#8b9dc3" \
                                    ).grid(row=i, column=j)
                else:
                    tkinter.Entry(self.fenetre, textvariable = self.entree[i][j], \
                                    width=3,font=("Calibri",24), justify='center', bg="#dfe3ee" \
                                    ).grid(row=i, column=j)
                self.entree[i][j].set( "")
                
    def fQuitter(self):
        """
        quitter l'application
        """
        self.fenetre.destroy()
        return
    
    def fResoudre(self):
        """
        résoud le sudoku et affiche la solution
        ne gère pas les sudoku sans solution
        """
        # on recupere les valeurs
        tableau = np.zeros((9, 9))
        for i in range(9):
            for j in range(9):
                val=self.entree[i][j].get()
                if isValid(val):
                    val=int(val)
                else:
                    val=0
                tableau[i,j]=val
        # on resoud le sudoku
        mSudok = Sudoku(tableau)
        mSudok.solve()
        
        # on affiche la solution
        for i in range(9):
            for j in range(9):
                self.entree[i][j].set( str(int(mSudok.solution[i, j])))
        return
    
    def fNouveau(self):
        """
        on reinitialise le tableau d'entrees (Entry)
        """
        for i in range(9):
            for j in range(9):
                self.entree[i][j].set( "")
        return
# ============================================================================
# Fonctions
# ============================================================================
def isValid(val):
    """
    test la valeur dans les cases
    - vrai si nombre entier entre 1 et 10
    - faux sinon
    """
    try:
        val=int(val)
        if val>0 and val<10:
            return True
        else:
            return False
    except:
        return False
# ============================================================================
# Programme
# ============================================================================

if __name__ == '__main__':
    Jeu=Interface()
    Jeu.start()



