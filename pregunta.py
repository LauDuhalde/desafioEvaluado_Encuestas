from alternativa import Alternativa
class Pregunta:
    def __init__(self, enunciado: str, ayuda: str = None, requerida: bool = False):
        self.enunciado = enunciado
        self.requerida = requerida
        self.ayuda = ayuda
        self.__alternativas = []

    def agregar_alternativas(self, alternativas):
        for alternativa in alternativas:
            self.alternativas.append(Alternativa(alternativa["contenido"],alternativa["ayuda"]))

    def mostrar(self):
        pass
