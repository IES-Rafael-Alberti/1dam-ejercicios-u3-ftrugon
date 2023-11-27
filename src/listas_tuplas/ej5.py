def ordenar(lista) -> list:
    lista.sort()
    lista.reverse()
    return lista

def separarcomas(lista:list) -> str:
    linea = ""
    for i in range(len(lista)):
        if i == 0:
            linea += f"{lista[i]}"
        else:
            linea += f", {lista[i]}"
        
    print(linea)


def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    ordenar(lista)
    separarcomas(lista)



if __name__ == "__main__":
    main()