"""
Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning
väljastab ekraanile ristküliku ümbermõõdu ja pindala.
"""

def compute_rectangle():
    width = float(input("Kirjuta ristküliku laius: "))
    length = float(input("Kirjuta ristküliku pikkus: "))
    P = 2 * (width + length)
    S = width * length
    print(f"Antud ristküliku pindala on {S}")
    print(f"Antud ristküliku ümbermõõt on {P}")

if __name__ == "__main__":
    compute_rectangle()
