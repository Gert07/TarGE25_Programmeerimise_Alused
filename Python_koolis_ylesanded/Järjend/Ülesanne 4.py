"""Moodusta järjend järgnevate sõnedega:

Jah, kindlasti!
Jah!
Võib-olla!
Ei!
Tee programm, kus kasutaja saab küsida jah/ei küsimuse ja programm annab vastuse ühe suvalise elemendi eelnevast järjendist.

Juhuslike arvude genereerimist vaatame tulevikus, kuid praegu lisame programmi algusesse rea, tänu millele Python suudab juhuslikke arve genereerida:

import random
Seejärel võime suvalises kohas programmis kasutada juhusliku arvu saamiseks funktsiooni random.randint(x, y), mis genereerib juhusliku täisarvu x-st y-ni (mõlemad kaasaarvatud), näiteks:

juhuarv = random.randint(1, 10)
Lisa ka sisse- ja väljajuhatavad tekstid, et dialoog kasutajaga oleks võimalikult loomulik.

Kui valmis, siis lisa järjendisse 20 erinevat vastusevarianti, mille ingliskeelsed vasted leiad leheküljelt https://en.wikipedia.org/wiki/Magic_8-Ball"""
import random
from multiprocessing.connection import answer_challenge
from random import randint



def ask_if_questions():
    vastused = ["Jah, kindlasti!","Jah!","Võib-olla!","Ei!"]
    print("Programmist väljumiseks kirjuta (Stop)")
    random_number = randint(0, len(vastused) -1)
    while True:
        question = input("Kirjutage siia kas küsimusi: ")
        print(vastused(random_number))
        if question == "Stop":
            break


if __name__ == "__main__":
    ask_if_questions()