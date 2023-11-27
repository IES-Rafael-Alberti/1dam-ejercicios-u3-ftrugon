def pedir_palabras() -> list:
    #Le pide al usuario las palabras a traducir
    return input("Dame las palabras traducidas con el formato (palabra1):(traduccion1),(palabra2):(traduccion2): ")

def transformar_a_lista2(listapalabras:str) -> list:
    #convierte la cadena str de pedir_palabra a una lista en la que cada valor es [[palabra:traduccion],[palabra2:traduccion]]
    listade2 = listapalabras.split(",")
    return listade2

def transformar_a_diccio(listade2:list) -> dict: 
    #Para cada elemento en listade2 crea un diccionario en la llave es la posicion antes de ":" y el valor es lo de despues
    diccio = dict()
    for elemento in listade2:
        diccio[elemento.split(":")[0]] = [elemento.split(":")[1]]
    return diccio

def pedir_frase() -> str:
    #Retorna el str de algo que le demos
    return input("Dime la frase, yo traducire las palabras: ")


def reemplazar(frase:str, diccio:dict) -> str:
    # aqui esta mi problema, EJ: yo traduzco hola a hello, si yo pongo hola que tal me deberia devolver Hello que tal
    # en lugar de eso me devuelve ["Hello"] que tal 
    listadefrase = frase.split(" ")
    x =""
    for elemento in listadefrase:
        if elemento in diccio:
            x += frase.replace(elemento, str(diccio.get(elemento,elemento)))
    return x


def main(): 
    listapalabras = pedir_palabras()
    listade2 = transformar_a_lista2(listapalabras)
    diccio = transformar_a_diccio(listade2)

    frase = pedir_frase()
    frasefinal = reemplazar(frase,diccio)
    if frasefinal =="":
        print("No se puede traducir ninguna palabra")
    else:
        print(frasefinal)
if __name__ == "__main__":
    main()