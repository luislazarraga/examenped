class Triangulo:

    def __init__(self, area): #Inicializamos area hasta que el test compile pero falle.
        self.area = area #Bastaría con self.area = pass para que compile y corra.

    '''def base(self, cantidad):
        self.area = cantidad #Bastaría para que pasara el segundo test con poner self.area = 10

    def altura(self, cantidad):
        self.area = 25 '''

    def CalcularArea(self, base, altura):
        self.area = (base * altura)/2