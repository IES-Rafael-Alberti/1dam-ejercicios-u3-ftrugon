def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    frutas_comunes = set_frutas1 & set_frutas2
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    print(frutas_comunes)
    print(frutas_solo_en_frutas1)
    print(frutas_solo_en_frutas2)
    
if __name__ == "__main__":
    main()