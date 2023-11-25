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
    print("Se van a mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.")
    lista_escuela = set(primaria + secundaria)
    print(lista_escuela)
    
    print("Se van a mostrar qué nombres se repiten entre los alumnos de primaria y secundaria")
    repetidos = set(primaria) & set(secundaria)
    print(repetidos)

def main():
    primaria = alumnos_primaria()
    secundaria = alumnos_secundaria()
    mostrar_cosas(primaria, secundaria)
if __name__ == "__main__":
    main()