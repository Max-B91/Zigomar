import random

mains = ["potions scintillantes", "clés mystérieuses", "boules brillantes", "squelettes miniatures"]
sac = []

# Mettre les objets des mains dans le sac
sac.extend(mains)
mains.clear()

while True:
    # Ramasser des objets
    while True:
        objet = input("Entrer ce que vous avez ramassé : ")

        if objet == "":
            break

        mains.append(objet)
        sac.extend(mains)
        mains.clear()

    # Choisir une méthode de triage
    choix = random.randint(1, 2)

    if choix == 1:
        # Triage automatique avec la lettre "b" et les chiffres
        if len(sac) >= 15:
            for i in range(len(sac) - 1, -1, -1):
                indice1 = sac[i].find("b")

                if indice1 != -1:
                    sac.remove(sac[i])

                elif sac[i].replace(" ", "").isalpha() == False:
                    sac.remove(sac[i])

    else:
        # Triage avec l'utilisateur
        print("Voici les objets dans votre sac :")
        print(sac)

        objet_choisi = input("Entrer l'objet que vous voulez enlever : ")
        sac.remove(objet_choisi)

    print(sac)
    print()

    # Mini-quiz de Zigomar
    print("Zigomar veut jouer à son mini-quiz farfelu !\n")
    print("Voici les objets dans votre sac :")
    print(sac)

    # Mélanger les objets
    random.shuffle(sac)

    # Choisir un objet au hasard
    objet_aleatoire = random.choice(sac)

    print("Devine quel objet j'ai choisi !")
    reponse = input("Entrer votre réponse : ")

    # Vérifier la réponse
    if reponse == objet_aleatoire:
        print("Zigomar saute de joie et te remercie !")
    else:
        print("Zigomar te lance un regard noir et grogne...")

    # Trier le sac par ordre alphabétique
    sac.sort()

    print()
    print("Voici votre sac trié par ordre alphabétique :")
    print(sac)

    break
