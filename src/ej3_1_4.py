def pedir_numeros():
    #contnum = 1
    #linea = ""
    print("Dime los numeros de la primitiva")
    #while contnum <= 6:
    #    num1 = int(input(f"({contnum}) => " ))
    #    contnum += 1
    #    linea += f"{num1} "
    #listalinea = linea.split(" ")
    #del listalinea[6]
    #return listalinea

    #listatodo = list(input(f"Numerin {i +1}: ") for i in range(6))
    #print(listatodo)
    #return listatodo
    
    lista = []
    cont = 0
    while cont < 6:
        try:
            num = input(f"({cont + 1})=> ")
            if int(num) < 1 or int(num) > 50:
                print("Escribe un numero valido")

            elif num in lista:
                print("El numero no se puede repetir")

            else:
                lista.append(num)
                #lista += num 
                cont += 1
        except ValueError:
            print("Tienes que poner un numero")
            
    print(lista)
    

#def main():
    
if __name__=="__main__":
    pedir_numeros()