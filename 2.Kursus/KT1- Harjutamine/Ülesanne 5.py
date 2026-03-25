"""1.	Küsi kasutajalt lause
2.	Kui lauses on vähem kui 5 sõna, jäta lause meelde ja küsi uus lause (Kordus, Järjend)
3.	Kuva pikas lauses (5 või rohkem sõna) olevad sõnad eraldi real"""

def ask_sentence():
    sentence = ""
    count = len(sentence)
    list = []
    #While tsükkel algab, kestab nii kaua kuni saame > kui 5 sõna
    while count < 5:
        sentence = str(input("Kirjuta lause: "))
        count = len(sentence.split())
        list.append(sentence)
    #Tsükkel läbi,
    words = sentence.split()
    for word in words:
        print(word)


if __name__ == "__main__":
    ask_sentence()