"""
Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5
"""


def calculator():
    number_1 = float(input("Sisestage esimene arv: "))
    number_2 = float(input("Sisestage teine arv: "))
    tehe = input("Sisestage tehe (+,-,*,/): ")
    if tehe == "+":
        tulemus = number_1 + number_2
    elif tehe == "-":
        tulemus = number_1 - number_2
    elif tehe == "*":
        tulemus = number_1 * number_2
    elif tehe == "/":
        tulemus = number_1 / number_2
    else:
        print("Tundmatu tehe.")

    print(f"Tulemus: {number_1}{tehe}{number_2}={tulemus}")


if __name__ == "__main__":
    calculator()