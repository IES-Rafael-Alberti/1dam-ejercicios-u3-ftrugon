def num_asig():
    numasig = int(input("Dime el numero de asignaturas: "))
    return(numasig)

def pedir_asignotas(numasig:int ) ->list:
    listatotal = list()
    for i in range(numasig):
        asigna = input("Dime una asignatura: ")
        nota = int(input("Ahora su nota: "))
        listatotal.append([asigna, nota])
    return(listatotal)

def quitar(lista:list) -> list:
    nuevalista = []
    for i in range(len(lista)):
        if lista[i][1] >= 5:
            continue
        else:
            nuevalista.append(lista[i])
    return nuevalista

def mostrar(nuevalista:list) ->str: 
    linea = "Tienes que repetir "
    for i in range(len(nuevalista)):
        if i == 0:
            linea += f"{nuevalista[i][0]}"
        else:
            linea += f" {nuevalista[i][0]}"
    print(linea)

def main():
    numasig = num_asig()
    listatotal = pedir_asignotas(numasig)
    nuevalista = quitar(listatotal)
    mostrar(nuevalista)

if __name__ == "__main__":
    main()