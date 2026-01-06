"""Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni. nt:"""

from random import randint

def main(min_value: int, max_value:int):
    random_number = randint(min_value, max_value)
    count = 0
    while count < 5:
        user_input = int(input("Sisesta täisarv vahemikus 1-20: "))
        count += 1
        if user_input < random_number:
            print("Liiga väike. Proovi uuesti")
        elif user_input > random_number:
            print("Liiga suur. Proovi uuesti")
        else:
            print(f"Õige! Vastus oli {random_number}. Arvasid ära {count} katsega.")
            break
    else:
        print(f"Vale, õige vastus oli {random_number}.")


if __name__ == "__main__":
    main(1, 20)