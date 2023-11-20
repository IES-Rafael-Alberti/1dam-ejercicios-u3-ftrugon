def comprobar(diccionario):
    divisa = input("Dime una divisa: ")
    if divisa.capitalize() in diccionario:
        print(f"El simbolo de {divisa} es {diccionario[divisa.capitalize()]}")
    else:
        print(f"Eso no es una divisa")

def main():
    diccionario = {"Euro": "€" , 'Dollar': '$', 'Yen': '¥'}
    comprobar(diccionario)

if __name__ == "__main__":
    main()