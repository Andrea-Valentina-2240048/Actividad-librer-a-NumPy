import numpy as np

cantidad_estudiantes = 6500

año_de_ingreso = np.random.randint(1960, 2025, size=cantidad_estudiantes ) #randint es random de tipo entero para que no genere error por tipo de dato
codigo_carrera = np.random.randint(10, 50, size=cantidad_estudiantes)
terminacion_codigo = np.random.randint(10, 100, size=cantidad_estudiantes)

codigo_estudiante = (año_de_ingreso*10000) + (codigo_carrera*100) + terminacion_codigo
#print(codigo_estudiante)
nombres = np.array(["Estudiante" + str(i) for i in range(1, cantidad_estudiantes + 1)])  
#print(nombres)
promedios = np.round(np.random.uniform(0, 5.01, size=cantidad_estudiantes), 2)
#print(promedios)
estudiantes = np.column_stack((codigo_estudiante, nombres, promedios)) #Asignación de un código, nombre y promedio a cada estudiante 
#print(estudiantes)

################# Estudiantes con promedio mayor o igual a 4 en la carrera x ####################################
carrera = int(input("Ingrese el código de la carrera que quiere buscar: "))
promedios_float = estudiantes[:, 2].astype(float)
encontrar_estudiantes = (codigo_carrera == carrera) & (promedios_float >= 4)
indices_de_los_estudiantes_que_cumplen = np.where(encontrar_estudiantes)[0]
estudiantes_que_cumplen_las_condiciones = estudiantes[indices_de_los_estudiantes_que_cumplen]

print(f"\nLos estudiantes con promedio mayor o igual a 4 en la carrera {carrera} son:")
for estudiante in estudiantes_que_cumplen_las_condiciones:
    print(f"Código: {estudiante[0]}, Nombre: {estudiante[1]}")

cantidad_estudiantes = np.sum((codigo_carrera == carrera) & (promedios_float >= 4))  # Contar solo los estudiantes que cumplen la condición
print(f"Hay {cantidad_estudiantes} estudiantes con promedio mayor o igual a 4 en la carrera {carrera}")

################# Estudiantes que ingresaron antes de 1990 y están condicionales ##################################
encontrar_estudiantes_condicionales = (año_de_ingreso < 1990) & (promedios < 3 )
indices_de_los_estudiantes_que_estan_condicional = np.where(encontrar_estudiantes_condicionales)[0]
estudiantes_que_cumplen_la_condicion = estudiantes[indices_de_los_estudiantes_que_estan_condicional]

print(f"\nLos estudiantes que ingresaron antes de 1990 y están condicionales son:")
for estudiante in estudiantes_que_cumplen_la_condicion:
    print(f"Código: {estudiante[0]}, Nombre: {estudiante[1]}, Promedio: {float(estudiante[2])}")

cantidad_estudiantes_condicionales = np.sum((año_de_ingreso < 1990) & (promedios < 3 ))  # Contar solo los estudiantes que cumplen la condición
print(f"Hay {cantidad_estudiantes_condicionales} estudiantes que entraron antes de 1990 y estan condicionales")

print(cantidad_estudiantes, cantidad_estudiantes_condicionales)