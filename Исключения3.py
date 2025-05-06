
#s=str(input("Введите строку"))
def parse_int(s):
    k = 1
    i = 1
    l=len(s)
    try:
        for i in range(l):
            k=int(s[i])
    except ValueError:
        print("ошибка")
while True:
    s = str(input("Введите строку"))
    parse_int(s)




