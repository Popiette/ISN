﻿# Créé par Pierre, le 17/03/2016 en Python 3.2
import pygame
pygame.init()
import pickle
"""Constantes projectiles"""
projectilesList = [ pygame.image.load("resources/photos/photon_bleu_clair_pour_le_joueur2.png"),
                    pygame.image.load("resources/photos/photon_bleu.png"),
                    pygame.image.load("resources/photos/photon_jaune.png"),
                    pygame.image.load("resources/photos/photon_rose2.png"),
                    pygame.image.load("resources/photos/photon_sombre.png"),
                    pygame.image.load("resources/photos/photon_vert.png"),
                    pygame.image.load("resources/photos/photon_violet.png")]

laser = pygame.image.load("resources/photos/laserjaune.png")
laser2 = pygame.image.load("resources/photos/laserjaune.png")

"""Les sprites des explosions"""
explodeList = [pygame.image.load("resources/photos/explosion_v1.1.bmp"),
               pygame.image.load("resources/photos/explosion_v2.2.bmp"),
               pygame.image.load("resources/photos/explosion_v3.bmp")]



touches = [122, 276, 275, 273, 274, 304]      #touches = [tir,gauche,droite,haut,bas,controle]
#Quand vous voulez récupérer l'image d'un photon : projectilesList[index]

#lycee
largeur,hauteur= 768, 600
#pas lycee
#largeur,hauteur=1280,720


recordOn=True
niveauActuel=1
niveauMaxAtteint=1
niveauMaxFait = 5

def sauvegarder() :
        """if niveauMaxAtteint > niveauMaxFait :
            niveauMaxAtteint = niveauMaxFait"""
        with open("options.pickle", 'wb') as file:
            pickle.dump([niveauActuel,niveauMaxAtteint,hauteur,largeur,touches],file)


indiceLangue = 1
langueDispo = ['FR','JP','DE','PL']
langue = langueDispo[indiceLangue]