class Product:
    payment = 'Visa'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    