"""Function examples."""


# func()
def func():
    """Print a message from inside the function."""
    print('I´m inside the function')


# my_name_is(name)
def my_name_is(name: str) -> str:
    """Print given name."""
    print(f"My name is {name}")


# sum_six(num)
def sum_six(num: int):
    """Return the sum of 6 digits."""
    return num + 6


# sum_numbers()
def sum_numbers(a, b: int):
    """Return the sum of (a, b)."""
    return a + b


# usd_to_eur()
def usd_to_eur(dollars: int):
    """Convert dollars to Euro."""
    eur = (dollars * 0.8)
    return eur