#importacion de modulos
from typing import List, Dict
from model.Rutas import Ruta
from model.Pasaje import Pasaje
from model.Vuelo import Vuelo
from util import debug
import pandas as pd
import numpy as np
import time
import random
import math


def create_list_rutas() -> List[Ruta]:
    """
    Función que crea y devuelve una lista de objetos Rutas
    """

    data_rutas: List[Dict[str, str or float or int]] = [
        {"cod_ruta": "LIM - AYA",
            "nombre_ruta": "Lima - Ayacucho", "precio_base": 55.19, "asiento_economico": 8.00, "asiento_premiun": 16.00},
        {"cod_ruta": "LIM - CUS",
            "nombre_ruta": "Lima - Cusco", "precio_base": 136.51, "asiento_economico": 8.00, "asiento_premiun": 16.00},
        {"cod_ruta": "LIM - ARE",
            "nombre_ruta": "Lima - Arequipa", "precio_base": 90.59, "asiento_economico": 8.00, "asiento_premiun": 16.00},
        {"cod_ruta": "LIM - TAR",
            "nombre_ruta": "Lima - Tarapoto", "precio_base": 71.89, "asiento_economico": 8.00, "asiento_premiun": 16.00},
        {"cod_ruta": "AYA - LIM",
            "nombre_ruta": "Ayacucho - Lima", "precio_base": 40.42, "asiento_economico": 7.00, "asiento_premiun": 16.00},
        {"cod_ruta": "CUS - LIM",
            "nombre_ruta": "Cusco - Lima", "precio_base": 124.32, "asiento_economico": 7.00, "asiento_premiun": 16.00},
        {"cod_ruta": "ARE - LIM",
            "nombre_ruta": "Arequipa - Lima", "precio_base": 86.59, "asiento_economico": 7.00, "asiento_premiun": 16.00},
        {"cod_ruta": "TAR - LIM",
            "nombre_ruta": "Tarapoto - Lima", "precio_base": 68.42, "asiento_economico": 7.00, "asiento_premiun": 16.00}
    ]

    # Creamos la lista de objetos Ruta
    rutas: List[Ruta] = []

    for key, ruta in enumerate(data_rutas):

        # Creamos el objeto Ruta
        obj_ruta = Ruta(str(ruta['cod_ruta']), str(ruta['nombre_ruta']), float(
            ruta['precio_base']), float(ruta['asiento_economico']), float(ruta['asiento_premiun']))
        rutas.append(obj_ruta)

    return rutas


def create_list_pasajes() -> List[Pasaje]:
    """
    Función que crea y devuelve una lista de objetos pasaje
    """
    data_pasajes: List[Dict[str, str or int or float]] = [
        {
            "ruta": "LIMA - AYACUCHO",
            "min_eco": 120,
            "max_eco": 130,
            "min_pre": 10,
            "max_pre": 20
        },
        {
            "ruta": "LIMA - CUSCO",
            "min_eco": 130,
            "max_eco": 144,
            "min_pre": 15,
            "max_pre": 24
        },

        {
            "ruta": "LIMA - AREQUIPA",
            "min_eco": 115,
            "max_eco": 138,
            "min_pre": 16,
            "max_pre": 22
        },
        {
            "ruta": "LIMA - TARAPOTO",
            "min_eco": 100,
            "max_eco": 120,
            "min_pre": 12,
            "max_pre": 18
        },
        {
            "ruta": "AYACUCHO - LIMA",
            "min_eco": 100,
            "max_eco": 115,
            "min_pre": 10,
            "max_pre": 15
        },
        {
            "ruta": "CUSCO - LIMA",
            "min_eco": 105,
            "max_eco": 120,
            "min_pre": 14,
            "max_pre": 20
        },
        {
            "ruta": "AREQUIPA - LIMA",
            "min_eco": 100,
            "max_eco": 110,
            "min_pre": 13,
            "max_pre": 18
        },
        {
            "ruta": "TARAPOTO - LIMA",
            "min_eco": 90,
            "max_eco": 105,
            "min_pre": 10,
            "max_pre": 15
        }

    ]

    # Lista de objetos Pasaje
    pasajes: List[Pasaje] = []

    # Iteramos la lista de Pasajes.
    for key, pasaje in enumerate(data_pasajes):
        # Creamos el objeto Pasaes
        obj_pasaje = Pasaje(str(pasaje['ruta']), int(pasaje['min_eco']), int(
            pasaje['max_eco']), int(pasaje['min_pre']), float(pasaje['max_pre']))
        pasajes.append(obj_pasaje)
    
    return pasajes



