import random
"""1. Make hola string
Funktsioon saab sisendiks arvu, mis näitab, mitu korda peab sõna "hola" sisalduma funktsiooni väljundis.
Ülesanne tuleks lahendada while tsükliga nii, et iga kord, kui väljundsõnale on liidetud hola, siis count
väärtus väheneb ühe võrra. While tsükkel kestab seni, kuni count väärtus on 0."""

def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    total = ""
    while count > 0:
        total += "hola"
        count -= 1
    return total


"""2. String with random length
Selles funktsioonis kasutame juhuslikke arve. Ülesande sõnastus on järgmine:

hakkame koostama sõne, mis koosneb miinusmärkidest (-)
võta üks juhuslik arv (vahemikus 0 kuni 1)
kui see arv on alla teatud piiri (threshold), siis lisame sõnesse ühe miinusmärgi
kui see juhuslik arv on üle piiri või piiriga võrdne, siis lõpetame sõne koostamise ära"""

def generate_random_length_string(threshold: float) -> str:
    """
    Generate a string of "-" until random numbers is below threshold.

    Use random.random() to generate a random float.
    If the random number is below threshold, add "-" to result.
    If the random number is greater or equal to the threshold, finish the loop.

    generate_string_with_random_length(0.9) => "-----" (result can vary)
    generate_string_with_random_length(0.5) => "-" (usually empty or 1 minus)
    """
    total = ""
    while True:
        r = random.random()
        if r < threshold:
            total += "-"
        else:
            break
    return total


"""3. Kasutaja vanuse küsimine
kui sisestatud vanus pole üldse korrektne arv, prinditakse Wrong input!
kui sisestatud vanus on liiga väike, prinditakse Too young!
kui sisestatud vanus on liiga suur, prinditakse Too old!"""

def ask_user_age(age_limit: int) -> int:
    """
    Ask user age.

    You have to ask the user his/her age using input("What is your age?").
    You have to repeat this process until a correct age is entered.
    The age is correct if:
    - it is numeric (answering "a" is not correct)
    - it is greater or equal to the age_limit
    - it is less or equal to 100

    So, if the user enters a wrong age, the user gets a warning.
    The question is repeated until a correct age is entered.
    The function returns the correct age as int.

    Warning is printed out:
    - non numberic input: Wrong input!
    - age < age_limit: Too young!
    - age > 100: Too old!

    An example (with age_limit 18):
    What is your age? a
    Wrong input!
    What is your age? 10
    Too young!
    What is your age? 101
    Too old!
    What is your age? 21

    (function returns 21)
    """
    while True:
        user_input = input("What is your age?")
        try:
            age = int(user_input)
        except ValueError:
            print("Wrong input!")
            continue
        if age < age_limit:
            print("Too young!")
        elif age > 100:
            print("Too old!")
        else:
            return age


if __name__ == '__main__':
    make_hola_string(3)
    generate_random_length_string(1)
    ask_user_age(100)