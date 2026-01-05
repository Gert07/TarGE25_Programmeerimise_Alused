"""Ül 3.
1.	Küsi kasutaja vanust ja nime
2.	Õnnitle kasutajat iga täisealisena veedetud aasta eest (Kordus)
3.	Iga õnnitluse järel küsi ja salvest antud aasta meeleolu (Järjend)
4.	Programmi lõpus kuva meeleolud nende pikkuse järjekorras"""

# Funktsioon, mis küsib kasutaja nime ja vanuse
def get_user_data():
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus: "))
    return name, age

# Funktsioon, mis kogub täisealise aastate meeleolud
def collect_moods(name, age):
    moods = []  # järjend meeleolude jaoks
    if age < 18:
        print(f"{name}, sa ei ole veel täisealine.")
        return moods
    else:
        adult_years = age - 18
        for i in range(1, adult_years+1):
            print(f"Õnnitlused {name}! Oled olnud täisealine {i} aastat.")
            mood = input(f"Mis oli sinu meeleolu {i}. täisealise aasta jooksul? ")
            moods.append(mood)
        return moods


# Peafunktsioon
def main():
    # 1. Küsi kasutaja vanust ja nime
    name, age = get_user_data()

    # 2–3. Õnnitle ja kogu meeleolud
    moods = collect_moods(name, age)

    # 4. Kuva meeleolud nende pikkuse järjekorras
    if moods:
        print("\nMeeleolud pikkuse järjekorras:")
        for mood in sorted(moods, key=len):
            print(mood)
    else:
        print("\nPole meeleolusid kuvada.")


if __name__ == "__main__":w
    main()