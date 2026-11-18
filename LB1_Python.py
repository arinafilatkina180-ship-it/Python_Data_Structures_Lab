
# ============================================
# ЛАБОРАТОРНА РОБОТА №1
# Імплементація та маніпуляції основними
# типами та структурами даних у Python
# ============================================

# ЗАВДАННЯ 1. СПИСКИ (LIST)

print("=" * 50)
print("ЗАВДАННЯ 1. СПИСКИ (LIST)")
print("=" * 50)

# 1. Створення початкового списку цілих чисел
numbers = [12, 5, 8, 21, 3, 16, 10, 7]

print("\n1. Початковий список:")
print(numbers)

# 2. Індексація списку
print("\n2. Індексація списку:")

print("Елемент з індексом [0]:", numbers[0])
print("Елемент з індексом [3]:", numbers[3])
print("Елемент з індексом [-1]:", numbers[-1])
print("Елемент з індексом [-3]:", numbers[-3])

# 3. Зрізи списку (Slicing)
print("\n3. Зрізи списку:")

# Перші три елементи
print("Перші три елементи:", numbers[:3])

# Елементи з індексу 2 до 5
print("Елементи з індексу 2 до 5:", numbers[2:6])

# Кожен другий елемент
print("Кожен другий елемент:", numbers[::2])

# 4. Модифікація списку
print("\n4. Модифікація списку:")

# Додавання нового елемента в кінець списку
numbers.append(25)

print("\nПісля додавання елемента 25:")
print(numbers)

# Заміна елемента з індексом 2
numbers[2] = 100

print("\nПісля заміни елемента з індексом 2 на 100:")
print(numbers)

# Видалення елемента зі значенням 21
numbers.remove(21)

print("\nПісля видалення елемента 21:")
print(numbers)

# ============================================
# ЗАВДАННЯ 2. КОРТЕЖІ (TUPLE)
# ============================================

print("\n" + "=" * 50)
print("ЗАВДАННЯ 2. КОРТЕЖІ (TUPLE)")
print("=" * 50)

# 1. Створення колекції кортежів студентів
students = [
    ("Симоненко", "КБ-25", [90, 85, 95]),
    ("Бондаренко", "КБ-25", [78, 88, 82]),
    ("Мельник", "КБ-26", [92, 96, 89])
]

print("\n1. Початкова колекція записів студентів:")

for student in students:
    print(student)
    
# 2. Розпакування кортежу за допомогою функції

def unpack_student(student_record):
    surname, group, grades = student_record
    return surname, group, grades


print("\n2. Розпакування запису студента:")

surname, group, grades = unpack_student(students[0])

print("Прізвище:", surname)
print("Група:", group)
print("Оцінки:", grades)

# 3. Обчислення середнього бала всіх студентів

def calculate_average(students_records):
    total_sum = 0
    total_count = 0

    for student in students_records:
        surname, group, grades = student

        total_sum += sum(grades)
        total_count += len(grades)

    if total_count == 0:
        return 0

    return total_sum / total_count


average = calculate_average(students)

print("\n3. Середній бал усіх студентів:")
print("Середній бал:", round(average, 2))

# 4. Демонстрація незмінності кортежу

print("\n4. Перевірка незмінності кортежу:")

try:
    students[0][0] = "Іваненко"
except TypeError as error:
    print("Помилка при спробі змінити елемент кортежу:")
    print(type(error).__name__)
    print("Кортеж не дозволяє змінювати свої елементи.")
# 5. Демонстрація мутабельності вкладеного списку

print("\n5. Зміна вкладеного списку оцінок:")

print("До зміни:", students[0])

students[0][2].append(100)

print("Після зміни:", students[0])

# ==================================================
# ЗАВДАННЯ 3. СЛОВНИКИ (DICTIONARIES)
# ==================================================

# 1. Введення та нормалізація тексту

print("\nЗАВДАННЯ 3. СЛОВНИКИ (DICTIONARIES)")
print("=" * 50)

print("Введіть текст для аналізу.")
print("Для завершення введення напишіть: КІНЕЦЬ")

lines = []

while True:
    line = input()

    if line.strip().upper() == "КІНЕЦЬ":
        break

    lines.append(line)

text = " ".join(lines)

normalized_text = text.lower()

for punctuation in ".,!?;:()[]{}\"'":
    normalized_text = normalized_text.replace(punctuation, "")

print("\nНормалізований текст:")
print(normalized_text)

# 2. Створення словника та підрахунок частоти слів

word_frequency = {}

