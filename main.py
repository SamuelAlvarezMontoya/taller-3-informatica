import funciones
import conexion_mongo

def main():
    datos = []
    
    while True:
        print("\nBienvenidx al Menú:\n")
        print("1. Generar datos")
        print("2. Validar datos")
        print("3. Guardar archivos (TXT, CSV, JSON)")
        print("4. Conectar a MongoDB y Consultar")
        print("5. Salir")
        
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            datos = funciones.generar_datos()
            print("Datos generados con exito.")
        elif opcion == "2":
            if len(datos) > 0:
                contador = 0
                for d in datos:
                    if funciones.validar_registro(d) == True:
                        contador = contador + 1
                print("Se validaron " + str(contador) + " registros.")
            else:
                print("Primero elige la opcion 1...")
        elif opcion == "3":
            if len(datos) > 0:
                funciones.gestionar_archivos(datos)
                print("Archivos organizados.")
            else:
                print("Primero elige la opcion 1...")
        elif opcion == "4":
            if len(datos) > 0:
                print("Conectando a Mongo... espera un momento.")
                conexion_mongo.interactuar_mongodb(datos)
                print("Listo. Revisa el archivo resultados_mongo.json")
            else:
                print("Primero elige la opcion 1...")
        elif opcion == "5":
            print("Adios!")
            break
        else:
            print("Opcion incorrecta...")