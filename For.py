# FOR es para listas, tuplas y diccionarios
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

print("- Ejemplo de FOR con listas")
for dia in dias:
    print(dia)

print("- Ejemplo de FOR con BREAK")
for dia in dias:
    print(dia)
    if dia == "Lunes":
        break

print("- Ejemplo de FOR con Excepción")
for dia in dias:
    if dia == "Viernes":
        break
    print(dia)

print("- Ejemplo de FOR con repetición")
for dia in dias:
    print(dia)
else:
    print("Fin del ejemplo")