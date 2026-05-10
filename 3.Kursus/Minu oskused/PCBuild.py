class PCBuild:
    def __init__(self, build_name):
        self.build_name = build_name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def total_cost(self):
        total = 0
        for component in self.components:
            total += component.price
        return total

    def display_summary(self):
        print(f"\nBuild: {self.build_name}")
        print("Components:")

        for component in self.components:
            print(component)

        print(f"Total: ${self.total_cost():.2f}")
