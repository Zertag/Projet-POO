'''
Fichier Contenant le comportement des différentes pièces du jeu
'''


class Piece:

    def __init__(self, couleur=None, coord=None):
        '''
        param: 
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple(int, int) (obssice(1-8), ordonnée(1-8)) ou None si la pièce n'est pas sur le plateau
        '''
        self.couleur=couleur
        self.coord=coord
        self.liste_coups=[]
        self.premier_coup=True #Important de le savoir pour les pion le roi et les tours
    

    def bouger_piece(self, x, y):
        '''
        Sers à bouger la pièce, lui change ses coordonnées avec les nouvelles qui correspondent à celles après s'être déplacé.
        Input:
            x: int nouvelle abcisse
            y: int nouvelle ordonnée
        '''
        self.coord=(x,y)
        if self.premier_coup:
            self.premier_coup=False


class Roi(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Roi", couleur)
        
        if self.couleur==True:
            self.symbole="♔"
        else:
            self.symbole="♚"

    def __str__(self):
        return self.symbole


    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        self.liste_coups=[]

        


class Reine(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♕"
        else:
            self.symbole="♛"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        self.liste_coups=[]

        #Déplacement de la tour
        #deplacement x croissant
        x,y = self.coord
        x+=1
        while x<=8 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                self.liste_coups.append((x,y))
                x+=1 #On continue 

        
        #deplacement x decroissant
        x,y = self.coord
        x-=1
        while x>=1 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                self.liste_coups.append((x,y))
                x-=1 #On continue

        
        #Déplacement y croissant
        x,y = self.coord
        y+=1
        while y<=8 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                self.liste_coups.append((x,y))
                y+=1 #On continue 

        
        #deplacement y decroissant
        x,y = self.coord
        y-=1
        while y>=1 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                self.liste_coups.append((x,y))
                y-=1 #On continue


class Fou(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♗"
        else:
            self.symbole="♝"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        self.liste_coups=[]


class Cavalier(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♘"
        else:
            self.symbole="♞"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        self.liste_coups=[]

class Tour(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♖"
        else:
            self.symbole="♜"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        self.liste_coups=[]
        
        #deplacement x croissant
        x,y = self.coord
        x+=1
        while x<=8 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                self.liste_coups.append((x,y))
                x+=1 #On continue 

        
        #deplacement x decroissant
        x,y = self.coord
        x-=1
        while x>=1 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                self.liste_coups.append((x,y))
                x-=1 #On continue

        
        #Déplacement y croissant
        x,y = self.coord
        y+=1
        while y<=8 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                self.liste_coups.append((x,y))
                y+=1 #On continue 

        
        #deplacement y decroissant
        x,y = self.coord
        y-=1
        while y>=1 and not case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if case_occupe(x,y, couleur): #Si une pièce adverse setrouve sur la cette case
                self.liste_coups.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                self.liste_coups.append((x,y))
                y-=1 #On continue



class Pion(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♙"
        else:
            self.symbole="♟"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        self.liste_coups=[]
        x,y=self.coord

        #Cas 1: Avancer d'une case
        if self.couleur: #Si blanc
            if y+1<=8: #Si la collone du dessus est encore sur le plateau
                if not case_occupe(x,y+1, self.couleur) and not case_occupe(x,y+1, not self.couleur): #Si la case au dessus n'est pas occupe
                    self.liste_coups.append((x, y+1))  #On peut aller dans cette case

                elif x+1<=8: #Si la collone de droite est encore sur le plateau
                    if case_occupe(x+1,y+1, self.couleur): #Si la case en diagonale droite est occupé par un pièce adverse
                        self.liste_coups.append((x+1, y+1))

                elif x-1<=8: #Si la collone de gauche est encore sur le plateau
                    if case_occupe(x-1,y+1): #Si la case en diagonale gauche est occupé par une pièce adverse 
                        self.liste_coups.append((x-1, y+1))

        else: #Couleur noir
            if y-1<=8: #Si la collone du dessous est encore sur le plateau
                if not case_occupe(x,y-1, self.couleur) and not case_occupe(x,y-1, not self.couleur): #Si la case en dessous n'est pas occupé
                    self.liste_coups.append((x, y-1))  #On peut aller dans cette case

                elif x+1<=8: #Si la collone de droite est encore sur le plateau
                    if case_occupe(x+1,y-1, self.couleur): #Si la case en diagonale droite est occupé par un pièce adverse
                        self.liste_coups.append((x+1, y-1)) #On peut aller sur cette case

                elif x-1<=8: #Si la collone de gauche est encore sur le plateau
                    if case_occupe(x-1,y-1, self.couleur): #Si la case en diagonale gauche est occupé par une pièce adverse 
                        self.liste_coups.append((x-1, y-1)) #On peut aller sur cette case


        #Cas 2: Avancer de 2 cases
        if premier_coup:
            if self.couleur: #Si blanc
                if not case_occupe(x,y+1, self.couleur) and not case_occupe(x,y+1, not self.couleur) and not case_occupe(x,y+2, self.couleur) and not case_occupe(x,y+2, not self.couleur):
                    self.coups_possibles.append((x, y-2))

                else: #Si noir
                    if not case_occupe(x,y-1, self.couleur) and not case_occupe(x,y-1, not self.couleur) and not case_occupe(x,y-2, self.couleur) and not case_occupe(x,y-2, not self.couleur):
                        self.coups_possibles.append((x, y-2))