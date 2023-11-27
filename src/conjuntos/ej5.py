def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12}
    lista_nume = list(numeros)
    pares = []
    multiplo_tres = []
    for numero in lista_nume:
        if numero % 2 == 0:
            pares.append(numero)
        if numero % 3 == 0 :
            multiplo_tres.append(numero)
    conjunpares = set(pares)
    conjudetres = set(multiplo_tres)
    pares_y_multiplos_de_tres = conjunpares - conjudetres
    print(f"{conjunpares}{conjudetres}{pares_y_multiplos_de_tres}")
if __name__ == "__main__":
    main()