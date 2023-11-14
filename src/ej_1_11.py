def calculo(lista1, lista2):
    for i in range(0, 3):
        lista3 = lista1[i] * lista2[i]
        print(lista3)


def main():
    lista1 = (1,2,3)
    lista2 = (-1,0,2)
    calculo(lista1,lista2)



if __name__ == "__main__":
    main()