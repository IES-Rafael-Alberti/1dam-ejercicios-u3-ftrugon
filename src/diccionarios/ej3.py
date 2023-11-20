def calculo(precios):
    producto = input("Dime el producto del que quieras saber el precio: ")
    if producto.capitalize() in precios:
        kilos = float(input("Cuantos kilos te quieres llevar: "))
        total = kilos * precios[producto.capitalize()]
        print("El precio de los kilos de "+str(producto)+" que te quieres llevar es de {:.2f}".format(total))
    else:
        print("Escribe un producto")

def main():
    precios = {"Platano" : 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja" : 0.70}
    calculo(precios)

if __name__ == "__main__":
    main()