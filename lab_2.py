"""Программа, выводящая количество простых чисел в диапозоне."""
def is_prime(num):
    """Проверяет, является ли число простым."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_primes(start, end):
    """Возвращает количество простых чисел в заданном диапазоне."""
    prime_count = 0
    for number in range(start, end + 1):
        if is_prime(number):
            prime_count += 1
    return prime_count


def main():
    """Основная функция программы."""
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if start > end:
            print("Ошибка: начало диапазона больше конца.")
            return
        prime_numbers_count = count_primes(start, end)
        print(f"Количество простых чисел в диапазоне от {start} до {end}: {prime_numbers_count}")
    except ValueError:
        print("Ошибка: введите целые числа.")

if __name__ == "__main__":
    main()
