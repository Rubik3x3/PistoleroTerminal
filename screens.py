import os
import pyrebase
import random

letters="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers="0123456789"

codePartida = ""

firebaseConfig = {
  "apiKey": "AIzaSyBUTPEMIxKKFYj2HZTMUbb24ETUtRzxA_U",
  "authDomain": "pistoleroterminal.firebaseapp.com",
  'databaseURL': "https://pistoleroterminal-default-rtdb.firebaseio.com/",
  "projectId": "pistoleroterminal",
  "storageBucket": "pistoleroterminal.appspot.com",
  "messagingSenderId": "299109486587",
  "appId": "1:299109486587:web:dd97fc192dffef4043455e"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title():
    print(" _____   _       _           _ \n|  __ \ (_)     | |         | | \n| |__) | _  ___ | |_   ___  | |  ___  _ __   ___ \n|  ___/ | |/ __|| __| / _ \ | | / _ \| '__| / _ \ \n| |     | |\__ \| |_ | (_) || ||  __/| |   | (_) | \n|_|     |_||___/ \__| \___/ |_| \___||_|    \___/ \n")
    print(f'{"<"*8} Desarrollado por Franco Talarico {">"*8}\n')

def mainMenu():
    clear()
    title()
    print(f'{" -"*11}- MENÚ -{"- "*11}')
    print("[1] Crear partida")
    print("[2] Unirse a una partida")
    print("[3] Salir")
    opcMenu = int(input("\nOpcion: "))

    if opcMenu == 1:
        crearPartida()
    elif opcMenu == 2:
        unirsePartida()
    elif opcMenu == 3:
        exit()
    else:
        exit()

def partida():
    print(f'{" -"*10}- PARTIDA -{"- "*11}')

def jugadores():
    
    print("Jugadores: ",)

def codigoPartida():
    global codePartida,db
    data ={"players": 1, "turno": 1, "b1":0, "b2": 0,"ronda": 1, "opc": 0}
    db.child(codePartida).set(data)
    print("Código de la partida: ",codePartida)

def crearPartida():
    global codePartida
    clear()
    title()
    partida()
    code = random.sample(letters+numbers,4)
    code = "".join(code)
    codePartida = code
    codigoPartida()

def unirsePartida():
    clear()
    title()
    codigo = str(input("Ingrese el código de la partida: "))
    
def my_handler(sender, value=None):
    print(value)

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child(codePartida).stream(stream_handler)