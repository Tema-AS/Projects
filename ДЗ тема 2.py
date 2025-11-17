# Задаём переменную со словом
word = 'test'  # Можно заменить на любое другое слово

# Определяем длину слова
length = len(word)

# Проверяем, чётное ли количество букв в слове
if length % 2 == 0:
    # Если чётное — берём две средние буквы
    middle_index = length // 2
    result = word[middle_index - 1:middle_index + 1]
else:
    # Если нечётное — берём одну среднюю букву
    middle_index = length // 2
    result = word[middle_index]

# Выводим результат
print(result)
