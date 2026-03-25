def eelarve(guests: int) -> int:
    """Ruumi rent 55€ + per külaline 10€"""

    place_price = 55
    price_per_quest = 10
    return place_price + price_per_quest * guests
if __name__ == "__main__":
    invited_quests = int(input("Palju inimesi on kutsutud?"))
    confirmed_quests = int(input("Mitu külalist tuleb kindlalt?"))
    min_budget = eelarve(confirmed_quests)
    max_budget = eelarve(invited_quests)
    print(f"Maksimaalne eelarve on {max_budget} €")
    print(f"Minimaalne eelarve on {min_budget} €")