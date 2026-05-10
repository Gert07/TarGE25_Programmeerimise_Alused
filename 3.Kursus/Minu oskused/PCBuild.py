from HardwareComponents import *

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