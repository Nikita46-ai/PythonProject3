def safe_division(a,b):
    if b==0:
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Деление на 0 невозможно")
    else:
        print(a/b)
safe_division(2,0)