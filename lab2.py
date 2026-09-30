import math


# ==========================================
# ЗАДАЧИ СРЕДНЕЙ СЛОЖНОСТИ (Вариант 9)
# ==========================================

def t9_minimo_lista(spisok):
    """9. Минимальный элемент списка."""
    if not spisok:
        return None
    minimum = spisok[0]
    for element in spisok:
        if element < minimum:
            minimum = element
    return minimum


def t1_tabla_umnozheniya(n):
    """1. Таблица умножения."""
    print(f"--- Таблица умножения на {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def t6_kalkulyator():
    """6. Калькулятор."""
    print("\n--- Калькулятор ---")
    print("Доступные операции: +, -, *, /")
    operaciya = input("Выберите операцию: ")

    try:
        chislo1 = float(input("Введите первое число: "))
        chislo2 = float(input("Введите второе число: "))

        if operaciya == '+':
            print(f"Результат: {chislo1 + chislo2}")
        elif operaciya == '-':
            print(f"Результат: {chislo1 - chislo2}")
        elif operaciya == '*':
            print(f"Результат: {chislo1 * chislo2}")
        elif operaciya == '/':
            if chislo2 != 0:
                print(f"Результат: {chislo1 / chislo2}")
            else:
                print("Ошибка: Деление на ноль невозможно.")
        else:
            print("Ошибка: Неверная операция.")
    except ValueError:
        print("Ошибка: Введите числа корректно.")


# ==========================================
# ЗАДАЧИ ПОВЫШЕННОЙ СЛОЖНОСТИ (Вариант 9)
# ==========================================

def a9_summa_rekursivnaya(n):
    """9. Рекурсивная сумма чисел."""
    if n <= 0:
        return 0
    return n + a9_summa_rekursivnaya(n - 1)


def a2_algoritm_evklida(a, b):
    """2. Алгоритм Евклида (НОД) рекурсивно."""
    if b == 0:
        return a
    return a2_algoritm_evklida(b, a % b)


# ==========================================
# ГЛАВНЫЙ БЛОК ДЛЯ ПРОВЕРКИ
# ==========================================
if __name__ == "__main__":
    print("=== ПРОВЕРКА ВАРИАНТА 9 ===")

    moy_spisok = [5, 2, 9, 1, 7]
    print(f"Минимальный элемент списка {moy_spisok}: {t9_minimo_lista(moy_spisok)}")

    t1_tabla_umnozheniya(5)

    t6_kalkulyator()

    n_summa = 5
    print(f"Рекурсивная сумма до {n_summa}: {a9_summa_rekursivnaya(n_summa)}")

    chislo1, chislo2 = 48, 18
    print(f"НОД чисел {chislo1} и {chislo2} (рекурсивно): {a2_algoritm_evklida(chislo1, chislo2)}")
