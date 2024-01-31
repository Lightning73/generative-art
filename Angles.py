from random import randrange as _randrange
from math import pi as _pi
from GenererPerlin import GenererPerlin as _GenererPerlin
from ExtractionImage import ExtractionImage as _ExtractionImage


class Angles:
    
    def __init__(self, imgpil_x_size, imgpil_y_size):
        self.imgpil_x_size, self.imgpil_y_size = imgpil_x_size, imgpil_y_size

    def pixel_en_angle(self, image, bornes):
        """
        Transforme la couleur d'un pixel en angle

        Entrées: 
            image: image fournie par l'utilisateur
            bornes: tuple des angles maximum (-95, 95)

        Sortie:
            lst: liste des angles
               
        """
        lst_rgb = _ExtractionImage(image).extract()
        lst = []

        for rgb_color in lst_rgb:
            somme_rgb = 0

            for element in rgb_color:
                somme_rgb += element

            lst.append((((somme_rgb / 765) * _randrange(bornes[0], bornes[1])) * _pi) / 180)

        return lst

    def angle_random(self, bornes):
        """
        génère une liste d'angles random à partir de la taille de l'image
        Entrée:
            bornes: tuple des angles maximum (-25, 25)

        Sortie:
            lst: liste des angles
        
        """
        lst = []

        for y in range(self.imgpil_y_size):

            for x in range(self.imgpil_x_size):
                if not x % 2:
                    lst.append(0)

                lst.append((_randrange(bornes[0], bornes[1]) * _pi) / 180)

        return lst

    def nuance_en_angle(self, bornes):
        """
        Transforme les valeurs générées par le Perlin en angle
        Entrée:
            bornes: tuple des angles maximum (-95, 95)

        Sortie:
            lst: liste des angles     
        """

        lst_perlin = _GenererPerlin(self.imgpil_x_size, self.imgpil_y_size).perl()

        for i in range(len(lst_perlin)):

            lst_perlin[i] = (lst_perlin[i] * _randrange(bornes[0], bornes[1]) * _pi) / 180

        return lst_perlin
