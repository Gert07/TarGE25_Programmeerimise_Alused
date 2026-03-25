"""
Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab
ekraanile nimelise tervituse koos tekstiga, mis ütleb, kas tegemist
on 7-18-aastase inimesega.
"""

def name_and_age():
    name = str(input("Sisestage oma nimi: "))
    age = int(input("Sisestage oma vanus: "))
    if age >= 7 and age <= 18:
        print(f"Tere {name}, teie vanus on selles grupis.")
    else:
        print(f"Tere {name}, teie vanus ei ole selles grupis.")


if __name__ == "__main__":
    name_and_age()