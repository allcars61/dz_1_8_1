# Необходимо написать программу для кулинарной книги.
#
# Список рецептов должен храниться в отдельном файле в следующем формате:
#
# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...
# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт
#
# Утка по-пекински
# 4
# Утка | 1 | шт
# Вода | 2 | л
# Мед | 3 | ст.л
# Соевый соус | 60 | мл
#
# Запеченный картофель
# 3
# Картофель | 1 | кг
# Чеснок | 3 | зубч
# Сыр гауда | 100 | г
#
# Фахитос
# 5
# Говядина | 500 | г
# Перец сладкий | 1 | шт
# Лаваш | 2 | шт
# Винный уксус | 1 | ст.л
# Помидор | 2 | шт

with open("DZ_1_8_1.txt", "rt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        number_of_ingredients = int(file.readline().strip())
        dishes = []
        for _ in range(number_of_ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dishes.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish] = dishes





