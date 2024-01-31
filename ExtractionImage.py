class ExtractionImage:
    """
    Récupère la couleur de chaque pixel d'une image donnée

    Entrée:
        image fournie par l'utilisateur
        
    Sortie:
        Liste des couleurs des pixels
    
    """
    def __init__(self, image):
        self.img = image

    def extract(self):
        lst = []

        for x in range(self.img.size[0]):

            for y in range(self.img.size[1]):
                lst.append(self.img.getpixel((x, y)))

        return lst
    
    