def create_list_vuelos() -> List[Vuelo]:
    """
    Función que crea y devuelve una lista de objetos Vuelo
    """

    data_vuelos: List[Dict[str, str or float or int]] = [
        {"ruta": "LIMA - AYACUCHO", "avion": "A001",
            "salida": "06:30 AM"},
        {"ruta": "LIMA - CUSCO", "avion": "A002",
            "salida": "07:25 AM"},
        {"ruta": "LIMA - AREQUIPA", "avion": "A003",
            "salida": "08:10 AM"},
        {"ruta": "LIMA - TARAPOTO", "avion": "A004",
            "salida": "08:50 AM"},
        {"ruta": "AYACUCHO - LIMA", "avion": "A001",
            "salida": "15:45 PM"},
        {"ruta": "CUSCO - LIMA", "avion": "A002",
            "salida": "16:25 PM"},
        {"ruta": "AREQUIPA - LIMA", "avion": "A003",
            "salida": "17:15 PM"},
        {"ruta": "TARAPOTO - LIMA", "avion": "A004",
            "salida": "17:50 PM"},
    ]

    # Creamos la lista de objetos Vuelos
    vuelos: List[Vuelo] = []

    for key, ruta in enumerate(data_vuelos):

        # Creamos el objeto Product
        obj_vuelo = Vuelo(str(ruta['ruta']), str(ruta['avion']), str(
            ruta['salida']))
        vuelos.append(obj_vuelo)

    return vuelos




