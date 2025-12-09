"""
Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer),
millele antakse samuti ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte
arvulisel kujul, vaid esitatakse "haukudes". Igaks juhuks: tsükleid pole vaja
kasutada, me pole neid veel õppinud.

Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: auh auh auh auh auh
"""

def calculator_auh():
    num1 = int(input("Sisestage esimene täisarvuline arv: "))
    num2 = int(input("Sisestage teine täisarvuline arv: "))
    tehe = input("Sisestage tehe (+,-,*,/): ")
    if tehe == "+":
        tulemus = num1 + num2
    elif tehe == "-":
        tulemus = num1 - num2
    elif tehe == "*":
        tulemus = num1 * num2
    elif tehe == "/":
        tulemus = num1 / num2
    else:
        print("Tundmatu tehe.")
    auh = int(tulemus) * "auh "
    print(f"Tulemus: {auh}")



if __name__ == "__main__":
    calculator_auh()