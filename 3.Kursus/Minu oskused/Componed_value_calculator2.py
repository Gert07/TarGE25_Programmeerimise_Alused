# ─────────────────────────────────────────────
#  HARDWARE CATALOG  (brand, model, GB, price)
# ─────────────────────────────────────────────

CPU_CATALOG = [
    ("Intel",  "Core i9-14900K",    None,  589.00),
    ("Intel",  "Core i7-14700K",    None,  389.00),
    ("Intel",  "Core i5-14600K",    None,  319.00),
    ("Intel",  "Core i5-13400F",    None,  179.00),
    ("Intel",  "Core i3-13100",     None,  129.00),
    ("AMD",    "Ryzen 9 7950X",     None,  699.00),
    ("AMD",    "Ryzen 9 7900X",     None,  449.00),
    ("AMD",    "Ryzen 7 7700X",     None,  299.00),
    ("AMD",    "Ryzen 5 7600X",     None,  249.00),
    ("AMD",    "Ryzen 5 5600X",     None,  149.00),
]

GPU_CATALOG = [
    ("NVIDIA", "RTX 4090",          None, 1999.00),
    ("NVIDIA", "RTX 4080 Super",    None, 1299.00),
    ("NVIDIA", "RTX 4070 Ti Super", None,  799.00),
    ("NVIDIA", "RTX 4070 Super",    None,  599.00),
    ("NVIDIA", "RTX 4060 Ti",       None,  399.00),
    ("NVIDIA", "RTX 4060",          None,  299.00),
    ("AMD",    "RX 7900 XTX",       None,  999.00),
    ("AMD",    "RX 7800 XT",        None,  499.00),
    ("AMD",    "RX 7600",           None,  269.00),
    ("Intel",  "Arc A770",          None,  349.00),
]

RAM_CATALOG = [
    ("Corsair",  "Vengeance DDR5",   32,   109.00),
    ("Corsair",  "Vengeance DDR5",   64,   189.00),
    ("Corsair",  "Vengeance DDR4",   16,    49.00),
    ("G.Skill",  "Trident Z5 DDR5",  32,   119.00),
    ("G.Skill",  "Trident Z5 DDR5",  64,   209.00),
    ("G.Skill",  "Ripjaws V DDR4",   16,    44.00),
    ("Kingston", "Fury Beast DDR5",  32,    99.00),
    ("Kingston", "Fury Beast DDR4",  16,    42.00),
    ("Crucial",  "Pro DDR5",         32,    94.00),
    ("Crucial",  "Ballistix DDR4",   16,    40.00),
]


# ─────────────────────────────────────────────
#  OOP CLASSES
# ─────────────────────────────────────────────

class HardwareComponent:
    LABEL_W  = 4
    DETAIL_W = 38

    def __init__(self, name, brand, model, price):
        self.name  = name
        self.brand = brand
        self.model = model
        self.price = price

    def detail_str(self):
        return f"{self.brand} {self.model}"

    def __str__(self):
        label  = self.name.ljust(self.LABEL_W)
        detail = self.detail_str().ljust(self.DETAIL_W)
        return f"  {label}  {detail}  ${self.price:>9,.2f}"


class CPU(HardwareComponent):
    def __init__(self, brand, model, price):
        super().__init__("CPU", brand, model, price)


class GPU(HardwareComponent):
    def __init__(self, brand, model, price):
        super().__init__("GPU", brand, model, price)


class RAM(HardwareComponent):
    def __init__(self, brand, model, capacity_gb, price):
        super().__init__("RAM", brand, model, price)
        self.capacity_gb = capacity_gb

    def detail_str(self):
        return f"{self.brand} {self.model} {self.capacity_gb}GB"


class PCBuild:
    def __init__(self, build_name):
        self.build_name = build_name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def total_cost(self):
        return sum(c.price for c in self.components)

    def display_summary(self):
        L = HardwareComponent.LABEL_W   # 4  — "CPU", "GPU", "RAM", "Part"
        D = HardwareComponent.DETAIL_W  # 38 — details column
        P = 9                           # price field width: "1,999.00"
        # Every line follows:  "  {label:<L}  {detail:<D}  ${price:>P}"
        W = 2 + L + 2 + D + 2 + 1 + P  # 2+4+2+38+2+1+9 = 58

        # Component __str__: f"  {label:<L}  {detail:<D}  ${price:>P,.2f}"
        # Dollar sign is always at position: 2+L+2+D+2 = 48
        dollar_at = 2 + L + 2 + D + 2  # = 48

        def row(label, detail, price_str):
            # label + detail fill the left side; price_str goes after the $
            left = f"  {label:<{L}}  {detail:<{D}}"
            return f"{left}  ${price_str:>{P}}"

        print("\n" + "=" * W)
        print(f"  BUILD: {self.build_name}")
        print("=" * W)
        print(row("Part", "Details", " Price"))
        print("-" * W)
        for c in self.components:
            print(c)
        print("-" * W)
        # TOTAL: pad left side to dollar_at chars, then $price
        left = f"  {'TOTAL':<{dollar_at - 2}}"
        print(f"{left}${self.total_cost():>{P},.2f}")
        print("=" * W)


