def elektrihind(skwh: float) -> float:
    """Konverteerib elektrihinna senti kilovatt tunni kohta, megavatt tunniks"""
    price_eur = skwh / 100
    return price_eur * 1000

if __name__ == "__main__":
    given_price_str = input("Sisesta elektrihind sentides kilovatt-tunni kohta.")
    converted_price = elektrihind(float(given_price_str))
    print(f"{given_price_str} s/kWh on {converted_price} €/MWh")
