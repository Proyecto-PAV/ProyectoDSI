from BaseDeDatos.CapaConexion import *

class ImpresorEntrada():
     #atributos de la clase ImpresorEntrada
    entradas = []

    def __init__(self, entradas):
        #constructor del objeto ImpresorEntrada
        self.entradas = entradas


    def imprimirEntradasGeneradas(entras_emitidas):
        if len(entras_emitidas) > 0:
            return True
        else:
            return False