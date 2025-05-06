stroka1 = str(input())
stroka2 = str(input())
def main(str1,str2):
    perstroki1=0
    perstroki2=0
    annagrama=""
    try:
        while perstroki1 < len(str2):
            if str1[perstroki1] == str2[perstroki2]:
                annagrama+=stroka1[perstroki1]
                perstroki1+=1
                perstroki2=0
            else:
                perstroki2+=1
        if annagrama == str1:
            print("true")
        else:
            print("false")

    except IndexError:
        print("Ошибка")

main(stroka1,stroka2)





