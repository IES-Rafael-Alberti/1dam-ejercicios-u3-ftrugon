def comprobar(tablero):
    if comprobar_horizontal(tablero,1) or comprobar_vertical(tablero,1) or comprobar_diagonales(tablero, 1):
        print("gana jugador 1")
    elif comprobar_horizontal(tablero,2) or comprobar_vertical(tablero,2) or comprobar_diagonales(tablero, 2):
        print("gana jugador 2")
    else:
        print("Empate")
    
def comprobar_horizontal(tablero:tuple,ficha:str) -> bool:
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == ficha:
            return True
    return False

def comprobar_vertical(tablero:tuple,ficha:str)-> bool:
    for i in range(len(tablero)):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == ficha:
            return True
    return False

def comprobar_diagonales(tablero: tuple, ficha: str) -> bool:
    return tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha or tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha

def main():
    comprobar(([1,2,0],[2,2,0],[1,1,2]))
    comprobar(([1,2,0],[1,2,0],[1,1,2]))
    comprobar(([2,2,0],[1,2,0],[1,1,2]))
    comprobar(([1,1,1],[2,2,0],[1,2,2]))
    comprobar(([1,2,0],[2,2,2],[1,1,2]))

if __name__ == "__main__":
    main()