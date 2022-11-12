class Auto():
    def __init__(self, model, color, engine_volume):
        self.model = model
        self.color = color
        self.engine_volume = engine_volume
    @staticmethod
    def forvard():
        print("move forvard")
    @staticmethod
    def backwards():
        print("move backvards")
car1 = Auto("Citroen", "maroon", 1.6)
car1.forvard()
car1.backwards()

class Auto2(Auto):
    @staticmethod
    def turn_left():
        print("turn left")
    @staticmethod
    def turn_right():
        print("turn right")