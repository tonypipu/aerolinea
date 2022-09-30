class Ruta(object):

    def __init__(self, cod_ruta: str, nombre_ruta: str ,precio_base:float,asiento_economico:float,asiento_premiun:float):
        """
        Constructor de la clase Ruta
        """
        self.cod_ruta: str = cod_ruta
        self.nombre_ruta: str = nombre_ruta
        self.precio_base: float = precio_base
        self.asiento_economico: float = asiento_economico
        self.asiento_premiun: float = asiento_premiun
        
        
    def __repr__(self) -> str:
        """
        Metodo de clase string 
        """
        return self.cod_ruta