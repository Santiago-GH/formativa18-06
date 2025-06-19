turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def Menu():
    print("*** MENU PRINCIPAL ***\n1.- Turistas por país.\n2.- Turista por mes.\n3.- Eliminar turista.\n4.- Salir")
    opcion = 0
    while opcion not in range(1,5):
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion not in range(1,5): print("Opción no disponible")
            else: break
        except: print("Solo de admiten números")
    return opcion

# La opción 1 debe estar implementada en una función llamada turistas_por_pais(pais) que
# recibe como parámetro el nombre del país y debe mostrar por pantalla una lista con los nombres de los turistas que pertenecen a ese país.
def turistas_por_pais(pais):
    for i,k in turistas.items():
        if pais == k[1]:
            print(k[0])
    return turistas

# La opción 2 debe estar implementada en una función llamada turistas_por_mes(mes), la cual
# recibe un mes como parámetro y debe retornar el porcentaje de turistas que visito chile ese
# mes con respecto al total, redondeado a un decimal. El código principal debe ser el encargado
# de mostrar por pantalla el mensaje.
# Es importante notar que el mes ingresado debe ser solo entre 1 y 12, y si no se cumple esto,
# el programa debe solicitar nuevamente el mes hasta que el usuario ingrese un valor dentro
# del rango solicitado. Ponga atención que, para un mes como febrero, solo se ingresa el valor
# 2 y no el 02.
def pedirMES():
    mes = 0
    while mes not in range(1,13):
        try:
            mes = int(input("Ingrese mes a buscar: "))
            if mes not in range(1,13): print("los meses van del 1 al 12")
            else:break
        except: print("Ingresa el número del mes")
    return mes
def turistas_por_mes(mes):
    cont = 0
    for key, value in turistas.items():
        fecha = value[2].split("-")
        fechames = int(fecha[1])
        if mes == fechames:
            cont += 1
            print("se sumó alguien")
        else: print("no vino este mes")
    porcentaje = round((cont/len(turistas)*100),1)
    print(porcentaje)

# La opción 3 debe estar implementada en una función llamada eliminar_turista(), la cual no
# recibe parámetros. La función debe permitir ingresar el nombre de un turista y eliminar ese
# turista siempre y cuando ese nombre exista. La eliminación debe funcionar independiente si
# el nombre que se ingresa está escrito en mayúsculas o minúsculas. Si se elimina un turista, la
# función debe mostrar el mensaje: "Turista eliminado con éxito.", y si no se elimina debe
# mostrar el mensaje: "Turista no encontrado. No se pudo eliminar."
def eliminar_turista():
    nombreslista = []
    nombre = input("Ingresa turista a eliminar: ").lower().strip().title()
    for i,k in turistas.items():
        if nombre == k[0]:
            nombreslista.append(k[0])
    if nombre not in nombreslista: print("Turista no encontrado. No se pudo eliminar.")
    else:
        for key, value in turistas.items():
            if nombre == value[0]:
                del turistas[key]
                print("Turista eliminado con éxito.")
                print(turistas)
    return turistas