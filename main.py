import pygame
from pygame.locals import *

# Initialisation de PyGame
pygame.init()

# Définition de la taille de la fenêtre
largeur, hauteur = 400, 300
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Détection des touches")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Boucle principale
def main():
    continuer = True
    horloge = pygame.time.Clock()
    
    while continuer:
        for evenement in pygame.event.get():
            if evenement.type == QUIT:
                continuer = False
            elif evenement.type == KEYDOWN:
                # Récupération de la touche pressée
                touche = pygame.key.name(evenement.key)
                
                # Effacement de l'écran
                fenetre.fill(BLANC)
                
                # Affichage de la touche pressée
                texte = pygame.font.SysFont(None, 30).render("Touche pressée : " + touche, True, NOIR)
                fenetre.blit(texte, (50, 50))
                
        # Mise à jour de l'affichage
        pygame.display.flip()
        
        # Limite de 60 FPS
        horloge.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()