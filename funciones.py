import random
import os
import csv
import json
import shutil
from datetime import datetime
from pymongo import MongoClient

def generar_datos():
    datos = []

    for i in range(1, 51):
        
        if i < 10:
            texto_id = "ID-00" + str(i)
        else:
            texto_id = "ID-0" + str(i)
            
        texto_edad = str(random.randint(18, 80)) + " Años"
        texto_fc = str(random.randint(60, 120)) + "ppm"
        texto_spo2 = str(random.randint(90, 100)) + "%"
        
        registro = {
            "id": texto_id,
            "fr": texto_edad,
            "fc": texto_fc,
            "spo2": texto_spo2
        }
        datos.append(registro)
    
    def obtener_fc(elemento):
        return elemento["fc"]
        
    datos.sort(key=obtener_fc)
    return datos

def validar_registro(registro):
    if not registro["id"].startswith("ID-"):
        return False
    if not " Años" in registro["fr"]:
        return False
    if not "ppm" in registro["fc"]:
        return False
    if not "%" in registro["spo2"]:
        return False
    return True