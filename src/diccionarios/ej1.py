def comprobar(diccionario):
    divisa = input("Dime una divisa: ")
    if divisa.title() in diccionario:
        print(f"El simbolo de {divisa} es {diccionario[divisa.title()]}")
    else:
        print(f"Eso no es una divisa")

def main():
    diccionario = {"Euro": "€" , 'Dollar': '$', 'Yen': '¥'}
    comprobar(diccionario)

if __name__ == "__main__":
    main()