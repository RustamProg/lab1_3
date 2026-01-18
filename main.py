def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    print("Сортировка пузырьком")

    try:
        numbers = list(map(float, input("Введите числа через пробел: ").split()))
        if not numbers:
            print("Не введено чисел!")
            return

        direction = input("Сортировать по возрастанию? (y/n): ").lower()
        ascending = direction == 'y'

        original = numbers.copy()
        sorted_nums = bubble_sort(numbers, ascending)

        print(f"\nИсходный: {original}")
        print(f"Отсортированный: {sorted_nums}")

    except:
        print("Ошибка ввода!")


if __name__ == "__main__":
    main()