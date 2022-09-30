import random
from model.Rutas import Ruta
from model.Vuelo import Vuelo
from model.Pasaje import Pasaje



class Detalles(object):

    def __init__(self, rutas:Ruta,vuelo:Vuelo,pasaje:Pasaje,pas_eco:int,pas_pre:int):
        self.ruta:Ruta=rutas 
        self.vuelo:Vuelo=vuelo
        self.pasaje:Pasaje=pasaje
        pas_eco:int=pas_eco
        pas_pre:int=pas_pre
        
    