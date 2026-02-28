"""Lihtsa sõnaraamatu jaoks koosta neli järjendit (arv, eesti, inglise, itaalia) sisuga: arv - 1, 2, 3, 4 eesti - üks,
kaks, kolm, neli inglise - one, two, three, four itaalia - uno, due, tre, quattro

Väljasta kõik elemendid tabelina ekraanile:
1 - üks - one - uno
2 - kaks - two - due ...

Lisa arvude ja eesti järjendile veel kaks elementi.
Kontrolli, kas itaalia sõnade järjendis eksiteerib element 'tre'
Väljasta kõigi nelja järjendi elemendid tähestikulises järjekorras kasvavalt."""

def main():
    numbers = [1,2,3,4]
    estonia = ["üks","kaks","kolm","neli"]
    english = ["one", "two", "three", "four"]
    italy = ["uno","due","tre","quattro"]
    for i in range(len(numbers)):
        """Alt + ä ja space = ^ Sellega saab joondada"""
        print(f"{numbers[i]} - {estonia[i]:^4} - {english[i]:^5} - {italy[i]:^7}")
        """kontrollime kas tre on listis"""
    if "tre" in italy:
        print("tre eksisteerib itaalia järjekorras")

    """Lisame numbrid 5 ja 6 listi"""
    numbers += [5, 6]
    """Lisame sõnad "viis" ja "kuus" järjendisse"""
    estonia.append("viis")
    estonia.append("kuus")
    print("numbrid sorteeritud")
    numbers.sort()
    for number in numbers:
        print(number)
    print("sorteeritud tähed, vastavalt listide järjekorras")
    all_languages = sorted(estonia)
    all_languages += sorted(english)
    all_languages += sorted(italy)
    for value in all_languages:
        print(value)
    print("kõik sorteeritud tähestiku järjekorras")
    all_languages.sort()
    for value in all_languages:
        print(value)



if __name__ == "__main__":
    main()