import funciones
import conexion_mongo

datos = []
    
while True:
    print("\nBienvenidos al Menú:\n")
    print("1. Ingresar datos (Aleatorios o Manual)")
    print("2. Validar datos")
    print("3. Exportar / Importar archivos")
    print("4. Conectar a MongoDB y Consultar por ID")
    print("5. Salir")
    
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        sub = input("Escribe '1' para generar 50 aleatorios o '0' para ingresar manualmente: ")
        if sub == "1":
            datos = funciones.generar_datos()
            print("50 datos generados y ordenados con exito.")
        elif sub == "0":
            nuevos = funciones.ingresar_datos_manuales()
            for n in nuevos:
                datos.append(n)
            print("Se agregaron " + str(len(nuevos)) + " pacientes a la lista.")
        else:
            print("Opcion no valida.")
            
    elif opcion == "2":
        if len(datos) > 0:
            contador = 0
            for d in datos:
                if funciones.validar_registro(d) == True:
                    contador = contador + 1
                else:
                    print("Registro con formato incorrecto: " + str(d))
            print("Se validaron " + str(contador) + " de " + str(len(datos)) + " registros.")
        else:
            print("Primero ingresa datos (Opcion 1).")
            
    elif opcion == "3":
        sub = input("Escribe '1' para Exportar (guardar) o '0' para Importar (leer JSON): ")
        if sub == "1":
            if len(datos) > 0:
                funciones.gestionar_archivos(datos)
                print("Archivos exportados y organizados en /data.")
            else:
                print("No hay datos para exportar. Usa la opcion 1 primero.")
        elif sub == "0":
            importados = funciones.importar_json()
            if len(importados) > 0:
                datos = importados
                print("Se importaron " + str(len(datos)) + " registros desde el JSON.")
        else:
            print("Opcion no valida.")
            
    elif opcion == "4":
        if len(datos) > 0:
            print("Conectando a Mongo... espera un momento.")
            conexion_mongo.interactuar_mongodb(datos)
            print("Listo. Revisa el archivo resultados_mongo.json")
        else:
            print("Primero ingresa o importa datos...")
            
    elif opcion == "5":
        print("Cerrando el sistema, muchas gracias por usarlo")
        break
    else:
        print("Opcion incorrecta.")