def bubble_sort(arr):
    """реализация сортировки пузырьком"""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():

    print("Сортировка пузырьком")

    # Ввод чисел
    try:
        numbers = list(map(float, input("Введите числа через пробел: ").split()))
    except:
        print("Ошибка ввода! Используйте только числа.")
        return

    if not numbers:
        print("Не введено чисел!")
        return

    # Сортировка
    original = numbers.copy()
    sorted_nums = bubble_sort(numbers)

    # Вывод
    print(f"\nИсходный массив: {original}")
    print(f"Отсортированный: {sorted_nums}")


if __name__ == "__main__":
    main()