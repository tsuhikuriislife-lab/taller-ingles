# Un juego realista.
import random

lagos = [
    {
        "nombre": "El Lago de los Amantes",
        "peces": {
            "peces comunes": ["Payaso", "Globo", "Mariposa", "Koi"],
            "peces raros": ["Dorado", "Plateado", "Arcoiris", "Angel"],
            "peces extra raros": ["Ponyo", "Marido", "Esposa",]
        }
    },
    {
        "nombre": "Lago Morita",
        "peces": {
            "peces comunes": ["Payaso", "Caballito de Mar", "Disco", "Angel" ],
            "peces raros": ["Tilapia" ],
            "peces extra raros": []
        }
    },
    {
        "nombre": "Lago de los Copitos",
        "peces": {

        }
    }]


print("*"*50)
print("Bienvenido al juego realista.")
print("*"*50)
print("En este juego, podras pescar diferentes tipos de peces, en diferentes lagos.\nSi tienes suerte, puedes encontrar peces raros!!!")
print()

menu = int(input("Por favor selecciona una opcion:\n1.Iniciar el juego\n2.Salir\n+++ "))
if menu == 1:
    print("Por favor elige el lago que deseas visitar:")
    count = 1
    for lago in lagos:
        print(f"---{count}. {lago['nombre']}")
        count += 1
    indice = int(input("+++ "))-1
    lago_actual = lagos[indice]
    print(f"Seleccionaste {lago_actual['nombre']}")
    salir =0
    while salir ==0:
            opciones = input("Que quieres hacer?:\n1.Pescar\n2.Salir\n--- ")
            if opciones == "1":
                salir = 0
                intentos = 0
                while salir == 0:
                    probabilidad = random.randint(1, 100)
                    a = input(f"\nLanzando caña por {intentos} vez...")
                    if probabilidad <= 30:
                        a = input("\nEl anzuelo se rompio :(...")
                        intentos += 1
                    elif probabilidad <= 75:
                        a = input("\nAlgo pico el anzuelo!")
                        pesca = random.choice(lago_actual["peces"]["peces comunes"])
                        peso = random.randint(5, 10)
                        if peso > 9:
                            a = input("\nEs pesado!")
                        a = input(f"\nFelicidades, pescaste un Pez {pesca} de {peso} kilos!")
                        intentos += 1
                    elif probabilidad <= 95:
                        a = input("\nAlgo raro pico el anzuelo!")
                        pesca = random.choice(lago_actual["peces"]["peces raros"])
                        peso = random.randint(20, 35)
                        if peso > 30:
                            a = input("\nEs pesado!")                    
                        a = input(f"\nFelicidades, pescaste un Pez {pesca} de {peso} kilos!")
                        intentos += 1                        
                    else:
                        a = input("\nAlgo extra raro pico el anzuelo!")                    
                        pesca = random.choice(lago_actual["peces"]["peces extra raros"])
                        peso = random.randint(30, 60)
                        if peso > 50:
                            a = input("\nEs pesado!")                    
                        a = input(f"\nFelicidades, pescaste un Pez {pesca} de {peso} kilos!")
                        intentos += 1                        
                    opciones = input("\nQuieres salir? (N): ")
                    if opciones == "N":
                        print("\nHasta la proxima!")
                        salir += 1
            elif opciones == "2":
                print("Gracias por jugar!")
                salir += 1
            else:
                print("\nSelecciona una opcion correcta.")
