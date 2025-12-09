"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab
tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii, et võimalik oleks
teisendamine nii üht- kui teistpidi? Proovi.
"""
def temperatuuri_konverteerija():
    suund = input("Millist kraadi soovite teisendada (C->F sisestage C, F->C = sisestage F): ")

    if suund.upper() == "C":
        celsius_i = float(input("Sisestage kraadid Celsiuses: "))
        fahr_o = (celsius_i * 9/5) + 32
        print(fahr_o)
    elif suund.upper() == "F":
        fahr_i = float(input("Sisestage kraadid Fahrenheitites: "))
        celsius_o = (fahr_i - 32) * 5/9
        print(celsius_o)
    else:
        print("Viga")

if __name__ == "__main__":
    temperatuuri_konverteerija()