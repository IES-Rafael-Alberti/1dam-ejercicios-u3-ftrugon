def mostrar_menu():
    print(f"\nQue quieres hacer:")
    print("1. Añadir factura")
    print("2. Pagar una factura")
    print("3. Terminar")

def elegir_opcion() -> int:
    estado = False
    while not estado:
        try:
            eleccion = int(input("Dime la opcion a elegir: "))
        except ValueError:
            print("Porfavor pon un numero")
        else:
            return eleccion

def pedir_factura(dictfactura: dict) -> dict:
    estadio = False
    while not estadio:
        try:
            cod_factura = int(input(f"\nNº de factura: "))
            coste = float(input("Cual es el coste de la factura: "))
            estadio = True
        except ValueError:
            print(f"\nPon parametros correctos")
    dictfactura[cod_factura] = coste
    return dictfactura

def pagar_factura(dictfactura) -> dict:
    estado = False
    while not estado:
        try:
            pagado = 0
            cod_factura = int(input(f"\nCual es el Cod_factura a pagar: "))
            estado = True
        except:
            print("Pon los formatos validos")
    
    if cod_factura in dictfactura:
        pagado += dictfactura[cod_factura]
        dictfactura.pop(cod_factura)
    else:
        print("No hay una factura con ese codigo")
    return pagado

def acabar_programa() -> bool:
    print(f"\nAsta pronto")
    return True

def a_pagar_y_pagado(dict_factura:dict, pagado:float):
    suma = sum(dict_factura.values())
    print(f"\ntienes que pagar {suma} y has pagado {pagado}")

def main(): 
    mostrar_menu()
    estado = False
    dict_factura = {}
    pagado = 0
    while not estado:
        opcion = elegir_opcion()
        
        if opcion == 1:
            pedir_factura(dict_factura)
            a_pagar_y_pagado(dict_factura, pagado)
            mostrar_menu()
        
        elif opcion == 2:
            pagado = pagar_factura(dict_factura)
            a_pagar_y_pagado(dict_factura, pagado)
            mostrar_menu()
        
        elif opcion == 3:
            estado = acabar_programa()
        
        else:
            print("Pon un numero valido")
    
if __name__ == "__main__":
    main()