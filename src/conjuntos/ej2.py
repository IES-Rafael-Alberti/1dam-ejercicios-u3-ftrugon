def alumnos_primaria() -> list:
    print("Dime los nombres de primaria")
    nombre = input("Dime el nombre: ")
    primaria = []
    while nombre.title() != "X":
        primaria.append(nombre.title())
        nombre = input("Dime el nombre: ")
    else:
        return primaria

def alumnos_secundaria() -> list:
    print("Dime los nombres de secundaria")
    nombre = input("Dime el nombre: ")
    secundaria = []
    while nombre.title() != "X":
        secundaria.append(nombre.title())
        nombre = input("Dime el nombre: ")
    else:
        return secundaria

def mostrar_cosas(primaria:list, secundaria:list):
    print(f"\nSe van a mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.")
    lista_escuela = set(primaria + secundaria)
    print(lista_escuela)
    
    print(f"\nSe van a mostrar qué nombres se repiten entre los alumnos de primaria y secundaria")
    repetidos = set(primaria) & set(secundaria)
    print(repetidos)

    print(f"\nSe van a mostrar qué nombres de primaria no se repiten en los de nivel secundaria.")
    exclusivo_primaria = set(primaria) - set(secundaria)
    print(exclusivo_primaria)

    print(f"\nSe van a mostrar si todos los nombres de primaria están incluidos en secundaria.")
    primaria_repetido = set(primaria) & set(secundaria)
    Se_repiten = set(primaria).issubset(set(secundaria))
    if Se_repiten == False:
        valor = "No"
        print(f"{valor} todos los nombres de primaria están incluidos en secundaria. Solo se repiten")
        print(f"{primaria_repetido}")
    else:
        print(f"Todos los nombres de primaria están incluidos en secundaria.")
        print(f"{primaria_repetido}")

    

def main():
    primaria = alumnos_primaria()
    secundaria = alumnos_secundaria()
    mostrar_cosas(primaria, secundaria)
if __name__ == "__main__":
    main()