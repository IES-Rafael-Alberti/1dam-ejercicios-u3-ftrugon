def poner_numeros() -> tuple:
    numes = input("Dame muchos numeros y separados por ,: ")
    separados = numes.split(",")
    convertidos = tuple(int(i) for i in separados)
    return convertidos

def calcular_media(convertidos:tuple) -> int:
    media = 0
    for i in range(len(convertidos)):
        media += convertidos[i]
    media /= 2
    return media

def main():
    convertidos = poner_numeros()
    media = calcular_media(convertidos)
    print(f"La media de los numeros es {media} y la desviacion tipica no se calcularla XD")

if __name__ == "__main__":
    main()
    
