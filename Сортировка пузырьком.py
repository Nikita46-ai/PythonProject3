import random
def main():
    array = [5,1,23,1,4,5,4,7,8,45]
    random.shuffle(array)
    print(array)
    j=0
    k=1
    for i in range(10):
        for j in range(0, 10-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)

main()















