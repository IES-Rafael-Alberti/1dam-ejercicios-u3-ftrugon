def quitar(abecedario:list) -> list:
    abecedario2 = []
    cont = 1
    #for i in range(len(abecedario)):
    for i in abecedario:
        if cont % 3 != 0:
            abecedario2.append(i)
        cont += 1
    print(abecedario2)
    

def main():
    abecedario = list(chr(i) for i in range(ord("a"),ord("z")+1))
    quitar(abecedario)

if __name__ == "__main__":
    main()
