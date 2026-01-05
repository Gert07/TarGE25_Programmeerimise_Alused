"""1.	Kasutajalt küsitakse sõna.
2.	Kasutajalt küsitakse numbrit.
3.	Loo järjend, kus antud sõna on korrutatud kasvavalt kuni antud numbrini (kordus, järjend).
4.	Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
5.	Kuva järjendi viimane väärtus"""

def word_and_number():
    word = str(input("Sisesta sõna: "))
    number = int(input("Sisesta täisarv: "))
    list = []
    if number > 10:
        print("Viga")
    else:
        for i in range(1, number + 1):
            tehe = word * i
            list.append(tehe)
    print(list[number-1])


if __name__ == '__main__':
    word_and_number()
