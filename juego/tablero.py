import random

from juego.linkedlist import LinkedList


class Tablero:
    def __init__(self, tamano):
        self.tamano: int = tamano
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        tablero = LinkedList()

        for i in range(self.tamano):
            fila = LinkedList()
            for j in range(self.tamano):
                fila.add_head(None)
            tablero.add_head(fila)
        return tablero

    def mostrar_tablero(self):
        fila = self.tablero.head
        while fila:
            col = fila.value.head
            fila_mostrar = ''
            while col:
                fila_mostrar += col.value
                col = col.next
            print(fila_mostrar)
            fila = fila.next

    def celdas(self):
        celdas = '🔳'

        fila = self.tablero.head
        while fila:
            col = fila.value.head
            while col:
                if col.value is None:
                    col.value = celdas
                col = col.next
            fila = fila.next

    def cambiar_casilla(self, fila, col, valor):
        nodo_fila = self.tablero.head

        for i in range(fila):
            nodo_fila = nodo_fila.next

        current = nodo_fila.value.head
        for i in range(col):
            current = current.next

        current.value = valor

    def obtener_posicion(self, fila, col):
        nodo_fila = self.tablero.head

        for i in range(fila):
            nodo_fila = nodo_fila.next

        current = nodo_fila.value.head
        for i in range(col):
            current = current.next

        return current.value

    def verificar_posicion(self, fila: int, col: int):
        validacion: bool = 0 <= fila < self.tamano and 0 <= col < self.tamano

        return validacion

    def posicion_inicial_x(self):
        fila = self.tamano - 1
        col = (self.tamano // 2)

        self.cambiar_casilla(fila, col, '🤖')
        return fila, col

    def posicion_inicial_y(self):
        fila = 0
        col = (self.tamano // 2)

        self.cambiar_casilla(fila, col, '👽')
        return fila, col

    def asignar_por_nivel_de_dificultad(self, valor_dificultad):

        valor_dificultad = int(valor_dificultad)

        if valor_dificultad < 25:
            sumas = ['➕'] * int((self.tamano ** 2) // 2)
            restas = ['➖'] * int((self.tamano ** 2) // 2)
            self.asignacion(sumas, restas)

        if 26 <= valor_dificultad >= 50:
            sumas = ['➕'] * int((self.tamano ** 2) // 2.5)
            restas = ['➖'] * int((self.tamano ** 2) // 2.5)
            self.asignacion(sumas, restas)

        if 51 <= valor_dificultad >= 75:
            sumas = ['➕'] * int((self.tamano ** 2) // 3.5)
            restas = ['➖'] * int((self.tamano ** 2) // 3.5)
            self.asignacion(restas, sumas)

        if 76 <= valor_dificultad >= 100:
            sumas = ['➕'] * int((self.tamano ** 2) // 5)
            restas = ['➖'] * int((self.tamano ** 2) // 5)
            self.asignacion(restas, sumas)

    def asignacion(self, sumas: list, restas: list):

        while sumas:
            fila = random.randint(0, self.tamano - 1)
            col = random.randint(0, self.tamano - 1)

            if self.verificar_posicion(fila, col):
                if self.obtener_posicion(fila, col) == '🤖' or '👽' or '➖':
                    self.cambiar_casilla(fila, col, sumas.pop())

            while restas:
                fila = random.randint(0, self.tamano - 1)
                col = random.randint(0, self.tamano - 1)

                if self.verificar_posicion(fila, col):
                    if self.obtener_posicion(fila, col) != '🤖' or '👽' or '➕':
                        self.cambiar_casilla(fila, col, restas.pop())
        return


