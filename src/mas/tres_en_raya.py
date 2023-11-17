import os


#Simbolos que se mostraran en el tablero
FICHAS = (' ','X','O')

def borrarConsola():
    """Limpiar consola"""
    os.system("cls")

def pulse_para_continuar():
    """"Mostrar eel mensaje Presione una tecla para continuar y
    hacer una pausa que se realice con la acccio."""
    os.system("pause")

def crear_fila(num_columnas = 3) -> list:
    """Crerar las columnas de una fila
    :para num_columnas: numero de columnas ed tablero.
        ()"""
    return list(0 for _ in range(num_columnas))

def crear_tablero(num_filas = 3) -> tuple:
    """Crea el tablero 3 x 3
    :Para num_filas: numero de filas del tablero.
        (por defecto se establece el valor 3)
    :return: tupla con la matiz num_filas x num_columnas
    """
    return tuple(crear_fila() for _ in range(num_filas))

def mostrar_fila(fila: list):
    """Mostrar una fila del tablero
    :param fila: lista con la informacion de la fila a mostrar"""

    contenido_fila= "| "
    for celda in fila:
        contenido_fila += FICHAS[celda] + " | "
    print(contenido_fila)

def mostrar_tablero(tablero: tuple):
    """Mostrar en consola el tablero con las fichas.
    :param tablero: matriz de 3x3 con la informacion del tabler."""

    borrarConsola()
    print("-" * 13)
    for fila in tablero:
        mostrar_fila(fila)
        print("-" * 13)

def cambiar_turno(turno: int) -> int:
    """Modficar el turno.
    :param turno: jugador que tieene eel turno anterior.
    :return: jugador que tiene el turno  actual"""

    if turno % 2 == 0:
        return 1
    return 2

def pedir_posicion(fila_col: str, msj: str ="") -> int:


    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f"Elige la {fila_col} (1, 2, 3): ")) -1
            if not 0 <= pos <=2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"**Error** {fila_col} no valida")
    return pos

def comprobar_casilla(tablero:tuple, pos_ficha: dict) -> bool:
    """Comprobar si la casilla seleccionada es correcta para colocarla en el tablero"""

    return tablero[pos_ficha["fila"]][pos_ficha["columna"]] == 0

def colocar_ficha(tablero:tuple, jugador:int):
    """solicitar a un  jugador las posciones de la ficha que va a colocar.
    :param tablero: matriz de 3x3 con la informaacion del tablero.
    :param jugador: numero del jugador"""

    pos_ficha = {"fila": None, "columna": None}
    Pos_correcta = False

    while not Pos_correcta:
        pos_ficha["fila"] = pedir_posicion("fila", f"\nJugador {jugador}, coloque una ficha")
        pos_ficha["columna"] = pedir_posicion("columna")

        Pos_correcta = comprobar_casilla(tablero, pos_ficha)
        if Pos_correcta:
            tablero[pos_ficha["fila"]][pos_ficha["columna"]] = jugador
        else:
            pos_ficha["fila"] = pos_ficha["columna"] = None
            print("**Error** movimiento invalido")
            pulse_para_continuar()
            mostrar_tablero(tablero)

def verificar_ganador(tablero) -> tuple:
    #verificar filas y columnas
    
def jugar(tablero: tuple):

    turno = 0
    ronda = 0
    hay_ganador = False

    while not hay_ganador:

        turno = cambiar_turno(turno)
        if turno == 1:
            ronda += 1

        print(f"\nRonda {ronda}")
        print("-" * len(f"RONDA {ronda}") + "\n")

        colocar_ficha(tablero, turno)
        mostrar_tablero(tablero)

        if ronda >= 3:
            ganador, hay_ganador = verificar_ganador(tablero)
        
        if hay_ganador:
            print(f"\n El jugador {ganador} ha ganado!\n")
        
        if ronda == 9:
            hay_ganador = True
            print("\nEmpate!")



def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)
    


if __name__ == "__main__":
    main()