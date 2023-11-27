def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecedario = set(chr(i) for i in range(ord("a"),ord("z")+1))
    abecedario_conso = abecedario - vocales
    comunes = abecedario & vocales
    print(abecedario_conso)
    print(comunes)
    #no entiendo porque hacer comunes si tengo las vocales ¯\(ツ)/¯
if __name__ == "__main__":
    main()