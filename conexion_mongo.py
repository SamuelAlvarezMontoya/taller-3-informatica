import json
from pymongo import MongoClient
import funciones

def interactuar_mongodb(datos):
    
    uri = "mongodb+srv://samuelalvarezm_db_user:T9aUaR5Lp3Ygo820@cluster0.fqzfg54.mongodb.net/" 
    try:
        cliente = MongoClient(uri)
        db = cliente["taller3"]
        coleccion = db["signos_vitales"]
        
        #Se guardan solamente los datos que pasen la validacion
        datos_validos = []
        for d in datos:
            if funciones.validar_registro(d) == True:
                datos_validos.append(d)
                
        if len(datos_validos) > 0:
            coleccion.delete_many({}) # Limpiar datos viejos
            coleccion.insert_many(datos_validos)
            
        #Calcular promedio de Frecuencia Cardiaca
        suma_fc = 0
        for d in datos_validos:
            numero_limpio = d["fc"].replace("ppm", "")
            suma_fc = suma_fc + int(numero_limpio)
            
        if len(datos_validos) > 0:
            promedio = suma_fc / len(datos_validos)
        else:
            promedio = 0
            
        #Buscar pacientes con oxigeno menor a 94
        bajos_oxigeno = []
        for d in datos_validos:
            numero_spo2 = d["spo2"].replace("%", "")
            if int(numero_spo2) < 94:
                bajos_oxigeno.append(d)

        #Se pide el ID y lo busca en la base de datos
        id_buscar = input("Escribe el ID a buscar (ejemplo ID-001) o presiona Enter para saltar: ")
        paciente_encontrado = None
        if id_buscar != "":
            paciente_encontrado = coleccion.find_one({"id": id_buscar}, {"_id": 0})
            if paciente_encontrado != None:
                print("Paciente encontrado: " + str(paciente_encontrado))
            else:
                print("No se encontro ningun paciente con ese ID.")
        
        #Exportar resultado
        resultados = {
            "promedio_frecuencia_cardiaca": promedio,
            "pacientes_peligro_oxigeno": bajos_oxigeno,
            "paciente_consultado": paciente_encontrado
        }
        
        archivo_res = open("resultados_mongo.json", "w", encoding="utf-8")
        json.dump(resultados, archivo_res, indent=4)
        archivo_res.close()
            
        funciones.escribir_log("Conexion a Mongo exitosa y consultas realizadas")
    except Exception as error:
        funciones.escribir_log("Error de MongoDB: " + str(error))