words = normalized_text.split()

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("\n3.2. Частота появи слів:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

# 3. Безпечне отримання значень і сортування

print("\n3.3. Безпечне отримання значення:")

missing_word = "кібербезпека"
print(
    f"Частота слова '{missing_word}':",
    word_frequency.get(missing_word, 0)
)

print("\nСортування за алфавітом:")
for word in sorted(word_frequency):
    print(f"{word}: {word_frequency[word]}")

print("\nСортування за частотою:")
sorted_by_frequency = sorted(
    word_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

for word, frequency in sorted_by_frequency:
    print(f"{word}: {frequency}")
    # 4. Створення похідного словника за допомогою Dictionary Comprehension

frequent_words = {
    word: frequency
    for word, frequency in word_frequency.items()
    if frequency >= 2
}

print("\n3.4. Слова, які зустрічаються щонайменше двічі:")
for word, frequency in frequent_words.items():
    print(f"{word}: {frequency}")
    # 4.1. Створення множин та видалення дублікатів

print("\nЗАВДАННЯ 4. МНОЖИНИ (SETS)")
print("=" * 50)

users_group_a = ["ID101", "ID102", "ID103", "ID103", "ID104", "ID105"]
users_group_b = ["ID103", "ID104", "ID106", "ID106", "ID107"]

set_a = set(users_group_a)
set_b = set(users_group_b)

print("Початкова колекція A:", users_group_a)
print("Множина A:", sorted(set_a))

print("\nПочаткова колекція B:", users_group_b)
print("Множина B:", sorted(set_b))
# 2. Основні операції над множинами

print("\n4.2. Основні операції над множинами:")

union_set = set_a | set_b
intersection_set = set_a & set_b
symmetric_difference_set = set_a ^ set_b

print("Об'єднання множин:", sorted(union_set))
print("Перетин множин:", sorted(intersection_set))
print("Симетрична різниця:", sorted(symmetric_difference_set))
# 3. Перевірка відношення підмножини

print("\n4.3. Перевірка відношення підмножини:")

subset_a = {"ID103", "ID104"}
subset_b = {"ID106", "ID107"}

print("Чи є subset_a підмножиною set_a?:", subset_a.issubset(set_a))
print("Чи є set_b підмножиною set_a?:", set_b.issubset(set_a))
# 1. Підготовка наборів даних для експерименту

import timeit

print("\nЗАВДАННЯ 5. ДОСЛІДЖЕННЯ ЧАСОВОЇ СКЛАДНОСТІ")
print("=" * 50)

sizes = [500, 2500, 10000]

search_data = {}
search_sets = {}
search_dicts = {}
duplicate_data = {}

for size in sizes:
    values = list(range(size))

    search_data[size] = values
    search_sets[size] = set(values)
    search_dicts[size] = {value: True for value in values}

    duplicate_data[size] = [
        value % (size // 2) for value in range(size)
    ]

print("Підготовлені набори даних:")

for size in sizes:
    print(f"\nРозмір набору: {size}")
    print("Елементів у списку:", len(search_data[size]))
    print("Елементів у множині:", len(search_sets[size]))
    print("Ключів у словнику:", len(search_dicts[size]))
    print("Елементів у списку з повторами:", len(duplicate_data[size]))
    print("Унікальних елементів у списку з повторами:",
          len(set(duplicate_data[size])))
    # 2. Вимірювання швидкості пошуку елементів

print("\n5.2. Порівняння швидкості пошуку:")

search_results = {}

for size in sizes:
    target = size - 1

    list_time = timeit.repeat(
        lambda: target in search_data[size],
        number=1000,
        repeat=5
    )

    set_time = timeit.repeat(
        lambda: target in search_sets[size],
        number=1000,
        repeat=5
    )

    dict_time = timeit.repeat(
        lambda: target in search_dicts[size],
        number=1000,
        repeat=5
    )

    list_average = sum(list_time) / len(list_time) / 1000
    set_average = sum(set_time) / len(set_time) / 1000
    dict_average = sum(dict_time) / len(dict_time) / 1000

    search_results[size] = {
        "list": list_average,
        "set": set_average,
        "dict": dict_average
    }

    print(f"\nРозмір набору: {size}")
    print(f"Пошук у списку: {list_average:.8f} сек.")
    print(f"Пошук у множині: {set_average:.8f} сек.")
    print(f"Пошук у словнику: {dict_average:.8f} сек.")
    # 3. Порівняння швидкості видалення дублікатів

print("\n5.3. Порівняння швидкості видалення дублікатів:")

deduplication_results = {}

def unique_with_list(data):
    result = []

    for item in data:
        if item not in result:
            result.append(item)

    return result


def unique_with_set(data):
    result = set()

    for item in data:
        result.add(item)

    return result


for size in sizes:
    data = duplicate_data[size]

    list_time = timeit.repeat(
        lambda: unique_with_list(data),
        number=1,
        repeat=3
    )

    set_time = timeit.repeat(
        lambda: unique_with_set(data),
        number=1,
        repeat=3
    )

    list_average = sum(list_time) / len(list_time)
    set_average = sum(set_time) / len(set_time)

    deduplication_results[size] = {
        "list": list_average,
        "set": set_average
    }

    print(f"\nРозмір набору: {size}")
    print(f"Унікальні елементи через список: {list_average:.8f} сек.")
    print(f"Унікальні елементи через множину: {set_average:.8f} сек.")

    print("Кількість унікальних елементів:",
          len(unique_with_set(data)))
    # 4. Підсумкова таблиця результатів експерименту

print("\n5.4. Підсумкова таблиця результатів:")
print("=" * 105)

print(
    f"{'Розмір':>8} | "
    f"{'Пошук list':>14} | "
    f"{'Пошук set':>14} | "
    f"{'Пошук dict':>14} | "
    f"{'Унікальні list':>16} | "
    f"{'Унікальні set':>16}"
)

print("-" * 105)

for size in sizes:
    print(
        f"{size:8} | "
        f"{search_results[size]['list']:14.8f} | "
        f"{search_results[size]['set']:14.8f} | "
        f"{search_results[size]['dict']:14.8f} | "
        f"{deduplication_results[size]['list']:16.8f} | "
        f"{deduplication_results[size]['set']:16.8f}"
    )

print("\nТеоретична часова складність:")
print("Пошук у списку: O(n)")
print("Пошук у множині: O(1) у середньому")
print("Пошук у словнику: O(1) у середньому")
print("Видалення дублікатів через список: O(n^2)")
print("Видалення дублікатів через множину: O(n) у середньому")