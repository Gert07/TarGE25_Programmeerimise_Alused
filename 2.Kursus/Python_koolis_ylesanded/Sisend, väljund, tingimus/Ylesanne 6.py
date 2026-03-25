"""
Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige, lineaarliige, vabaliige)
kordajad ning arvutab nende põhjal diskriminandi ja väljastab selle põhjal ruutvõrrandi lahendid.
Nagu tead, võib lahendeid vastavalt diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa.
"""
import math



def calc_ruutvorrand(a: float, b: float, c: float) -> float:
    """Arvutame ruutvõrrandi."""
    return b ** 2 - 4 * a * c


def solve_quadratic_equasion(a, b, diskriminant, useAddition):
    if useAddition:
        top = -b + math.sqrt(diskriminant)
    else:
        top = -b - math.sqrt(diskriminant)
    bottom = 2 * a
    return top / bottom


if __name__ == "__main__":

    print("Arvutame ruutvõrrandit!")
    a = float(input("sisestage ruutliige: "))
    if a == 0:
        print("Ruutliige ei tohi olla null")
    else:
        b = float(input("Sisestage lineaarliige: "))
        c = float(input("Sisestage vabaliige: "))
        diskriminant = calc_ruutvorrand(a, b, c)
        if diskriminant < 0:
            print("Lahendid puuduvad")
        elif diskriminant == 0:
            solution = solve_quadratic_equasion(a, b, diskriminant, True)
            print(f"Lahendid on võrdsed: {solution}")
        else:
            solution1 = solve_quadratic_equasion(a, b, diskriminant, True)
            solution2 = solve_quadratic_equasion(a, b, diskriminant, False)
            print(f"Lahendid on võrdsed: {solution1} ja {solution2}")
