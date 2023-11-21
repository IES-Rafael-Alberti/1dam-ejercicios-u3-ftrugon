def sumar_a_diccio(info,clave,diccio_cosas) -> dict:
    diccio_cosas[info] = clave
    return diccio_cosas



def mostrar_diccionario(diccio_cosas) -> dict:
    print(f"\nSe ha actualizado la lista -----------------------------------------------------\n")
    for info, clave in diccio_cosas.items():
        print(f"Se ha añadido {info} con clave {clave}\n")
    print("--------------------------------------------------------------------------------------")



def pedir_info():
    info = input("\nDime la informacion a añadir al diccionario(* si no quieres añadir informacion): ")
    ##### Esto de aqui abajo , este crear diccio_cosas me a entretenido 2horas como minimo, me he perdido como la manca de nisaxter subia a platino
    diccio_cosas = {}
    if info != "*":
        clave = input("Dime la clave a añadir al diccionario: ")
    while info != "*":
        diccio_cosas = sumar_a_diccio(info,clave,diccio_cosas)
        mostrar_diccionario(diccio_cosas)
        info = input("Dime la informacion a añadir al diccionario(* si quieres acabar): ")
        if info == "*":
            break
        clave = input("Dime la clave a añadir al diccionario: ")
    
def main(): 
    pedir_info()
if __name__ == "__main__":
    main()