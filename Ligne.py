from Angles import Angles as _Angles
import math as _maths
from random import sample as _sample


class Ligne:
    def __init__(self, imgpil, userImage=None):
        self.imgpil = imgpil
        self.user_Image = userImage

        self.dist_pts = 10

        self.imgpil_x_size = self.imgpil.size[0]
        self.imgpil_y_size = self.imgpil.size[1]

        self.y_pixels = _sample([i for i in range(self.imgpil_y_size)], self.imgpil_y_size // 3)

        self.list_angles = None

    def tracer_ligne_random(self, context):
        self.list_angles = _Angles(self.imgpil_x_size, self.imgpil_y_size).angle_random((-95, 95))
        self.__tracer_ligne(context, 'i')

    def tracer_ligne_perlin(self, context):
        self.list_angles = _Angles(self.imgpil_x_size, self.imgpil_y_size).nuance_en_angle((-180, 180))
        self.__tracer_ligne(context, 'i')

    def tracer_ligne_image(self, context):
        self.list_angles = _Angles(self.imgpil_x_size, self.imgpil_y_size).pixel_en_angle(self.user_Image,
                                                                                          (-95, 95))
        self.__tracer_ligne(context, 'c')

    def __tracer_ligne(self, context, mode):
        couleurs = (255, 255, 255)

        for y in self.y_pixels:
            i = 0
            lst_coords = self.__angles_en_coords(y)

            if mode == 'i':  # i = intensité
                couleurs = self.__change_intensite(y)

            while i < len(lst_coords) - 1:

                if mode == 'c':  # c = couleurs
                    couleurs = self.__change_couleur(lst_coords[i])

                context.line((lst_coords[i], lst_coords[i + 1]),
                             (couleurs[0], couleurs[1], couleurs[2]))

                i += 1

    def __angles_en_coords(self, y):
        list_coords = []
        x = 0

        for i in range(self.imgpil_x_size):
            x = int(x + self.dist_pts * _maths.cos(self.list_angles[i]))
            y = int(y + self.dist_pts * _maths.sin(self.list_angles[i]))
            list_coords.append((x, y))

        self.list_angles = self.list_angles[self.imgpil_x_size:]

        return list_coords

    def __change_intensite(self, y):
        intens = (y / self.imgpil_y_size) * 255
        intens = int(intens)

        return intens, intens, intens

    def __change_couleur(self, coords):

        if 0 < coords[0] < self.imgpil_x_size and 0 < coords[1] < self.imgpil_y_size:
            return self.user_Image.getpixel(coords)

        else:
            return 0, 0, 0
