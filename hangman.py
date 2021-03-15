import random

def hangman(word):
    wrong = 0
    stages = ["",
             "_______       ",
             "|      |      ",
             "|      |      ",
             "|      O      ",
             "|     /|\     ",
             "|     / \      ",
             "|_____________"]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to hangman game!\nThis is the word to guess:")
    print((" ".join(board)))

    while wrong < len(stages)-1:
        print("\n")
        char = input("Guess a letter: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "__" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("You lose! It was {}".format(word))

list_words = ["ciao", "suca", "troia", "culo", "cazzo", "dioporco"]

hangman("dioporco")
#hangman(random.choice(list_words))
