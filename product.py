class Product:
    def __init__(self, product_id, name, premium):
        self.product_id = product_id
        self.name = name
        self.premium = premium
        self.active = True

    def update_premium(self, new_premium):
        self.premium = new_premium
        return f"Premium updated to ${new_premium}."

    def suspend_product(self):
        self.active = False
        return f"Product {self.name} suspended."

    def __str__(self):
        return f"Product: {self.name}, Premium: ${self.premium}, Active: {self.active}"