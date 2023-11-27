def num_asig():
    numasig = int(input("Dime el numero de asignaturas asignadas: "))
    return(numasig)

def pedir_asignatura(numasig) -> tuple:
    return tuple(input("Dime una asignatura: ") for i in range(numasig))

def mostrar_asig(asig):
    mostrar = f"Tus asignaturas son "
    for i in range(len(asig)):
        mostrar += f" {asig[i]}"
    print(mostrar)

def main():
    try:
        numasig = num_asig()
        asig = pedir_asignatura(numasig)
        mostrar_asig(asig)
    except ValueError:
        print("Una asignatura poooorfa")
    

if __name__ == "__main__":
    main()