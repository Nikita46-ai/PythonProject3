def mm():
    s=str(input("Введите слово"))
    d=len(s)
    i=0
    k=0
    a=""
    for i in range(d):
        k+=1
        a=a+s[d-k]
    if a == s:
        print("Палиндром")
    else:
        print("Не палиндром")
while True:
    mm()
