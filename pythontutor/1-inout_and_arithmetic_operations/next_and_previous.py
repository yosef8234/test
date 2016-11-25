# Задача «Следующее и предыдущее»
# Условие
# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
# Во всех задачах считывайте входные данные через input() и выводите ответ через print().

n = int(input())
nn = n + 1
pn = n - 1
print("The next number for the number " + str(n) + " is " + str(nn))
print("The previous number for the number " + str(n) + " is " + str(pn))