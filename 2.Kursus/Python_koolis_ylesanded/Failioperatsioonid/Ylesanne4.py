"""Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib
 failis luuletus.txt uut rida lisada ning seejärel lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin."""

from Ylesanne2 import add_poem

def what_row_to_add(filename, add_row, poem_line):
    with open(filename, encoding="utf-8") as f:
        rows = f.readlines()
    new_rows = []
    found = False
    for row in rows:
        new_rows.append(row)
        if row.strip() == poem_line:
            new_rows.append(add_row + "\n")
            found = True
    if not found:
        print("Antud rida ei leitud")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.writelines(new_rows)



if __name__ == "__main__":
    filename = "luuletus4.txt"
    add_poem(filename)
    poem_line = input("Sisesta rida, mille järele soovid uut rida lisada:")
    add_row = input("Sisesta rida, mida soovid lisada:")
    what_row_to_add(filename, add_row, poem_line)
    with open(filename, encoding="utf-8") as f:
        print(f.read())