materias = ["Matematicas","Fisica","Quimica","Biologia", "Geografia", "Literales"]
materias.append("Ingles")
materias.insert(2, "Educacion Fisica")
print(materias[2])

docente = ("Juan Perez", "Fulanito Pérez", "perecila Sanchez")
print(docente[0])

conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.add(6)
print(conjunto)

alumno = {"nombre": "Carlos", "edad": 20, "carrera": "Ingenieria"}
print(alumno["nombre"])
print(alumno["edad"])

print(materias)
lista_conjunto = list(conjunto)
conjunto_materias = set(materias)
print(conjunto_materias)