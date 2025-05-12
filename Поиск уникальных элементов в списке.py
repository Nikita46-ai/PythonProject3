def main():
    numbers=str(input())
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    print(unique)
    try:
        for i in range(len(numbers)):
            numint = int(numbers[i])
    except:
        print("Некорректный элемент:",numbers[i])
main()


