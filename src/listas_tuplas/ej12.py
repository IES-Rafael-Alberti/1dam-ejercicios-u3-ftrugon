def calculo(matriz1:tuple,matriz2:tuple) -> tuple:
    matrizfila = list()
    for i in range(len(matriz1)):
        matrizcolumna = list()
        for x in range(len(matriz1[0])):
            matrizcolumna.append(matriz1[i][x] * matriz2[i][x])
        matrizfila.append(matrizcolumna)
    print(f"{matriz1} + {matriz2} = {matrizfila}")

#def producto2(matriz1,matriz2):
#    return tuple(matriz1[i] * matriz2[i] for i in range(len(matriz1)))
#
#def producto(matriz1, matriz2):
#    return tuple(producto2(matriz1[i], matriz2[i]) for i in  range(len(matriz1)))

def main():
    matriz1 = ([1,2],[3,4],[5,6])
    matriz2 = ([-1,0],[0,1],[1,1])
    calculo(matriz1,matriz2)
    #matriz3 = producto(matriz1,matriz2)
    #print(f"{matriz1} + {matriz2} = {matriz3}")
if __name__ == "__main__":
    main()