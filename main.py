def create_numeric_list():
    n = int(input("Въведете броя на елементите (15 < n < 35): "))
    while not (15 < n < 35):
        print("Невалиден вход. Моля, въведете стойност между 15 и 35.")
        n = int(input("Въведете броя на елементите (15 < n < 35): "))

    num_list = []
    for _ in range(n):
        num = int(input(f"Въведете положително цяло число между 30 и 300: "))
        while not (30 <= num <= 300):
            print("Невалиден вход. Моля, въведете число между 30 и 300.")
            num = int(input(f"Въведете положително цяло число между 30 и 300: "))
        num_list.append(num)

    return num_list

def count_tens_digit_multiple_of_3(lst):
    count = sum(1 for num in lst if (num // 10) % 3 == 0)
    return count

def index_min_remainder_4_mod_6(lst):
    min_remainder_4_mod_6 = min((num, i) for i, num in enumerate(lst) if num % 6 == 4)
    return min_remainder_4_mod_6[1]

def create_second_list(lst):
    second_list = [num for num in lst if 10 <= num <= 99 and (num % 2 == 0 or num % 3 == 0)]
    return second_list

def mean_odd_indices(lst):
    odd_indices = [num for i, num in enumerate(lst) if i % 2 != 0]
    mean = sum(odd_indices) / len(odd_indices) if odd_indices else 0
    return mean

def delete_min_even(lst):
    min_even = min(num for num in lst if num % 2 == 0)
    lst.remove(min_even)

# Main program
numeric_list = create_numeric_list()
print(f"Оригинален списък: {numeric_list}")

tens_digit_multiple_of_3_count = count_tens_digit_multiple_of_3(numeric_list)
print(f"Брой елементи с десетки, кратни на 3: {tens_digit_multiple_of_3_count}")

min_remainder_4_mod_6_index = index_min_remainder_4_mod_6(numeric_list)
print(f"Индекс на минимален елемент с остатък 4 , 6: {min_remainder_4_mod_6_index}")

second_list = create_second_list(numeric_list)
print(f"Втори списък: {second_list}")

odd_indices_mean = mean_odd_indices(second_list)
print(f"Средно аритметично на елементи с нечетни индекси: {odd_indices_mean}")

delete_min_even(second_list)
print(f"Втори списък след изтриване на минималното четно число: {second_list}")
