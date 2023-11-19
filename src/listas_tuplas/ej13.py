def poner_numeros() -> tuple:
    numes = input("Dame muchos numeros y separados por ,: ")
    separados = numes.split(",")
    convertidos = tuple(int(i) for i in separados)
    return convertidos

def main():
    convertidos = poner_numeros()
    print(f"el mayor de tus numeros es {max(convertidos)} y el menor es {min(convertidos)}")

if __name__ == "__main__":
    main()
    
