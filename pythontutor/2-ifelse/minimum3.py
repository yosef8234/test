# Задача «Минимум из трех чисел»
# Условие
# Даны три целых числа. Выведите значение наименьшего из них.

a,b,c = int(input()),int(input()),int(input())

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)