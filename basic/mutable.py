class Product:
    payment = ['Visa','Master','American Express']# class variable shared by all instances

    def __init__(self, name):
        self.name = name    