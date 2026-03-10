import json
import os

# Lae andmed failist
def lae_andmed():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# Salvesta andmed faili
def salvesta_andmed(andmed):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for line in f:
            if name !=
            nimi.append


# Lisa uus kontakt
def lisa_kontakt(andmed):
    nimi = input("Sisesta nimi: ")

    if nimi in andmed:
        print("Sellel nimel on juba number olemas.")
        return

    number = input("Sisesta telefoninumber: ")
    andmed[nimi] = number
    salvesta_andmed(andmed)
    print("Kontakt lisatud.")


# Otsi nime järgi
def otsi_nime_jargi(andmed):
    nimi = input("Sisesta nimi: ")

    if nimi in andmed:
        print(f"{nimi} number on {andmed[nimi]}")
    else:
        print("Nime ei leitud.")
        lisa = input("Kas soovid lisada? (j/e): ")
        if lisa.lower() == "j":
            number = input("Sisesta telefoninumber: ")
            andmed[nimi] = number
            salvesta_andmed(andmed)


# Otsi numbri järgi
def otsi_numbri_jargi(andmed):
    number = input("Sisesta telefoninumber: ")

    for nimi, nr in andmed.items():
        if nr == number:
            print(f"Number kuulub: {nimi}")
            return

    print("Numbrit ei leitud.")
    lisa = input("Kas soovid lisada? (j/e): ")
    if lisa.lower() == "j":
        nimi = input("Sisesta nimi: ")
        if nimi in andmed:
            print("Sellel nimel on juba number.")
        else:
            andmed[nimi] = number
            salvesta_andmed(andmed)


# Kuva kogu telefoniraamat
def kuva_raamat(andmed):
    if not andmed:
        print("Telefoniraamat on tühi.")
    else:
        print("\nTelefoniraamat:")
        for nimi, number in andmed.items():
            print(f"{nimi}: {number}")


# Peamenüü
def menuu():
    andmed = lae_andmed()

    while True:
        print("\n--- Telefoniraamat ---")
        print("1. Lisa kontakt")
        print("2. Otsi nime järgi")
        print("3. Otsi numbri järgi")
        print("4. Kuva kogu telefoniraamat")
        print("5. Välju")

        valik = input("Vali tegevus: ")

        if valik == "1":
            lisa_kontakt(andmed)
        elif valik == "2":
            otsi_nime_jargi(andmed)
        elif valik == "3":
            otsi_numbri_jargi(andmed)
        elif valik == "4":
            kuva_raamat(andmed)
        elif valik == "5":
            print("Programm lõpetab töö.")
            break
        else:
            print("Vale valik!")

if __name__ == "__main__":
    FILE_NAME = "telefoniraamat.txt"
    menuu()