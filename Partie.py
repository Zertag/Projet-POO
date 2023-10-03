from joueurs import*
from piece import*
import numpy as np

class Partie:
    
    """Partie de jeu d'échecs
    """
<<<<<<< HEAD
    def __init__(self,j1 :Joueur, j2:Joueur, plateau: str = "Plateau_base"):
=======
    def __init__(self,j1 :Joueur, j2:Joueur, plateau = "Plateau_base"):
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        """Construit une partie d'échecs.
        Commence par créer un plateau si il n'est pas fourni,
        puis attribue les pièces de ce plateau aux joueurs
        de la partie, selon leur couleurs. Attribue aussi leur position aux pièces.

        Args:
            plateau (_type_, optional): Plateau de jeu. None si non fourni (nouvelle partie)
            j1 (Joueur) : Premier joueur de la partie, instance de la classe Joueur
            j2 (Joueur) : Second joueur de la partie, instance de la classe Joueur
        """
        print("Chargement de la partie")
        #création des joueurs
        self.j1=j1
        self.j2=j2
<<<<<<< HEAD
=======
       
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        #lecture du fichier de sauvegarde
        fichier = open(plateau+".txt", 'r')
        sauv_txt = fichier.read()
        fichier.close()
        #maintenant il faut extraire le texte important : 
<<<<<<< HEAD
        pionsj1,pionsj2 = sauv_txt.split("\n")
        pionsj1 = pionsj1[10:]
        pionsj2 = pionsj2[10:]
=======
        pieces_j1,pieces_j2 = sauv_txt.split("\n")
        pieces_j1 = pieces_j1[10:]
        pieces_j2 = pieces_j2[10:]
        
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        
        
        #dictionnaire de {coordonnées : objet piece}
        self.plateau = {}
<<<<<<< HEAD
        for pionsj in (pionsj1,pionsj2):
            for p in pionsj.split(";"):
=======
        for pieces_j in (pieces_j1,pieces_j2):
            for p in pieces_j.split(";"):
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
                p = p[1:-1]
                p = p.split(",")
                type_piece = p[0]
                couleur_piece = True if p[1] == "True" else False
                coord_piece = (int(p[2]),int(p[3]))
                
                #pion tour cavalier fou roi reine 
                if type_piece == "Pion":
                    piece = Pion(couleur_piece,coord_piece)
                if type_piece == "Tour":
                    piece = Tour(couleur_piece,coord_piece)
                if type_piece == "Cavalier":
                    piece = Cavalier(couleur_piece,coord_piece)
                if type_piece == "Fou":
                    piece = Fou(couleur_piece,coord_piece)
                if type_piece == "Reine":
                    piece = Reine(couleur_piece,coord_piece)
                if type_piece == "Roi":
                    piece = Roi(couleur_piece,coord_piece)
                #on ajoute la piece au plateau
                self.plateau[coord_piece] = piece
                
                #on ajoute la piece au bon joueur
