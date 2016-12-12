# Нам необходимо найти позицию наименьшего элемента в следующем
# Наборе данных: 809, 834, 477, 478, 307, 122, 96, 102, 324, 476.

counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
counts.index(min(counts)) #6

# Усложним задачу и попытаемся найти позицию двух наименьших элементов в не отсортированном списке.
# Какие возможны алгоритмы решения?

# 1. Поиск, удаление, поиск. Поиск индекса минимального элемента в списке, удаление его, снова поиск минимального, возвращаем удаленный элемент в список.
def find_two_smallest(L):
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest) # удаляем первый минимальный элемент
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    L.insert(min1, smallest) # возвращаем первый минимальный обратно
    if min1 <= min2:  # проверяем индекс второго минимального из-за смещения
        min2 += 1 # min2 = min2 + 1
    return(min1, min2) # возвращаем кортеж

find_two_smallest(counts) # (6, 7)

# 2. Сортировка, поиск минимальных, определение индексов.

def find_two_smallest2(L):
    temp_list = sorted(L) # возвращаем КОПИЮ отсортированного списка
    smallest = temp_list[0]
    next_smallest = temp_list[1]
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    return(min1, min2)

find_two_smallest2(counts) # (6, 7)

# 3. Перебор всего списка. Сравниваем каждый элемент по порядку, получаем два наименьших значения, обновляем значения, если найдены наименьшие.

def find_two_smallest3(L):
    if L[0] < L[1]:
        min1, min2 = 0, 1 # устанавливаем начальные значения
    else:
        min1, min2 = 1, 0
    for i in range(2, len(L)):
        if L[i] < L[min1]: # «первый вариант»
            min2 = min1
            min1 = i
        elif L[i] < L[min2]: # «второй вариант»
            min2 = i
    return(min1, min2)

find_two_smallest3(counts) # (6, 7)