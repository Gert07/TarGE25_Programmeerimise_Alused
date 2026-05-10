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