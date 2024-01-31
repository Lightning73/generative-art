from perlin_noise import PerlinNoise as _PerlinNoise


class GenererPerlin:
    """
    Génère une liste de nombres aléatoires à l'aide d'un Perlin noise

    Sortie :
        lst: liste de nombres générés avec le permin noise
    """
    def __init__(self, imgpil_x_size, imgpil_y_size):
        self.lst = []

        self.imgpil_x_size, self.imgpil_y_size = imgpil_x_size, imgpil_y_size

    def perl(self):
        for y in range(0, self.imgpil_x_size):

            for x in range(0, self.imgpil_y_size):

                self.lst.append(_PerlinNoise().noise([((x/800) + 1)/2, ((y/800) + 1)/2]))

        return self.lst
