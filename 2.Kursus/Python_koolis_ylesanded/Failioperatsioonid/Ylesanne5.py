"""Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt ühesugunem (näit. "kook", "kuulilennuteetunneliluuk" jne).
Loo programm, mis trükib ekraanile välja kõik tekstifailis olevad sõnad, mis on palindroomid. Alustekstiks võid kasutada suvalist teksti,
kuid katsetada tasuks ka sõnaloenditega, kus iga sõna asub eraldi real (näit. eesti keele sõnade algvormid e. lemmad veebilehelt http://www.eki.ee/tarkvara/wordlist/)."""

def add_palindroom(filename):
    list = [
        "kook on siin ja siis",
        "sos",
        "lol",
        "kes",
        "kuulilennuteetunneliluuk",
    ]
    with open(filename, "w", encoding="utf-8") as f:
        for rida in list:
            f.write(rida + "\n")


def check_if_palindroom(filename):
    with open(filename, "r", encoding="utf-8") as f:
        sisu = f.read()
        sonad = sisu.split()
        for sona in sonad:
            word = sona.strip().lower()
            word_back = sona.lower().strip()[::-1]
            if word == word_back:
                print(word)



if __name__ == "__main__":
    filename = "palindroomid.txt"
    add_palindroom(filename)
    check_if_palindroom(filename)