import random
import os
import csv
import json
import shutil
from datetime import datetime

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

def escribir_log(mensaje):
    archivo_log = open("log.txt", "a")
    archivo_log.write(str(datetime.now()) + " - " + mensaje + "\n")
    archivo_log.close()

def gestionar_archivos(datos):
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/txt"):
        os.makedirs("data/txt")
    if not os.path.exists("data/csv"):
        os.makedirs("data/csv")
    if not os.path.exists("data/json"):
        os.makedirs("data/json")
    
    try:

        archivo_txt = open("datos.txt", "w", encoding="utf-8")
        for d in datos:
            linea = d['id'] + ", " + d['fr'] + ", " + d['fc'] + ", " + d['spo2'] + "\n"
            archivo_txt.write(linea)
        archivo_txt.close()
        shutil.move("datos.txt", "data/txt/datos.txt")
        
        #Archivo CSV
        archivo_csv = open("datos.csv", "w", newline='', encoding="utf-8")
        escritor = csv.DictWriter(archivo_csv, fieldnames=["id", "fr", "fc", "spo2"])
        escritor.writeheader()
        for d in datos:
            escritor.writerow(d)
        archivo_csv.close()
        shutil.move("datos.csv", "data/csv/datos.csv")
        
        #Archivo json
        archivo_json = open("datos.json", "w", encoding="utf-8")
        json.dump(datos, archivo_json, indent=4)
        archivo_json.close()
        shutil.move("datos.json", "data/json/datos.json")
        
        escribir_log("Archivos guardados en sus carpetas")
    except Exception as error:
        escribir_log("Error al crear archivos: " + str(error))

def ingresar_datos_manuales():
    lista_manual = []
    cantidad = int(input("\n¿Cuantos pacientes quieres ingresar?: "))
    
    for i in range(cantidad):
        print("\nPaciente " + str(i + 1) + ":")
        nuevo_id = input("Ingresa el ID (ejemplo ID-051): ")
        nueva_edad = input("Ingresa la edad (ejemplo 25 Años): ")
        nueva_fc = input("Ingresa la frecuencia cardiaca (ejemplo 085ppm): ")
        nuevo_spo2 = input("Ingresa el SpO2 (ejemplo 97%): ")
        
        registro = {
            "id": nuevo_id,
            "fr": nueva_edad,
            "fc": nueva_fc,
            "spo2": nuevo_spo2
        }
        lista_manual.append(registro)
        
    return lista_manual

def importar_json():
    ruta = "data/json/datos.json"
    if os.path.exists(ruta):
        archivo = open(ruta, "r", encoding="utf-8")
        datos_cargados = json.load(archivo)
        archivo.close()
        escribir_log("Datos importados desde data/json/datos.json")
        return datos_cargados
    else:
        print("Aun no has exportado el archivo JSON.")
        return []