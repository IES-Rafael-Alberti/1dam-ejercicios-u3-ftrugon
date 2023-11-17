def pedir_palabra() -> tuple:
    lista = ""
    palabra = input("Dame una palabra: ").lower()
    while palabra != "":
        lista = lista + palabra
        palabra =input("Dame una palabra: ").lower()
    lista = tuple(lista)
    return lista

def contar_vocales(palabra: tuple) -> tuple:
    vocales =(["a",0],["e",0],["i",0],["o",0],["u",0])
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales

def mostrar(vocales):
    print("Numero de vocales: ")
    for vocal in vocales:
        print(f"{vocal[0]} = {vocal[1]}")

def main():
    palabra = pedir_palabra()
    vocales = contar_vocales(palabra)
    mostrar(vocales)

if __name__ == "__main__":
    main()