import numpy as np

candidatos = np.arange(1,31) #número de candidatos
#print(candidatos)
votos = np.random.choice(candidatos, size=5000, replace=True) #Selecciona 5000 elementos del array aleatorios, permitiéndosen repeticiones 
#print(votos)
resultados = np.bincount(votos, minlength=31)[1:] #Cuenta cuantas veces se repite el numero de candidatos en los votos
#print(resultados)
ordenado = np.argsort(-resultados)
#print(ordenado_desc)  # Ordenamiento de los dator de mayor a menor

for i in ordenado:
    print(f"El candidato {i+1} recibió: {resultados[i]} votos")




