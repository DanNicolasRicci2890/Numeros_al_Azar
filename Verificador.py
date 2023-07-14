from strconfig import *

class verifdata:
    __Value = ""
    
    def __init__(self, num):
        self.__Value = num
        
    def ConfigState(self):
        salida = "OK"
        try:
            if (len(self.__Value) == 0):
                raise ValueError
            elif ((strconfig.IsNumeric(self.__Value)) == False):
                raise TypeError
            elif ((strconfig.IsIntero(self.__Value)) == False):
                raise IndexError
        except ValueError:
            salida = "No se permite datos vacios..."
        except TypeError:
            salida = "No se permite letras, solo numeros..."
        except IndexError:
            salida = "No se permite numeros flotantes..."
        return salida
    
    def getverif(self):
        return self.__Value
    
            