def main():
    """
    Función principal del módulo app.py
    """
    # Creamos las listas de objetos 
   
    rutas: List[Ruta] = create_list_rutas()
    vuelos: List[Vuelo] = create_list_vuelos()
    pasajes: List[Pasaje] = create_list_pasajes()

    #Crear listas para el data frame
    lrutas=list()
    lvuelos=list()
    lsalida=list()
    lpasaje_eco=list()
    lpasaje_pre=list()
    lpre_base=list()
    lasi_eco=list()
    lasi_pre=list()
    
    #creacion de dataframe a utilizar
    dfreporte = pd.DataFrame()
    dforden=pd.DataFrame()
    dforden_max_min=pd.DataFrame()
    dfavion_temp=pd.DataFrame()
    dfavion=pd.DataFrame()
    
   
    print("REPORTE DE VUELOS")
    print("*"*30)
    print("\n")


    for key, vuelo in enumerate(vuelos):
        lvuelos.append(vuelo.avion)
        lsalida.append(vuelo.salida)
        
    for key, ruta in enumerate(rutas):
       
        lrutas.append(ruta.nombre_ruta)
        lpre_base.append(ruta.precio_base)
        lasi_eco.append(ruta.asiento_economico)
        lasi_pre.append(ruta.asiento_premiun)
        
        
    for key, pasaje in enumerate(pasajes):    
        total_asientos_eco=random.randint(pasaje.min_pasaje_eco,pasaje.max_pasaje_eco)
        total_asientos_pre=random.randint(pasaje.min_pasaje_pre,pasaje.max_pasaje_pre)
        lpasaje_eco.append(total_asientos_eco)
        lpasaje_pre.append(total_asientos_pre)
        
      
   
        
   #manipulacion de datos dataframe
    dfreporte['Rutas']=lrutas
    dfreporte['Avion']=lvuelos
    dfreporte['Salida']=lsalida
    dfreporte['Pasajes_Economicos']=lpasaje_eco
    dfreporte['Pasajes_Premiun']=lpasaje_pre
    col_sumar=['Pasajes_Economicos','Pasajes_Premiun']
    dfreporte['Total_asientos']=dfreporte.loc[:,col_sumar].sum(axis=1)
    dfreporte['Precio_base']=lpre_base
    dfreporte['Asientos_Eco']=lasi_eco
    dfreporte['Asientos_Pre']=lasi_pre
   
    dfreporte['IGV_Eco']=(((dfreporte['Precio_base'] + dfreporte['Asientos_Eco'])*18)/100)
    dfreporte['IGV_Pre']=(((dfreporte['Precio_base'] + dfreporte['Asientos_Pre'])*18)/100)
    dfreporte['Venta_eco']=dfreporte['IGV_Eco']+(dfreporte['Precio_base'] + dfreporte['Asientos_Eco'])
    dfreporte['Venta_pre']=dfreporte['IGV_Pre']+(dfreporte['Precio_base'] + dfreporte['Asientos_Pre'])
    dfreporte['Venta_Total']=dfreporte['Venta_eco'] + dfreporte['Venta_pre']
    
    
    #variables de almacenamiento de totales
    tol_asientos=dfreporte['Total_asientos'].sum()
    tol_ingresos_eco=dfreporte['Venta_eco'].sum()
    tot_ingresos_pre=dfreporte['Venta_pre'].sum()
    tol_igv=(dfreporte['IGV_Eco'].sum())+(dfreporte['IGV_Pre'].sum())
    val_prom_eco=dfreporte['Pasajes_Economicos'].mean()
    val_prom_pre=dfreporte['Pasajes_Premiun'].mean()
    vue_id_max=dfreporte['Total_asientos'].idxmax()
    vue_id_min=dfreporte['Total_asientos'].idxmin()
    vue_max_pasajero=dfreporte.iloc[vue_id_max,0]
    vue_min_pasajero=dfreporte.iloc[vue_id_min,0]
    
    #obtenemos las 3 mayores rutas
    dforden['Rutas']=dfreporte['Rutas']
    dforden['Venta_Total']=dfreporte['Venta_Total']
    dforden=dforden.sort_values(by='Venta_Total', ascending=False)
    dforden_max_min['Mayores_Rutas']=dforden["Rutas"].iloc[0:3]
    print(dfreporte)
    
    #obtenemos el avion con mayor pasajeros
    dfavion_temp['Avion']=dfreporte['Avion']
    dfavion_temp['Total_asientos']=dfreporte['Total_asientos'] 
    n_aviones=list()
    nom_aviones=list()
    for i in range(1,5):
        avion1=dfavion_temp.loc[dfavion_temp['Avion'] == f'A00{i}', 'Total_asientos'].sum()
        nom_aviones.append(f'A00{i}')
        n_aviones.append(avion1)
    dfavion['Avion']=nom_aviones
    dfavion['Avion_cantidad_max']=n_aviones
    max_avion=dfavion['Avion_cantidad_max'].idxmax()
    
    dfavion_completo = pd.DataFrame()
    nom_avion=dfavion.iloc[max_avion,0]
    
    
    
    
    
    #creamos dataframe que almacene los totales (preguntas)
    datos = {
    'Total_asientos' : [tol_asientos],
    'Total_Ingresos_VPC' : [tol_ingresos_eco],
    'Total_Ingresos_VPP' : [tot_ingresos_pre],
    'Total_Importe_IGV' : [tol_igv],
    'Valor_Promedio_pasaje_eco' : [val_prom_eco],
    'Valor_Promedio_pasaje_pre' : [val_prom_pre],
    'Vue_max_cant_pasajero' : [vue_max_pasajero],
    'Vue_min_cant_pasajero' : [vue_min_pasajero],
    'Avion_cantidad_max':[nom_avion]
    
    
    }
    
    dfrep_detalle = pd.DataFrame(datos)
    print("REPORTE DETALLES")
    print("*"*30)
    print("\n")
    
    print(dfrep_detalle)
       
    print("REPORTE DETALLES 3 MAYORES")
    print("*"*30)
    print("\n")

    print(dforden_max_min)
    
    
    
    #crear reporte en excel por hojas
    try:
        writer = pd.ExcelWriter('reportecompleto'+time.strftime('%d-%m-%Y')+'.xlsx', engine='xlsxwriter')   
        dfreporte.to_excel(writer, sheet_name='Reporte')
        dfrep_detalle.to_excel(writer, sheet_name='Preguntas')
        dforden_max_min.to_excel(writer, sheet_name='Ultima_pregunta') 
        debug.logger.info('Se realizo de forma correcta la creacion de excel reporte')   
        writer.save()
    except NameError:
        debug.logger.error('A ocurrido un error:',NameError)
        
        
if __name__ == "__main__":
    main()
