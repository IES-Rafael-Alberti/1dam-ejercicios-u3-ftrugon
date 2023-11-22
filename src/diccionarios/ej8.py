def pedir_palabras() -> list:
    return input("Dame las palabras traducidas con el formato (palabra1):(traduccion1),(palabra2):(traduccion2): ")

def transformar_a_lista2(listapalabras):
    listade2 = listapalabras.split(",")
    return listade2

def lista1(listade2):
    
    for i in range(listade2):
        listade1 = listade2[i].split(":")
    return listade1

def transformar_a_diccio(listade1):
    diccio = dict(listade1)
    print(diccio)

def main(): 
    listapalabras = pedir_palabras()
    listade2 = transformar_a_lista2(listapalabras)
    listade1 = []
    listade1 = lista1(listade2)
    diccio = transformar_a_diccio(listade1)
    print(diccio)


if __name__ == "__main__":
    main()