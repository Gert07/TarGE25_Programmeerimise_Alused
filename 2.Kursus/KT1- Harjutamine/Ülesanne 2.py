"""1.	Küsi kasutaja nime ja vanust
2.	Kui vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
3.	Muidu küsi koosta nime pikkuse jagu arvutus tehteid juhuarvudega (Järjend)
4.	Kuva tehteid ja lase kasutajal vastata, teata kas said õige tulemuse.
5.	Programmi lõpus õnnitle kasutajat erineva tekstiga olenevalt programmi käigust"""

def name_and_age ():
    name = str(input("Sisestage oma nimi: "))
    age = int(input("Sisestage oma vanus: "))
    if age < 5:
        for i in range (3):
            print(f"Tere {name}")
    else:
        name = name.split()


if __name__ == "__main__":
    print(name_and_age())
