def main():
    fecha = input("Introduce la fecha en formato dd/mm/aaaa: ")
    listafecha = fecha.split("/")
    meses = {1: 'Enero',2: 'Febrero',3: 'Marzo',4: 'Abril',5: 'Mayo',6: 'Junio',7: 'Julio',8: 'Agosto',9: 'Septiembre',10: 'Octubre',11: 'Noviembre',12: 'Diciembre'}
    print(f"{listafecha[0]} de {meses[int(listafecha[1])]} de {listafecha[2]}")

if __name__ == "__main__":
    main()