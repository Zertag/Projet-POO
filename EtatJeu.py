from joueurs import*
from piece import*
import numpy as np


class EtatJeu:
    
    """Partie de jeu d'échecs
    """
    def __init__(self,plateau  = None, trait = None, sauvegarde : str = "Plateau_base"):
        """Construit une partie d'échecs.
        Commence par créer un plateau si il n'est pas fourni,
        puis attribue les pièces de ce plateau aux joueurs
        de la partie, selon leur couleurs. Attribue aussi leur position aux pièces.

        Args:
            plateau (_type_, optional): Plateau de jeu. None si non fourni (nouvelle partie)
            j1 (Joueur) : Premier joueur de la partie, instance de la classe Joueur
            j2 (Joueur) : Second joueur de la partie, instance de la classe Joueur
            trait (bool) : prochaine couleur à jouer
        """
        
        print("Chargement de la partie")
        #création des joueurs
        self.pieces=[[],[]]
        
        
        #lecture du fichier de sauvegarde
        fichier = open("sauvegardes\\"+sauvegarde+".txt", 'r')
        sauv_txt = fichier.read()
        fichier.close()
        #maintenant il faut extraire le texte important : 
        pieces_blanches,pieces_noires,trait_texte = sauv_txt.split("\n")
        pieces_blanches = pieces_blanches.split(" : ")[1]
        pieces_noires = pieces_noires.split(" : ")[1]
        trait_texte = trait_texte.split(" : ")[1]
        
        
        #dictionnaire de {coordonnées : objet piece}
        self.plateau = {}
        for pieces_j in (pieces_blanches,pieces_noires):
            for p in pieces_j.split(";"):
                p = p[1:-1]
                p = p.split(",")
                type_piece = p[0]
                couleur_piece = True if p[1] == "True" else False
                coord_piece = (int(p[2]),int(p[3]))
                
                #pion tour cavalier fou roi reine 
                if type_piece == "Pion": piece = Pion(couleur_piece,coord_piece)
                if type_piece == "Tour": piece = Tour(couleur_piece,coord_piece)
                if type_piece == "Cavalier": piece = Cavalier(couleur_piece,coord_piece)
                if type_piece == "Fou": piece = Fou(couleur_piece,coord_piece)
                if type_piece == "Reine": piece = Reine(couleur_piece,coord_piece)
                if type_piece == "Roi": piece = Roi(couleur_piece,coord_piece)
                #on ajoute la piece au plateau
                self.plateau[coord_piece] = piece
                
                #on ajoute la piece au bon joueur

                if pieces_j == pieces_blanches:
                    self.pieces[1].append(piece)
                elif pieces_j == pieces_noires:
                    self.pieces[0].append(piece)
                    
        if trait_texte == "blancs": self.trait = True
        else : self.trait = False
        self.valeur = 0
            
                
    def __str__(self)->str:
        """Méthode print pour la partie. Affiche le plateau dans
        son état actuel.Nous n'utilisons pas la métohde spéciale __str__, car En fonction du tour, l'affichage
        du plateau est renversé.
        
        Args:
            tour (bool) :  True <=> Tour aux blancs 
        Returns:
            str: Le plateau.
        """
        if self.trait:
            ordre_affichage=range(7,-1,-1)
        else:
            ordre_affichage=range(8)
        
        p=""

        num_ligne=[str(x) for x in range(1,9)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
        
        p+=" "*5 +  "    ".join(nom_col) +"\n"
        
        for i in ordre_affichage:
           
           p+=num_ligne[i] + "  | "
               
           for j in range(8):
               symbole=self.plateau.get((j,i)," ").__str__()
               p+= symbole + "  | "
                

           p+=  "\n" + "   "+ "-"*41 + "\n"
           
        p+=" "*5 +  "    ".join(nom_col)
        
        return p
        
    
    
    def sauvegarder(self,nom_fichier : str = None) -> None:
        #ouvrir un fichier de sauvegarde en ecriture
        #écrire la sauvegarde sous format [(type de piece, couleur, coordonnées)]
        #fermer le fichier
        sauvegarde = "blancs : "
        for piece in self.pieces[1]:
            sauvegarde+=f"[{piece.nom},{piece.couleur},{piece.coord[0]},{piece.coord[1]}];"    
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au dernier
        
        #sauvegarder les pieces noires
        
        sauvegarde+=f"\nnoirs : "
        for piece in self.pieces[0]:
            sauvegarde+=f"[{piece.nom},{piece.couleur},{piece.coord[0]},{piece.coord[1]}];"
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au  dernier 
        
        sauvegarde+="\nTrait : "
        if self.trait :sauvegarde+="blancs"
        else : sauvegarde+="noirs"
        
        
        #demander le fichier a sauvegarder s'il n'est pas spécifier par le programme (sauvegarde de base du jeu)
        if sauvegarde is None:
            nom_fichier = input("nom du fichier de sauvegarde : ")
            
        #écriture dans le fichier spécifier (écrase le texte déja existant ou crée un nouveau fichier)
        fichier = open("sauvegardes\\"+nom_fichier+".txt", 'w')
        fichier.write(sauvegarde)
        fichier.close()
        
        
        
        
    
    
    
    def deplacer_piece(self, coord1: tuple[int,int], coord2: tuple[int, int])->np.ndarray:
        """Déplace une pièce du plateau à un autre endroit.
        Cette méthode n'est exécutée que si le coup est valide,
        il n'y a donc pas besoin de le vérifier.

        Args:
            coord1 (tuple[int,int]): Position de la pièce à déplacer
            coord2 (tuple[int,int]): Position finale de la pièce
        Returns:
            dict: Le plateau modifié
            """
    
    
    def mouvements(self) -> dict[tuple(int,int),list[tuple(int,int)]]:
        mouv = dict()
        for coord_piece in self.plateau.keys():
            mouv[coord_piece] = coord_piece.coups_possibles()
        return mouv
    
    
    def calcul_valeur(self)->float:
        """Fonction qui calcule la valeur du plateau. La valeur est positive si les blancs ont l'avantage et négative si 
        les noirs ont l'avantage 

        Returns:
            float: valeur du jeu
        """
        valeur=0
        for pieces in [self.pieces_j1, self.pieces_j2]:
            cases_controllees=set()
            pions_blanc=[]
            pions_noir=[]
            for piece in pieces:
                
                if isinstance(Pion,piece) and piece.couleur:
                    pions_blanc.append(piece)
                elif isinstance(Pion, piece) and not piece.couleur:
                    pions_noir.append(piece)
                
                valeur+=piece.valeur
                cases_controllees.add(set(piece.coups_legaux))            
            
                for centre in [(3,3),(3,4),(4,4),(4,3)]:
                    if piece==self.plateau.get(centre,None):
                        valeur+=(0.33*piece.valeur)
                
                for sous_centre in [(2,2),(2,3),(2,4),(2,5),(3,5),(4,5),(5,5),(6,5),(6,4),(6,3),(6,2),(5,2),(3,2)]:
                    if piece==self.plateau.get(sous_centre, None):
                        valeur+=(0.10*piece.valeur)
                    
            if pieces==self.pieces_j1:
                valeur+=len(cases_controllees)
            else:
                valeur-=len(cases_controllees)
                
            for pions in [pions_blanc, pions_noir]:
                collones=[]
                for pion in pions:
                    if pion.coord[0] not in collones:
                        collones.append(pion.coord[0])
                    else:
                        if pion.couleur:
                            valeur-=0.1
                        else:
                            valeur+=0.1
        self.valeur=valeur
                
                
    
                
    def echec(self) -> bool:
        """Fonction qui nous dis si le roi de la couleur demandé est en échec

        Args:
            couleur (bool): Couleur de du roi dont on veut savoir si il est en échec (True<=> Blanc et False <=> Noir)

        Returns:
            bool: True <=> Roi en échec
        """
        #il faut trouver qui est le joueur à qui c'est le tour
        
        for piece in self.pieces[self.trait] : 
            if piece.nom == "Roi":case_roi = piece.coord#on récupere la case occupée par le roi
            else : pieces_adversaire = self.pieces[not (self.trait)]#on récupere les pieces de l'adversaire
            
        for piece in pieces_adversaire: #Pour les pièces de l'adversaire en jeu
            for case in piece.coups_possibles(self):# Pour chaque case controllé par l'adversaire
                if case == case_roi :#On vérifie si cette case est celle du roi
                    print(piece.nom,piece.couleur)
                    return True
        return False
        


   
    def echec_et_mat(self):
        #regarder si le roi est en echec, regarder s'il peut bouger, regarder s'il y a d'autre coups parmis les pieces
        if not self.echec() : return False #si le roi n'est pas en echec il n'y a pas mat
        #on regarde s'il existe des pièces qui ont le droit de bouger
        
  
        pieces_joueur = self.pieces[self.trait]
        for piece in pieces_joueur:
                if len(piece.coups_legaux(self))>0 :return False
        return True
    
    
    def gagnant(self):
        
        if self.echec_et_mat(): 
            return self.trait #attention ici on ne renvoie que la couleur du gagnant, au main de décider quel joueur c'est
     
        
        
        
        