def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def main():
    num = None
    string = "5 6 8 3 4 2 8 11 62 7 89 90"
    try:
        num = int(input("Введите число: "))
        int_list = list(map(int, string.split()))
    except ValueError as error:
        print(error)
        return

    sort_list = sort(int_list)
    print(sort_list)
    print(binary_search(sort_list, num, 0, len(sort_list)))


if __name__ == '__main__':
    main()
