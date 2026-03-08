"""Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.

Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea järjekorranumbri ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse."""
from Tekstifailid.cooper import results

def add_poem(filename):
    luuletus = [
        "Hommikul kui üles ärkan,",
        "arvutit ma laual märkan.",
        "Padja, teki viskan maha,",
        "jooksen ruttu compu taha.",
        "Kiirelt sisestan parooli,",
        "kuid juba tuleb minna kooli.",
        "Error tuleb ette siis,",
        "kool on mulle räme piin."
    ]
    # faili loomine ja luuletuse kirjutamine
    with open(filename, "w", encoding="utf-8") as f:
        for rida in luuletus:
            f.write(rida + "\n")

def read_poem(filename):
    # failist lugemine ja ekraanile kuvamine
    with open(filename, "r", encoding="utf-8") as f:
        for nr, rida in enumerate(f, start=1):
            rida = rida.rstrip("\n")
            pikkus = len(rida)
            print(f"{nr}. {rida} ({pikkus})")

if __name__=="__main__":
    filename = "luuletus.txt"
    add_poem(filename)
    read_poem(filename)
