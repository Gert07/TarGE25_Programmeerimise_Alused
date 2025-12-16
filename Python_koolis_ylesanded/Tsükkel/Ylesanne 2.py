"""
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.
"""

def while_tsykkel():
    count = 0
    total = 0
    while count < 10:
        number = float(input(f"Sisesta {count + 1}. arv: "))
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}")

def for_tsykkel():
    total = 0
    for i  in range(10):
        number = float(input(f"Sisesta {i+1}. arv: "))
        total += number
    print(f"Sisestatud arvude summa on: {total}")


def infinite_while_tsykkel():
    count = 0
    total = 0
    while True:
        text_input = input(f"Sisesta {count + 1}. arv: ")
        if not text_input.isnumeric():
            break
        number = float(text_input)
        total += number
        count += 1
    print(f"Sisestatud arvude summa on {total}")


if __name__ == "__main__":
    while_tsykkel()
    for_tsykkel()
    infinite_while_tsykkel()
