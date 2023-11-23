def pedir_articulo() -> str:
    #retorna el primer mensaje del articulo
    return input("Dime el articulo(* si no quieres meter nada): ")

def pedir_articulo2() -> str:
    #retorna el segundo articulo hacia adelante
    return input("Dime cual es el siguiente articulo(* si quieres acabar): ")

def pedir_precio() -> float:
    #para retornar el precio
    return float(input("Dime su precio: "))

def bucle_de_artiprecio() -> dict:
    articulo = pedir_articulo()
    if articulo == "*":
        return(print("No se a introducido nada champion"))
    #try:
    precio = pedir_precio()
    #except:
    #    print("tienes que poner un numero")
    listadelacompra = {}
    while articulo:
        listadelacompra[articulo] = precio
        articulo = pedir_articulo2()
        if articulo == "*":
            break
        precio = pedir_precio()
    return listadelacompra

def calctotal(listadelacompra:dict) -> int:
    precios = sum(listadelacompra.values())
    return precios


def ponerlaslineas(listadelacompra:dict):
    print(f"\nLista de la compra\n")
    for llave, valor in listadelacompra.items():
        print(f"{llave} -----> {valor}")
    total = calctotal(listadelacompra)
    print("El total es {:.2}€".format(total))

def main(): 
    listadelacompra = bucle_de_artiprecio()
    ponerlaslineas(listadelacompra)
if __name__ == "__main__":
    main()