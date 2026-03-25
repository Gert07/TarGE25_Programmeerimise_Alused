"""1. Küsi kasutjalt 3 arvu
2. Väikseim arv korruta kahega
3. Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni
4. Teata kas kasutaja vastas õigesti või valesti
5. Programmi lõpus näita kasutaja valesti vastatud ruutude õiged tulemused"""

# Funktsioon, mis küsib kasutajalt 3 arvu
def get_numbers():
    numbers = []
    for i in range(3):
        n = int(input(f"Sisesta {i+1}. arv: "))
        numbers.append(n)
    return numbers

# Funktsioon, mis küsib ruute ja salvestab valed vastused
def ask_squares(limit):
    wrong_answers = []  # järjend valede vastuste jaoks
    for i in range(1, limit + 1):
        answer = int(input(f"Mis on arvu {i} ruut? "))
        correct = i ** 2
        if answer == correct:
            print("Õige!")
        else:
            print("Vale!")
            wrong_answers.append((i, correct))
    return wrong_answers

# Peafunktsioon
def main():
    # 1. Küsi kasutajalt 3 arvu
    numbers = get_numbers()

    # 2. Väikseim arv korruta kahega
    smallest = min(numbers)
    limit = smallest * 2
    print(f"Väikseim arv on {smallest}, korrutatud kahega = {limit}\n")

    # 3–4. Küsi ruute ja kontrolli vastuseid
    wrong_answers = ask_squares(limit)

    # 5. Näita valesti vastatud ruutude õiged tulemused
    if wrong_answers:
        print("\nVales, õige vastus:")
        for number, correct in wrong_answers:
            print(f"{number}² = {correct}")
    else:
        print("\nKõik vastused olid õiged! Tubli!")

if __name__ == "__main__":
    main()
