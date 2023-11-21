def retornar__lista(lista):
    conjunto_calles = set()
    for i in lista:
        conjunto_calles.add(i[3])
    print(conjunto_calles)


def main():
    lista = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"), 
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
        ("Jorge Russo", 15, 958, "Mirasol 218")
        ]
    retornar__lista(lista)



if __name__ == "__main__":
    main()


