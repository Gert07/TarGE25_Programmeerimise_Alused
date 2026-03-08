"""Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon)."""

from Ylesanne2 import add_poem

def line_print(lineNumber: int, fileName: str) -> None:
    message = ""
    with open(fileName, encoding="utf-8") as f:
        for index, line in enumerate(f):
            if (index + 1) == lineNumber:
                print(message + line)
                break
        else:
            print("Viga, luuletus pole nii palju ridu")

if __name__ == "__main__":
    filename = "luuletus.txt"
    add_poem(filename)
    user_input = input("Mitmendat rida soovid kuvada: ")
    if user_input.isdigit():
        line_print(int(user_input), filename)
    else:
        print("Viga, sisesta täisarv")

