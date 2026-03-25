"""Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN.
Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks:"""

def main(size: int, symbol: str, alt: str):
    for x in range(size):
        for y in range(size):
            if x == y or x + y == size -1:
                print(f"{alt}", end=" ")
            else:
                print(f"{symbol}", end=" ")
        print()



if __name__ == "__main__":
    size = int(input("Sisesta ruudu suurus (täisarv): "))
    main(size, "o", "x")
    main(size * 2, "I", "-")