import json
def chtenie():
    with open('оценки.json', 'r', encoding='utf-8') as write_file:
        t=json.load(write_file)
    print(t)

def beststudent():
    ocenki={}
    while True:
        name = input("Введите имя студента или стоп для завершения, или 'проверить', что бы посмотреть результат: ")
        if name.lower()=='стоп':
            break
        elif name.lower() == 'посмотреть':
            chtenie()
            break
        elif name.lower() == 'выгрузить':
            with open('оценки.json', 'w', encoding='utf-8') as write_file:
                json.dump(ocenki,write_file, ensure_ascii=False)
                print("Ваши данные выгружены")
                break
        if name.lower() != 'проверить':
            ocenka = float(input(f"Введите оценку для  {name}: "))
            ocenki[name] = ocenka
            best= max(ocenki, key=ocenki.get)
        else:
            print(f"Список студентов и их оценки:  ({ocenki})")
    print(f"Студент с наивысшей оценкой: {best} ({ocenki[best]})")
while True:
    beststudent()


 #with open("data4.json", "w", encoding='utf-8') as write_file:
# json.dump("к", write_file)