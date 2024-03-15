from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas
class Encuesta:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__preguntas = []
        self.__listados_respuestas = []

    def agregar_pregunta(self, preguntas):
        for pregunta in preguntas:
            self.preguntas.append(Pregunta(pregunta["enunciado"],pregunta["ayuda"],pregunta["requerida"]))

    def agregar_listado_respuestas(self, usuario,lista_respuestas):
        self.listados_respuestas.append(ListadoRespuestas(usuario,lista_respuestas))

    def mostrar(self):
        pass

class EncuestaLimitadaPorEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int):
        super().__init__(nombre)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima
    @property
    def edad_minima(self):
        return self.__edad_minima
    @edad_minima.setter
    def edad_minima(self,edad_minima):
        pass
        
    @property
    def edad_maxima(self):
        return self.__edad_maxima
    @edad_maxima.setter
    def edad_maxima(self,edad_maxima):
        pass
    
    def agregar_listado_respuestas(self, usuario,listado_respuestas, edad_usuario):
        pass

class EncuestaLimitadaPorRegion(Encuesta):
    def __init__(self, nombre: str, regiones: list):
        super().__init__(nombre)
        self.__regiones = regiones
        
    @property
    def regiones(self):
        return self.__regiones
    @regiones.setter
    def regiones(self,regiones):
        pass
    
    def agregar_listado_respuestas(self, usuario,listado_respuestas, region_usuario):
        pass