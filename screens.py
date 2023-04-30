import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title():
    print(" _____   _       _           _ \n|  __ \ (_)     | |         | | \n| |__) | _  ___ | |_   ___  | |  ___  _ __   ___ \n|  ___/ | |/ __|| __| / _ \ | | / _ \| '__| / _ \ \n| |     | |\__ \| |_ | (_) || ||  __/| |   | (_) | \n|_|     |_||___/ \__| \___/ |_| \___||_|    \___/ \n")
    print(f'{"<"*8} Desarrollado por Franco Talarico {">"*8}\n')

def mainMenu():
    print(f'{" -"*11}- MENÚ -{"- "*11}')
    print("[1] Crear partida")
    print("[2] Unirse a una partida")
    print("[3] Salir")
    opcMenu = int(input("\nOpcion: "))