# ─────────────────────────────────────────────
#  CATALOG DISPLAY & PICKER
# ─────────────────────────────────────────────

def show_catalog(catalog, has_gb=False):
    print(f"  {'#':<4} {'Brand':<10} {'Model':<24}", end="")
    if has_gb:
        print(f" {'GB':>4}", end="")
    print(f"  {'Price':>9}")
    print(f"  {'-'*4} {'-'*10} {'-'*24}", end="")
    if has_gb:
        print(f" {'-'*4}", end="")
    print(f"  {'-'*9}")
    for i, entry in enumerate(catalog, 1):
        brand, model, gb, price = entry
        print(f"  {i:<4} {brand:<10} {model:<24}", end="")
        if has_gb:
            print(f" {gb:>4}", end="")
        print(f"  ${price:>8,.2f}")


def pick_from_catalog(catalog, has_gb=False):
    """Show catalog, let user pick by number or enter custom. Returns component tuple."""
    while True:
        choice = input(f"\n  Enter number (1-{len(catalog)}) or 0 for custom: ").strip()
        try:
            n = int(choice)
        except ValueError:
            print(f"  Please enter a number between 0 and {len(catalog)}.")
            continue

        if n == 0:
            return None  # custom entry
        elif 1 <= n <= len(catalog):
            return catalog[n - 1]
        else:
            print(f"  Please enter a number between 0 and {len(catalog)}.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt).replace(",", ""))
            if value < 0:
                print("    Price can't be negative. Try again.")
                continue
            return value
        except ValueError:
            print("    Please enter a valid number.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("    Must be a positive number.")
                continue
            return value
        except ValueError:
            print("    Please enter a whole number.")


# ─────────────────────────────────────────────
#  INPUT FUNCTIONS
# ─────────────────────────────────────────────

def input_cpu():
    print("\n┌─ CPU Catalog ──────────────────────────────────────────")
    show_catalog(CPU_CATALOG)
    print("└────────────────────────────────────────────────────────")

    entry = pick_from_catalog(CPU_CATALOG)
    if entry:
        brand, model, _, price = entry
        print(f"  ✔ Selected: {brand} {model}  —  ${price:,.2f}")
        return CPU(brand, model, price)
    else:
        print("  Custom CPU:")
        brand = input("    Brand : ").strip()
        model = input("    Model : ").strip()
        price = get_float("    Price ($): ")
        CPU_CATALOG.append((brand, model, None, price))
        print(f"  ✔ Added to catalog as #{len(CPU_CATALOG)}")
        return CPU(brand, model, price)


def input_gpu():
    print("\n┌─ GPU Catalog ──────────────────────────────────────────")
    show_catalog(GPU_CATALOG)
    print("└────────────────────────────────────────────────────────")

    entry = pick_from_catalog(GPU_CATALOG)
    if entry:
        brand, model, _, price = entry
        print(f"  ✔ Selected: {brand} {model}  —  ${price:,.2f}")
        return GPU(brand, model, price)
    else:
        print("  Custom GPU:")
        brand = input("    Brand : ").strip()
        model = input("    Model : ").strip()
        price = get_float("    Price ($): ")
        GPU_CATALOG.append((brand, model, None, price))
        print(f"  ✔ Added to catalog as #{len(GPU_CATALOG)}")
        return GPU(brand, model, price)


def input_ram():
    print("\n┌─ RAM Catalog ───────────────────────────────────────────")
    show_catalog(RAM_CATALOG, has_gb=True)
    print("└─────────────────────────────────────────────────────────")

    entry = pick_from_catalog(RAM_CATALOG, has_gb=True)
    if entry:
        brand, model, gb, price = entry
        print(f"  ✔ Selected: {brand} {model} {gb}GB  —  ${price:,.2f}")
        return RAM(brand, model, gb, price)
    else:
        print("  Custom RAM:")
        brand = input("    Brand    : ").strip()
        model = input("    Model    : ").strip()
        gb    = get_int("    Size (GB): ")
        price = get_float("    Price ($): ")
        RAM_CATALOG.append((brand, model, gb, price))
        print(f"  ✔ Added to catalog as #{len(RAM_CATALOG)}")
        return RAM(brand, model, gb, price)


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 58)
    print("          PC HARDWARE COST ESTIMATOR")
    print("=" * 58)

    build_name = input("\n  Build name (e.g. Gaming Rig): ").strip()
    if not build_name:
        build_name = "My Build"

    build = PCBuild(build_name)

    build.add_component(input_cpu())
    build.add_component(input_gpu())
    build.add_component(input_ram())

    while True:
        print("\n  Add another component?")
        print("  1. CPU   2. GPU   3. RAM   4. Done")
        choice = input("  Choice: ").strip()
        if choice == "1":
            build.add_component(input_cpu())
        elif choice == "2":
            build.add_component(input_gpu())
        elif choice == "3":
            build.add_component(input_ram())
        elif choice == "4":
            break
        else:
            print("  Please enter 1, 2, 3, or 4.")

    build.display_summary()


if __name__ == "__main__":
    main()