"""1.	Küsi kasutaja sugu ja vanus
2.	Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
3.	Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda.
4.	Salvesta järjendisse iga kolmas tervitus ja viimane
5.	Kuva ekraanile järjendis olevate tervituste eelviimased sõnad"""

def gender_and_age():
    gender = str(input("""Kirjutage kas te olete "mees" või "naine": """))
    age = int(input("Kui vana te olete?"))
    if gender == "mees":
        print("Tere Hr.")
    elif gender == "naine":
        print("Tere Pr.")



if __name__ == "__main__":
    gender_and_age()
