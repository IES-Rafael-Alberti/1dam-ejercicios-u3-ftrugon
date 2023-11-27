def main():
    asignaturas = {"Mates": 6,"Física": 4,"Química": 5}
    total = 0
    for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} = {creditos}")
        total += creditos
    print(f"El total de creditos del curso ha sido {total}")
if __name__ == "__main__":
    main()