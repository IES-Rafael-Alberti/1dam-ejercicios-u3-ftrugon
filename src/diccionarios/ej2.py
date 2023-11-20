def devolvercosa():
    nombre = input("Dime tu nombre: ")
    edad = input("Dime tu edad: ")
    direcion = input("Dime tu direccion: ")
    tlfn = input("Dime tu numero de telefono: ")

    dicio = {"Nombre":nombre,"Edad":edad,"Direccion":direcion,"Telefono": tlfn}
    
    return dicio
    
def main():
    dicio = devolvercosa()
    print(f"{dicio['Nombre']} tienes {dicio['Edad']} años, vives en {dicio['Direccion']} y tu telefono es {dicio['Telefono']}")

if __name__ == "__main__":
    main()