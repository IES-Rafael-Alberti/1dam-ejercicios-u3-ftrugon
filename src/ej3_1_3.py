def num_asig():
    numasig = int(input("Dime el numero de asignaturas: "))
    return(numasig)

def pedir_asignotas(numasig) ->list:
    listatotal = list()
    for i in range(numasig):
        asigna = input("Dime una asignatura: ")
        nota = int(input("Ahora su nota: "))
        listatotal.append([asigna, nota])
    return(listatotal)

def mostrar_cosas(listatotal:list):
    #for asigna , nota in listatotal:
    #    print(f"En {asigna} has sacado un {nota}")
    for i in range(len(listatotal)):
        print(f"En {listatotal[i][0]} has sacado un {listatotal[i][1]}")


def main():
    try:
        numasig = num_asig()
    except ValueError:
        print("Una asignatura poooorfa")
    listatotal = pedir_asignotas(numasig)
    mostrar_cosas(listatotal)


if __name__ == "__main__":
    main()