<<<<<<< HEAD
                if pionsj == pionsj1:
                    self.j1.pieces.append(piece)
                elif pionsj == pionsj2:
                    self.j2.pieces.append(piece)
                 
                
                
                
    def __str__(self)->str:
        """Méthode print pour la partie. Affiche le plateau dans
        son état actuel.
=======
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147

                if pieces_j == pieces_j1:
                    self.j1.pieces.append(piece)
                elif pieces_j == pieces_j2:

                    self.j2.pieces.append(piece)
            
                
                
    def afficher(self, tour: bool)->str:
        """Méthode pour afficherla partie. Affiche le plateau dans
        son état actuel.Nous n'utilisons pas la métohde spéciale __str__, car En fonction du tour, l'affichage
        du plateau est renversé.
        
        Args:
            tour (bool) :  True <=> Tour aux blancs 
        Returns:
            str: Le plateau.
        """
        
        if tour:
            ordre_affichage_lignes=range(7,-1,-1)
        else:
            ordre_affichage_lignes=range(8)
        
        p=""
        i=0
        num_ligne=[str(x) for x in range(1,9)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
<<<<<<< HEAD
        p+="    " +  "    ".join(nom_col) +"\n"
        for i in range(8):
           
            p+=num_ligne[7-i] + "   "
        
            
            for j in range(8):
=======
        
        if tour: p+=" "*5 +  "    ".join(nom_col) +"\n"
        else: p+=" "*5 +  "    ".join(nom_col[-1::-1]) + "\n"
      
        
        for i in ordre_affichage_lignes:
           
           p+=num_ligne[i] + "   "
               
           for j in range(8):
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
                try:
                    p+=self.plateau[(j,i)].__str__() + "  | "
                except KeyError:
                    p+= " " + "  | "
                
<<<<<<< HEAD
            i+=1
            p+=  "\n" + "   "+ "-"*41 + "\n"
        p+=" "*5 +  "    ".join(nom_col) 
        return p
=======
           i+=1
           p+=  "\n" + "   "+ "-"*41 + "\n"
           
        if tour: p+=" "*5 +  "    ".join(nom_col) 
        else: p+=" "*5 +  "    ".join(nom_col[-1::-1]) 
        
        print(p)
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
    
    
    def sauvegarder(self,nom_fichier : str = None) -> None:
        #ouvrir un fichier de sauvegarde en ecriture
        #écrire la sauvegarde sous format [(type de piece, couleur, coordonnées)]
        #fermer le fichier
        sauvegarde = "Joueur1 : "
        for i in self.j1.pieces:
            sauvegarde+=f"[{i.nom},{i.couleur},{i.coord[0]},{i.coord[1]}];"    
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au dernier
        
        #sauvegarder le deuxieme joueur
        
        sauvegarde+="\nJoueur2 : "
        for i in self.j1.pieces:
            sauvegarde+=f"[{i.nom},{i.couleur},{i.coord[0]},{i.coord[1]}];"
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au  dernier 
        
        #demander le fichier a sauvegarder s'il n'est pas spécifier par le programme (sauvegarde de base du jeu)
        if sauvegarde is None:
            nom_fichier = input("nom du fichier de sauvegarde : ")
            
        #écriture dans le fichier spécifier (écrase le texte déja existant ou crée un nouveau fichier)
        fichier = open(nom_fichier+".txt", 'w')
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
        if isinstance(self.plateau[coord1] ,Pion) or isinstance(self.plateau[coord1], Roi) or isinstance(self.plateau[coord1], Tour) :
            self.plateau[coord1].premier_coup=False
        
<<<<<<< HEAD
    
=======
        self.plateau[coord1].coord=coord2
        
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        self.plateau[coord2] = self.plateau.pop(coord1)
                
    def echec(self,couleur: bool) -> bool:
        """Fonction qui nous dis si le roi de la couleur demandé est en échec

        Args:
            couleur (bool): Couleur de du roi dont on veut savoir si il est en échec (True<=> Blanc et False <=> Noir)

        Returns:
            bool: True <=> Roi en échec
        """
        liste_case_controllee=[]
        if couleur: #On regarde l'échec du roi Blanc
            print(self.j2.pieces)
            for piece in self.j2.pieces: #Pour les pièces noire en jeu

                liste_case_controllee+=piece.cases_controllees(self) #On ajoute les case controllé par chaque pieces adverse à l'ensemble des cases controllé par l'adversaire

            for case in liste_case_controllee: # Pour chaque case controllé par l'adversaire
                try:
                    piece=self.plateau[case]
                    if piece.nom=="Roi" and couleur: #On vérifie si cette pièce 
                        return True
                except: #Il n'y a pas de case à ces coordonnées
                    pass                
        
        else:
            for piece in self.j1.pieces:
                liste_case_controllee+=piece.cases_controllees

            for case in liste_case_controllee:
                piece=self.plateau[case]
                if piece.nom=="Roi" and not piece.couleur:
                    return True
                
        return False
<<<<<<< HEAD


    def case_occupe(self, coord , couleur: bool):
        '''
        Nous renvoie si la case de coordonnées coord est déjà occupé par une des pieces de la même couleur
        Input:
            coord (tuple[int,int]): coordonnées de la case
            couleur: couleur de la piece concerné, on doit donc voir si la case est occupé par cette couleur

        Output: Bool
            La case est occupé par une piece de même couleur -> True
            La case n'est pas occupé par une piece de même couleur -> False
        '''
        piece=self.plateau.get(coord,None)
        if piece is not None:
            if piece.couleur==couleur:
                return True
            else:
                return False
        return False
=======
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        


   
    def echec_et_mat(self,couleur):
        pass
    
    def gagnant(self):
        
        if self.echec_et_mat(True): return self.j1
        
        elif self.echec_et_mat(False): return self.j2
        
        return None  