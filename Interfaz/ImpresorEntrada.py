from BaseDeDatos.CapaConexion import *

class ImpresorEntrada():
     #atributos de la clase ImpresorEntrada
    entradas = []

    def __init__(self, entradas):
        #constructor del objeto ImpresorEntrada
        self.entradas = entradas


    def imprimirEntradasGeneradas(entras_emitidas):
        #imprime las entradas en formato consola
        print(entras_emitidas)