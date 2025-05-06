import random
def main():
    b=0
    k=1
    c=0
    pp = int(input("Введите колличество случайных чисел"))
    while k<=pp:
        k+=1
        a=random.randint(1,50)
        print(a)
        b=b+a
        c=b/10
    print("Сумма",b)
    print("Cреднее арифмитическое",c)
    hh = str(input())

main()

