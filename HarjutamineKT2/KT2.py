"""Koosta programm telefoniraamatu loomiseks.



1.       Peab saama sisestada nime ja telefoni numbrit
2.       Samal nimel võib olla ainult üks telefoni number
3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime
    a.       Kui vastet pole, siis peab võimaldama lisamist
4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)
5.       Lisa funktsioon terve raamatu kuvamiseks"""



def add_contact():
    nimed = []
    nimi = input("Sisesta nimi: ")

    if nimi in nimed:
        print("Sellel nimel on juba number olemas.")
        return

    number = input("Sisesta telefoninumber: ")
    print("Kontakt lisatud.")




if __name__ == "__main__":
    add_contact()