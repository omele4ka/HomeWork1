# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти расстояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите координату Х первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))

x2 = int(input('Введите координату Х второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))

distance = round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 2)
print(f'Расстояние между заданными точками {distance}')
