def ingresar_datos (): 
    
    escribir = open('alumno.txt' , 'a' )
    cant= int(input("De cuantos alumnos quiere registar datos: "))
    for i in range(cant):
        notafinal = 0
        notas=[]
        nombre = input(f'Ingrese el nombre del estudiante {i+1}: ')
        nombre=nombre.title()
        apellido = input(f'Ahora ingrese su apellido: ')
        apellido=apellido.title()
        dni = int(input("Ahora su DNI: "))
        for x in range(6):
            tp = int(input(f'Ingrese la nota {x+1} '))
            notas.append(tp)
        
        notafinal= sum(notas)/6
        
        escribir.write(f'\n{nombre};{apellido};{dni};{notas};{notafinal}')
    
    escribir.close()
    
def mostrar(): 
    muestra = open('alumno.txt' , 'r')
    _=muestra.readline()
    
    print(f'\nLos alumnos que se encuentran en la lista son los siguientes:')
    
    for i in muestra.readlines():
        muestra_separados = i.split(";")

        print(muestra_separados[0] , muestra_separados[1])

    muestra.close()


def aprob_desaprob (): 
    muestra = open('alumno.txt' , 'r')
    _=muestra.readline()
    
    for i in muestra.readlines():
        elemento=0
        muestra_separados = i.split(";")

        elemento = muestra_separados[4]

        entero=float(elemento)

        if entero >= 6.0 :
            print(f'El alumno {muestra_separados[0], muestra_separados[1]} está aprobado con {muestra_separados[4]}')

        else:
            print(f'El alumno {muestra_separados[0], muestra_separados[1]} está desaprobado con {muestra_separados[4]}')

    muestra.close()



while True: 
    print("\nMENU DE OPCIONES")
    print("1. Ingresar estudiantes y notas de los trabajos practicos")
    print("2. Mostrar lista de los alumnos")
    print("3. Mostrar estudiantes aprobados y desaprobados")
    print("4. Salir")

    opc=input("Elija una opcion: ")

    if opc == "1":
        ingresar_datos()
    
    elif opc == "2":
        mostrar()
    
    elif opc == "3":
        aprob_desaprob()
    
    elif opc == "4":
        print("Gracias por visitar el programa")
        break
    else:
        print("Ingrese una opcion válida por favor")
