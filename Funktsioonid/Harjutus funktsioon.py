"""Function examples."""


#func()
def func():
    print("I'm inside the function")

#my_name_is(name)
def my_name_is(name: str) -> str:
    print(f"My name is {name}")

#sum_six(num)
def sum_six(num: int) -> str:
    return f"{num}+{6}={num+6}"

#sum_numbers()
def sum_numbers(a, b: int):
    return f"{a}+{b}={a+b}"

#usd_to_eur()
def usd_to_eur(dollars: int):
    eur = (dollars * 0.8)
    return eur

