"""Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga. On määratud erinevad hindenormid meestele ja naistele.
Koostada funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:
•	Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
•	Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
•	Sõne „rahuldav“ muudel juhtudel
•	Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu
Koostada programm, mis küsib kasutajalt:
•	failinime,
Programm peab:
•	lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
•	funktsiooniga arvutama hinded ja väljastama need ekraanile
•	arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni ümardatud keskmised ning funktsiooni abil keskmised hinded.
"""

def file_main():
    men = []
    women = []
    file = input("Sisestage fail nimi, mida kontrollida: ")
    if file == "cooper.txt":
        with open("cooper.txt", "r") as f:
            for line in f:
                number, gender = line.strip().split()
                if gender == "M":
                    men.append(int(number))
                else:
                    women.append(int(number))
        results(men, women)
        average(men, women)
    else:
        print("Wrong file name")


def average(men, women):
    print("Keskmised tulemused:")
    print(f"Mehed: {grade(round(sum(men) / len(men)), 2800, 2000)}")
    print(f"Naised: {grade(round(sum(women) / len(women)), 2600, 1800)}")


def grade(score, good_limit, weak_limit):
    if score >= good_limit:
        return f"{score}, väga hea"
    elif score < weak_limit:
        return f"{score}, nõrk, järgmisest hindest jäi puudu {weak_limit - score} meetrit"
    else:
        return f"{score}, rahuldav, järgmisest hindest jäi puudu {good_limit - score} meetrit"


def results(men, women):
    print("Mehed:")
    for score in men:
        print(grade(score, 2800, 2000))

    print("Naised:")
    for score in women:
        print(grade(score, 2600, 1800))


if __name__ == "__main__":
    file_main()