import random


# FONCTIONS
def dictionnaire():
    keep_going = 'y'
    while keep_going.lower() == 'y':
        print("Saisissez le mot que vous souhaitez ajouter au dictionnaire (au moins deux lettres : ")
        word_to_add = input("Mot : ")
        if len(word_to_add) >= 2:
            words_list.append(word_to_add)
            print("Le mot", word_to_add, "a bien été ajouté ! \n")
        keep_going = input("Voulez-vous ajouter un autre mot ? Oui (Y) ou Non (N) : ")
    welcome()


def play():
    # Vérification de la présence de mots dans le dictionnaire
    if len(words_list) == 0:
        print("Pas de mots dans le dictionnaire ... Merci d'en ajouter !\n")
        welcome()

    # Choix du nom du joueur
    player_name = input("Quel est votre nom ? ")
    name_in_table = False
    step = 0

    for i in range(0, len(players_scores), 1):
        if player_name == players_scores[i][0]:
            name_in_table = True
            step += i

    if name_in_table is True:
        print("Bon retour parmi nous,", player_name, "!")
    else:
        print("Bienvenue parmi nous", player_name)
        players_scores.append([player_name, 0])


    # Initialisation du mot
    index = random.randint(0, len(words_list) - 1)
    word_fetch = words_list[index]
    word_in_list = []
    word_to_find = []
    words_written = []
    score = 0
    error = 0

    # Création des tableaux (mot à trouver et mot trouvés de l'utilisateur
    for i in range(0, len(word_fetch), 1):
        word_in_list.append(word_fetch[i])
        word_to_find.append("_")

    # Vérification de la lettre selon le nombre d'erreurs et les lettres trouvées
    while not (score == len(word_in_list)) and not (error == 7):
        letter_to_find = input("Saisissez une lettre : ")
        letter_to_find = letter_to_find.lower()
        word_displayed = ''
        letter_fetched = False

        # Ajout au tableau des lettres proposées
        words_written.append(letter_to_find)

        #Vérification de la lettre dans le mot à trouver
        for i in range(0, len(word_in_list), 1):
            if letter_to_find == word_in_list[i]:
                word_to_find[i] = letter_to_find
                score += 1
                letter_fetched = True
                print("+1 Point\n")
            elif i == (len(word_in_list) - 1) and letter_fetched is False:
                error += 1

        # Message en cas de défaite, victoire ou d'étape intermédiaire
        if score == len(word_fetch):
            print("Bravo ! Vous avez gagné !!!\n")
        elif error == 7:
            print("Looser ! Bah écoute, tu as perdu ...\n")
        else:
            for i in range(0, len(word_in_list), 1):
                word_displayed += word_to_find[i]
            print(error, "/", "7 erreurs | À la 7ème erreur : fin de partie !")
            print(word_displayed)
            print("Vos propositions : ", words_written, "\n")

    # Affectation des scores
    for i in range(0, len(players_scores), 1):
        if player_name == players_scores[i][0]:
            players_scores[i][1] += score - error

    # Fin de partie
    welcome()


def scores(tableau):
    # Tri du tableau
    sort_score()
    classement = 1

    # Boucle de classement des joueurs selon leurs score
    for i in range(len(tableau) - 1, -1, -1):
        print(classement, ". ", tableau[i][0], "avec", tableau[i][1], "point(s)")
        classement += 1
    welcome()


def welcome():
    print('Bienvenue dans le Pendu ! Vous souhaitez : ')
    choice_mode = str(input("- Ajouter un mot dans le dictionnaire (A)\n- Jouer (P)\n- Voir le tableau des scores (T) ?\n Votre choix : "))

    # Navigation vers les menus
    if choice_mode.lower() == 'a':
        dictionnaire()
    elif choice_mode.lower() == 'p':
        play()
    elif choice_mode.lower() == 't':
        scores(players_scores)
    else:
        print('Saisie incorrecte. Au revoir ;)')


def sort_score():
    swap = True
    while swap is True:
        swap = False
        # Tri à bulle pour classer les joueurs
        for i in range(0, len(players_scores) - 1, 1):
            if players_scores[i][1] > players_scores[i + 1][1]:
                temp = players_scores[i]
                players_scores[i] = players_scores[i + 1]
                players_scores[i + 1] = temp
                swap = True


# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    # Variables
    words_list = []
    players_scores = []
    welcome()
