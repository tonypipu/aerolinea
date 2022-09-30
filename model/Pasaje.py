import random
class Pasaje(object):

    def __init__(self, ruta:str,min_pasaje_eco:int,max_pasaje_eco:int,min_pasaje_pre:int,max_pasaje_pre:int):
        """
        Constructor de la clase Pasaje
        """
        self.ruta: str = ruta
        self.min_pasaje_eco: int = min_pasaje_eco
        self.max_pasaje_eco: int = max_pasaje_eco
        self.min_pasaje_pre: int = min_pasaje_pre
        self.max_pasaje_pre: int = max_pasaje_pre
        
        
