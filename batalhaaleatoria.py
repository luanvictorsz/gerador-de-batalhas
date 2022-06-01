import random

lista = ["Lobisomem", "Ogro", "Slime", "Harpia", "Vampiro", "Goblin"]

lobisomem = 10
ogro = 15
slime = 5
harpia = 7
vampiro = 10
goblin = 7


criatura = random.choice(lista)
dano = random.randint(1, 20)

print(f"Batalha contra {criatura}:")

if "Lobisomem" in criatura:
    print(f"o  Lobisomem possui {lobisomem} de vida.")
    if lobisomem <= dano:
        print(f"você deferiu {dano} de dano na criatura, então vc o derrotou")
    else:
        print(f"você deferiu {dano} de dano na criatura, então você não o derrotou")
        
if "Ogro" in criatura:
    print(f"o  Ogro possui {ogro} de vida.")
    if ogro <= dano:
        print(f"você deferiu {dano} de dano na criatura, então vc o derrotou")
    else:
        print(f"você deferiu {dano} de dano na criatura, então você não o derrotou")
        
if "Slime" in criatura:
    print(f"o  Slime possui {slime} de vida.")
    if slime <= dano:
        print(f"você deferiu {dano} de dano na criatura, então vc o derrotou")
    else:
        print(f"você deferiu {dano} de dano na criatura, então você não o derrotou")
        
if "Harpia" in criatura:
    print(f"a Harpia possui {harpia} de vida.")
    if harpia <= dano:
        print(f"você deferiu {dano} de dano na criatura, então vc o derrotou")
    else:
        print(f"você deferiu {dano} de dano na criatura, então você não o derrotou")

if "Vampiro" in criatura:
    print(f"o  Vampiro possui {vampiro} de vida.")
    if vampiro <= dano:
        print(f"você deferiu {dano} de dano na criatura, então vc o derrotou")
    else:
        print(f"você deferiu {dano} de dano na criatura, então você não o derrotou")
        
if "Goblin" in criatura:
    print(f"o  Goblin possui {goblin} de vida.")
    if goblin <= dano:
        print(f"você deferiu {dano} de dano na criatura, então vc o derrotou")
    else:
        print(f"você deferiu {dano} de dano na criatura, então você não o derrotou")
