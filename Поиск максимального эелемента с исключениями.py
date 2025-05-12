def main():
    numbers = str(input())
    k=0
    for i in range((len(numbers))):
        for k in range(len(numbers)):
            if numbers[i]>numbers[k]:
                j+=1
            else:
                j=0
            if j == len(numbers)-1:
                print(numbers[i])
    if not numbers:
        print("Список пуст")
    try:
        for i in range(len(numbers)):
            numint = int(numbers[i])
    except:
        print("Некорректный элемент:", numbers[i])


main()


