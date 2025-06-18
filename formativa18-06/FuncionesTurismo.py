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
def turistas_por_pais(pais,diccionario):
    for i,k in diccionario.items():
        if pais == k[1]:
            print(k[0])
    return diccionario

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
def turistas_por_mes(mes,diccionario):
    cont = 0
    for key, value in diccionario.items():
        fecha = value[2].split("-")
        fechames = int(fecha[1])
        if mes == fechames:
            cont += 1
            print("se sumó alguien")
        else: print("no vino este mes")
    porcentaje = round((cont/len(diccionario)*100),1)
    print(porcentaje)