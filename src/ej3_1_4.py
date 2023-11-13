def pedir_numeros():
    contnum = 1
    linea = ""
    print("Dime los numeros de la primitiva")
    while contnum <= 6:
        num = int(input(f"({contnum}) => " ))
        contnum += 1
        linea += f"{num} "
    listalinea = linea.split(" ")
    print(listalinea)
    listalinea = listalinea
#def main():
    
if __name__=="__main__":
    pedir_numeros()