

def promedio_estudiante(name, nota1, nota2, nota3):
    proNotas=(nota1+nota2+nota3)/3
    return name, proNotas

Cantidad_estudiantes= int(input("Ingrese la cantidad de estudiantes: "))
for i in range(Cantidad_estudiantes):
    def notas_estudiante(): 
        name=  input("Ingrese el nombre del estudiante: ")
        nota1= int(input("Ingrese la primer nota de 0 a 5: "))    
        nota2= int(input("Ingrese la segunda nota de 0 a 5: "))
        nota3= int(input("Ingrese la tercer nota de 0 a 5: "))
        return name,nota1,nota2,nota3
    info_estudiantes=notas_estudiante()
    average=promedio_estudiante(info_estudiantes[0], info_estudiantes[1],info_estudiantes[2],info_estudiantes[3])
    if average [1] >=3: 
        print(f"el estudiante {average[0]} tiene un promedio de {average[1]} y Aprobo, ¡Bien hecho!" )
    elif average [1] < 3:
        print(f"el estudiante {average[0]} obtuvo un promedio de {average [1]} y reprobo, Necesitas estudiar más, tú puedes! ")
