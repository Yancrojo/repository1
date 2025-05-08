#pedir al usuario ingresar una nota númerica entre 0 y 100 
#verificar si los datos ingresados son correctos 
#validar si el estudiante aprobo o reprobo 

note= [] #lista para guardar las notas
Nnote =int(input("Ingresa la cantidad de notas: " )) #Variable para guardar cantidad de notas
datumnote= 0
Tnotas=0
average=0
count=0 

for i in range (Nnote):  
    #ingresar notas
    while True: 
        try: 
            datumnote = input("Ingrese una nota: ")
            if datumnote.isnumeric():
                datumnote=float (datumnote)
                note.append(datumnote)
                if 0 < datumnote <= 40: #verificación de notas si es menor a 40
                    print("La nota fue reprobada: ")
                    break
                elif 40 < datumnote <= 100:
                    print("La nota fue aprobada: ") 
                    break
                else: 
                    print("Nota incorrecta: ")
            else:
                print("El rango de las notas debe ser entre 0 y 100: ")
        except ValueError:
            print("Valor incorrecto: ")
    Tnotas= Tnotas + note[i]
    count= note
    average = (Tnotas) /  (Nnote)

result= input("Ingrese las notas separadas por ',': ")
taverage= result.split("***")
print(taverage) 

print(f"La suma de sus notas es {Tnotas} y su promedio es {average: .2f}   ")
if average > 40: 
            print("La nota es aprobada: ")
            
elif average <= 40: 
            print("No aprobo sus notas:  ")
cont=0
punt=int(input("Elija una nota para validar las veces que se repite: "))
for i in range(Nnote): 
    print(punt)
    print(note)
    if punt == note[i]:
        cont= cont+1 
        

print("Las veces que esta se repite son: ", cont)

cont2=0
valid=int(input("Ingrese un nota para validar cuales son mayores: "))

for i in range(Nnote): 
    if valid < note[i]:
        cont2= cont2+1 
        
print("La cantidad de notas mayores son: ", cont2)
if cont2 == 0 :
    print("No hay notas mayores a la nota ingresada" , cont2)






    



    