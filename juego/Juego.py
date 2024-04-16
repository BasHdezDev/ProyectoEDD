import random

from juego.tablero import Tablero


class Juego:
    def __init__(self, tablero: Tablero):
        self.tablero = tablero
        self.pos_x = None
        self.vida_x = 50
        self.pos_y = None
        self.vida_y = 50

    def iniciar_x(self):
        self.pos_x = self.tablero.posicion_inicial_x()

    def iniciar_y(self):
        self.pos_y = self.tablero.posicion_inicial_y()

    def movimiento_x(self):
        direccion = input("Movimiento:\n1: Arriba\n2: Abajo\n3: Izquierda\n4: Derecha\n->  ")

        nueva_fila, nueva_col = self.pos_x

        if direccion == "1":
            nueva_fila -= 1  # Para abajo
        elif direccion == "2":
            nueva_fila += 1  # Para arriba
        elif direccion == "3":
            nueva_col -= 1   # Para la izq
        elif direccion == "4":
            nueva_col += 1   # Para la der
        else:
            print('Ingrese 1, 2, 3 o 4')
            return

        if self.tablero.verificar_posicion(nueva_fila, nueva_col):
            node_value = self.tablero.obtener_posicion(nueva_fila, nueva_col)

            if node_value == '➕':
                self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                self.tablero.cambiar_casilla(nueva_fila, nueva_col, '🤖')
                if self.vida_x < 50:
                    self.vida_x += 10
                self.pos_x = (nueva_fila, nueva_col)
                return

            if node_value == '➖':
                self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                self.tablero.cambiar_casilla(nueva_fila, nueva_col, '🤖')
                if self.vida_x > 0:
                    self.vida_x -= 10
                self.pos_x = (nueva_fila, nueva_col)
                return

            if node_value == '👽':
                pass

            else:
                self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                self.tablero.cambiar_casilla(nueva_fila, nueva_col, '🤖')
            self.pos_x = (nueva_fila, nueva_col)
            return

        else:
            print("No puedes hacer ese movimiento")
            return

    def movimiento_y(self):

        direccion = str(random.randint(1, 4))
        nueva_fila, nueva_col = self.pos_y

        if direccion == "1":
            nueva_fila -= 1     #Arriba
        elif direccion == "2":
            nueva_fila += 1     #Abajo
        elif direccion == "3":
            nueva_col -= 1      #Izquierda
        elif direccion == "4":
            nueva_col += 1      #Derecha
        else:
            return

        if self.tablero.verificar_posicion(nueva_fila, nueva_col):
            node_value = self.tablero.obtener_posicion(nueva_fila, nueva_col)

            if node_value == '➕':
                self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                self.tablero.cambiar_casilla(nueva_fila, nueva_col, '👽')
                if self.vida_y < 50:
                    self.vida_y += 10
                self.pos_y = (nueva_fila, nueva_col)
                return

            if node_value == '➖':
                self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                self.tablero.cambiar_casilla(nueva_fila, nueva_col, '👽')
                if self.vida_y > 0:
                    self.vida_y -= 10
                self.pos_y = (nueva_fila, nueva_col)
                return

            if node_value == '🤖':
                pass

            else:
                self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                self.tablero.cambiar_casilla(nueva_fila, nueva_col, '👽')

                self.pos_y = (nueva_fila, nueva_col)
                return
        else:
            return

    def verificar_ganador(self):

        if self.vida_y <= 0:
            print(f"La vida del alien es {self.vida_y}.\n")

            return "\n!!!!!!!!!!!!!!!!El jugador X gana!!!!!!!!!!!!!!!"
        if self.vida_x <= 0:

            print(f"Tú vida es {self.vida_x}.\n")

            return "\nLa maquina gana :("
        else:
            return None


def menu_crear_tablero():
    while True:
        tamano_tablero = int(input("\nIngresa el tamaño del tablero\n-> "))
        print("")

        if tamano_tablero < 3:
            print("El tablero debe ser minimo de 3x3")
            continue
        tablero = Tablero(tamano_tablero)
        juego = Juego(tablero)
        menu_inicio(tablero, juego)


def menu_inicio(tablero, juego):
    while True:
        opcion = input("Menú del juego\n1. Iniciar\n2. Salir\n-> ")
        print("\n Iniciando el juego \n")
        if opcion == "1":

            dificultad = int(input("\nIngresa la dificultad (De 1 a 100)\n"
                                   "Siendo 100 la más díficil y 1 la más fácil \n->"))

            tablero.celdas()
            tablero.asignar_por_nivel_de_dificultad(dificultad)
            juego.iniciar_x()
            juego.iniciar_y()
            menu_turnos(tablero, juego)
            break

        elif opcion == "2":
            break

        else:
            print('Opción invalida, ingrese 1 o 2')
            continue


def menu_turnos(tablero, juego):
    while True:
        tablero.mostrar_tablero()
        print(f"Tú - {juego.vida_x} <-------> {juego.vida_y} - Alien")

        print("\nTurno del jugador X\n")
        opcion_x = input("1. Moverse\n2. Atacar\n-> ")
        if opcion_x == "1":
            juego.movimiento_x()
        elif opcion_x == "2":
            continue
        else:
            print("Ingrese 1 o 2")
            continue

        ganador = juego.verificar_ganador()
        if ganador:
            print(ganador)
            quit()

        print("\nTurno de la maquina\n")

        opcion_y = str(random.randint(1, 2))
        if opcion_y == "1":
            juego.movimiento_y()
        if opcion_y == "2":
            #if verificar_ataque:
                #atacar
            #else:
            juego.movimiento_y()

        menu_turnos(tablero, juego)

menu_crear_tablero()
