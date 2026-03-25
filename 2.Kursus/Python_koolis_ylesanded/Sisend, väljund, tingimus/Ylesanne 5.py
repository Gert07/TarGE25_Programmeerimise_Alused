"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab
tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii, et võimalik oleks
teisendamine nii üht- kui teistpidi? Proovi.
"""
def convert_to_fahrenheit(temp_celsius: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return temp_celsius * 1.8 + 32

def convert_to_celsius(temp_fahrenheit: float) -> float:
    """Convert to celsius"""
    return (temp_fahrenheit - 32) / 1.8

if __name__ == "__main__":
    suund = input("Määra sisestava temperatuuri ühik (C/F): ")
    if suund.upper() == "C":
        temp_celsius = float(input("Sisestage kraad Celsiuses: "))
        temp_fahrenheit = convert_to_fahrenheit(temp_celsius)
        print(f"{temp_celsius} C on {temp_fahrenheit:.2f} F kraadi")
    elif suund.upper() == "F":
        temp_fahrenheit = float(input("Sisestage kraad Fahrenheitides: "))
        temp_celsius = convert_to_celsius(temp_fahrenheit)
        print(f"{temp_fahrenheit} F on {temp_celsius:.2f} C kraadi")
    else:
        print("Viga, valesti sisestatud sümbol.")
