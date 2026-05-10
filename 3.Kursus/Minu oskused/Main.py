from PCBuild import *

# Hardware catalog: brand, model, GB, price

CPU_CATALOG = [
    ("Intel", "Core i9-14900K", None, 589.00),
    ("Intel", "Core i7-14700K", None, 389.00),
    ("Intel", "Core i5-14600K", None, 319.00),
    ("Intel", "Core i5-13400F", None, 179.00),
    ("Intel", "Core i3-13100", None, 129.00),
    ("AMD", "Ryzen 9 7950X", None, 699.00),
    ("AMD", "Ryzen 9 7900X", None, 449.00),
    ("AMD", "Ryzen 7 7700X", None, 299.00),
    ("AMD", "Ryzen 5 7600X", None, 249.00),
    ("AMD", "Ryzen 5 5600X", None, 149.00),
]

GPU_CATALOG = [
    ("NVIDIA", "RTX 4090", None, 1999.00),
    ("NVIDIA", "RTX 4080 Super", None, 1299.00),
    ("NVIDIA", "RTX 4070 Ti Super", None, 799.00),
    ("NVIDIA", "RTX 4070 Super", None, 599.00),
    ("NVIDIA", "RTX 4060 Ti", None, 399.00),
    ("NVIDIA", "RTX 4060", None, 299.00),
    ("AMD", "RX 7900 XTX", None, 999.00),
    ("AMD", "RX 7800 XT", None, 499.00),
    ("AMD", "RX 7600", None, 269.00),
    ("Intel", "Arc A770", None, 349.00),
]

RAM_CATALOG = [
    ("Corsair", "Vengeance DDR5", 32, 109.00),
    ("Corsair", "Vengeance DDR5", 64, 189.00),
    ("Corsair", "Vengeance DDR4", 16, 49.00),
    ("G.Skill", "Trident Z5 DDR5", 32, 119.00),
    ("G.Skill", "Trident Z5 DDR5", 64, 209.00),
    ("G.Skill", "Ripjaws V DDR4", 16, 44.00),
    ("Kingston", "Fury Beast DDR5", 32, 99.00),
    ("Kingston", "Fury Beast DDR4", 16, 42.00),
    ("Crucial", "Pro DDR5", 32, 94.00),
    ("Crucial", "Ballistix DDR4", 16, 40.00),
]


def show_catalog(catalog, has_gb=False):
    for i, entry in enumerate(catalog, 1):
        brand, model, gb, price = entry
        if has_gb:
            print(f"{i}. {brand} {model} {gb}GB - ${price:.2f}")
        else:
            print(f"{i}. {brand} {model} - ${price:.2f}")


def pick_from_catalog(catalog):
    while True:
        choice = input(f"Enter number (1-{len(catalog)}) or 0 for custom: ")

        try:
            number = int(choice)
        except ValueError:
            print("Please enter a number.")
            continue

        if number == 0:
            return None
        if 1 <= number <= len(catalog):
            return catalog[number - 1]

        print("That number is not in the catalog.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Price cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be positive.")
        except ValueError:
            print("Please enter a whole number.")


def input_cpu():
    print("\nCPU Catalog")
    show_catalog(CPU_CATALOG)

    entry = pick_from_catalog(CPU_CATALOG)
    if entry:
        brand, model, _, price = entry
        print(f"Selected: {brand} {model}")
        return CPU(brand, model, price)

    print("Custom CPU")
    brand = input("Brand: ")
    model = input("Model: ")
    price = get_float("Price: ")
    CPU_CATALOG.append((brand, model, None, price))
    return CPU(brand, model, price)


def input_gpu():
    print("\nGPU Catalog")
    show_catalog(GPU_CATALOG)

    entry = pick_from_catalog(GPU_CATALOG)
    if entry:
        brand, model, _, price = entry
        print(f"Selected: {brand} {model}")
        return GPU(brand, model, price)

    print("Custom GPU")
    brand = input("Brand: ")
    model = input("Model: ")
    price = get_float("Price: ")
    GPU_CATALOG.append((brand, model, None, price))
    return GPU(brand, model, price)


def input_ram():
    print("\nRAM Catalog")
    show_catalog(RAM_CATALOG, has_gb=True)

    entry = pick_from_catalog(RAM_CATALOG)
    if entry:
        brand, model, gb, price = entry
        print(f"Selected: {brand} {model} {gb}GB")
        return RAM(brand, model, gb, price)

    print("Custom RAM")
    brand = input("Brand: ")
    model = input("Model: ")
    gb = get_int("Size (GB): ")
    price = get_float("Price: ")
    RAM_CATALOG.append((brand, model, gb, price))
    return RAM(brand, model, gb, price)


def main():
    print("PC Hardware Cost Estimator")

    build_name = input("Build name: ")
    if not build_name:
        build_name = "My Build"

    build = PCBuild(build_name)

    build.add_component(input_cpu())
    build.add_component(input_gpu())
    build.add_component(input_ram())

    while True:
        print("\nAdd another component?")
        print("1. CPU")
        print("2. GPU")
        print("3. RAM")
        print("4. Done")

        choice = input("Choice: ")
        if choice == "1":
            build.add_component(input_cpu())
        elif choice == "2":
            build.add_component(input_gpu())
        elif choice == "3":
            build.add_component(input_ram())
        elif choice == "4":
            break
        else:
            print("Please enter 1, 2, 3, or 4.")

    build.display_summary()


if __name__ == "__main__":
    main()
