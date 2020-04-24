#висельница

import random

def viselnica():
    
    words=["жопа","хуй","пизда","зайка"]
    word=words[random.randint(0,3)]
               
    wrong = 0
    chuvak = ["               ","_________       ","|        |      ","|        |      ","|        0      ","|       /|\     ","|       / \     ","|____________   "]
    
    slovospisok = list(word)
    slovoekran = ["_"]*len(word)
    win = False
    print("Поехали!")

    while wrong < len(chuvak) - 1:
        print ("\n")
        guess = input("Введи букву:")
        
        if guess in slovospisok:
            right = slovospisok.index(guess)
            slovoekran[right] = guess
            slovospisok[right] = '$'
        else:
            wrong += 1

        print(" ".join(slovoekran))
        e = wrong + 1
        print("\n".join(chuvak[0:e]))

        if "_" not in slovoekran:
            print("\n")
            print("Победа! Слово: {}.".format(word))
            win = True
            break

    if win == False:
        print("\n".join(chuvak))
        print("\n")
        print("Проиграл! Слово: {}.".format(word))

viselnica()

a=input()
    
