import random

class Ruleta:
    __INICIO = 0
    __FINAL = 0
    __AZAR = 0
    
    def __init__(self):
        __INICIO = 0
        __FINAL = 0
        __AZAR = 0       
        
    def setinicio(self, valor):
        self.__INICIO = valor
        
    def setfinal(self, valor):
        self.__FINAL = valor
        
    def getazar(self):
        return self.__AZAR
    
    def verificaring(self):
        salida = "OK"
        if ((self.__FINAL - self.__INICIO) >= 5):
            self.__AZAR = random.randrange(self.__INICIO, self.__FINAL + 1)
        else:
            salida = "los limites ingresados no son correctos..."
        return salida

