while True:
    name=str(input("Введите ваше имя: "))
    age=int(input("Введите ваш возраст: "))
    def main(nameuser, userage):
            if userage>=18:
                print(f"{nameuser}, Вам {userage}, вы совершеннолетний")
            else:
                print(f"{nameuser}, Вам {userage}, вы несовершеннолетний")
    main(name, age)


