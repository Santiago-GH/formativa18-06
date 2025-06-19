import FuncionesTurismo as ft
import time
import os
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

opción = 0

while opción != 4:
    opción = ft.Menu()
    if opción == 1:
        print("~~~~~~~~Turistas por país~~~~~~~~")
        pais = input("Ingrese pais a buscar: ").lower().strip().title()
        ft.turistas_por_pais(pais)
    elif opción == 2:
        print("~~~~~~~~Turistas por mes~~~~~~~~")
        mes = ft.pedirMES()
        ft.turistas_por_mes(mes)
    elif opción == 3:
        print("~~~~~~~~Eliminar turistas~~~~~~~~")
        ft.eliminar_turista()
    else:
        print("Cerrando programa...")
        for i in range(0,51,5):
            os.system("cls")
            time.sleep(0.1)
            print(f"{i*2}%")
            print(f"{"□"*i}")
        print("Programa finalizado")