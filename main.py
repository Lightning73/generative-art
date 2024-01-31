from PIL import Image, ImageDraw
from Ligne import Ligne as _Ligne


print(f"1. Générer l'image avec les angles générés aléatoirement \n"
      f"2. Générer l'image avec un Perlin Noise\n"
      f"3. Générer l'image à partir d'une image donnée par l'utilisateur")

action = input("Numéro de l'action: ")


def auto_open(mode, userImage=None):
    imgPIL = None

    if mode == 'U':  # U == User == action 3, créer une image de la même taille que celle fournie
        imgPIL = Image.new('RGB', userImage.size)
    elif mode == 'A':  # A == Auto == action 1 et 2, demande la taille de l'image voulue
        x_size = int(input("Longueur de l'image: "))
        y_size = int(input("Hauteur de l'image: "))
        imgPIL = Image.new('RGB', (x_size, y_size))

    return imgPIL, ImageDraw.Draw(imgPIL)


def save_and_show(img):
    img.save("Image_generee.png")
    img.show()


if action == '1':
    imagePIL, ctx = auto_open('A')
    _Ligne(imagePIL).tracer_ligne_random(ctx)
    save_and_show(imagePIL)

elif action == '2':
    imagePIL, ctx = auto_open('A')
    _Ligne(imagePIL).tracer_ligne_perlin(ctx)
    save_and_show(imagePIL)

elif action == '3':
    uImage = Image.open(input("Chemin vers l'image: "))
    imagePIL, ctx = auto_open('U', uImage)
    _Ligne(imagePIL, uImage).tracer_ligne_image(ctx)
    save_and_show(imagePIL)
