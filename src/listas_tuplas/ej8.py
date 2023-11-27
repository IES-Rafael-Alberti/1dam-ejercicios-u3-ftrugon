def trasnformar_palabra(palabra:str) -> tuple:
#    return tuple(palabra)
    transformada = tuple(palabra)
    return transformada

def comprobar(palabra: str) -> bool:
    transformada = trasnformar_palabra(palabra)
    empezar = len(transformada) // 2
    #for i in range(len(transformada)):
    for i in range(empezar):
        #if transformada[i + empezar -1] == transformada[i - 1]:
        if transformada[i] == transformada[empezar - i - 1]:
            return True
    return False

def main():
    palabra = input("Dame tu palabra para comprobarla: ")
    resultado = comprobar(palabra)
    if resultado == True:
        print("tu palabra es un palindromo")
    else:
        print("tu palabra no es un palindromo")
    
if __name__ == "__main__":
    main()