"""1.	Küsi kasutaja sugu ja vanus
2.	Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
3.	Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda.
4.	Salvesta järjendisse iga kolmas tervitus ja viimane
5.	Kuva ekraanile järjendis olevate tervituste eelviimased sõnad"""

def get_greeting(gender, age):
    if gender == "mees":
        if age < 18:
            return f"Tere noormees, sa oled {age} aastat vana"
        elif age < 65:
            return f"Tere härra, sa oled {age} aastat vana"
        else:
            return f"Tere vanahärra, sa oled {age} aastat vana"
    if gender == "naine":
        if age < 18:
            return f"Tere neiu, sa oled {age} aastat vana"
        elif age < 65:
            return f"Tere proua, sa oled {age} aastat vana"
        else:
            return f"Tere vanaproua, sa oled {age} aastat vana"

def greeting_program():
    gender = input("What is your gender? ")
    age = int(input("What is your age? "))

    greetings = []
    saved = []

    previous = ""
    for i in range(10):
        greetings = get_greeting(gender, age)
        append.greetings(greetings)
        if previous and greetings != previous:
            break

        previous = greetings
        age += 1

    for i in range(len(greetings)):
        if (i + 1) % 3 == 0:
            saved.append(greetings[i])

    if greetings[-1] not in saved:
        saved.append(greetings[-1])

    print("Eelviimased sõnad: ")
    for x in saved:
        words = x.split()
        if len(words) >= 2:
            print(words[-2])


if __name__ == "__main__":
    greeting_program()