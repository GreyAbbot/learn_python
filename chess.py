print("Введите шахматную фигуру.")
chess_piece = input().lower()
# print("Введите начальные координаты фигуры от 1 до 8 через пробел.")
# x1, y1 = map(int, input().split())
# print("Введите конечные координаты фигуры от 1 до 8 через пробел.")
# x2, y2 = map(int, input().split())
print("введите начальную координату фигуры по оси x1 от 1 до 8: ")
x1 = int(input())
print("введите начальную координату фигуры по оси y1 от 1 до 8: ")
y1 = int(input())
print("введите конечную координату фигуры по оси x2 от 1 до 8: ")
x2 = int(input())
print("введите конечную координату фигуры по оси y2 от 1 до 8: ")
y2 = int(input())
check = False
if chess_piece in ["король", "king"]:
    # проверка на перемещение в любую сторону на одну клетку
    if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
        check = True
elif chess_piece in ["ферзь", "queen"]:
    # проверка на перемещение по горизонтали или вертикали, перемещение по диагонали
    if abs(x2 - x1) == abs(y2 - y1) or x1 == x2 or y1 == y2:
        check = True
elif chess_piece in ["ладья", "rook"]:
    # проверка на перемещение по горизонтали или вертикали
    if x2 == x1 or y2 == y1:
        check = True
elif chess_piece in ["слон", "bishop"]:
    # проверка на перемещение по диагонали
    if abs(x2 - x1) == abs(y2 - y1):
        check = True
elif chess_piece in ["конь", "knight"]:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # проверка на перемещение буквой "Г"
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        check = True
elif chess_piece in ["пешка", "pawn"]:
    print("Цвет фигуры белый? (введите y - если да, n - если нет)")
    isWhite = True if input() == "y" else False
    if isWhite:
        # Проверка на возможность сделать первый ход на 2 клетки белой пешкой
        if (x1 == 2 and y1 <= 8) and ((x2 == 3 or x2 == 4) and y1 <= 8):
            check = True
        # Проверка на перемещение на одну клетку вперед белой пешкой
        elif (x1 > 2 and y1 <= 8) and (x2 - x1 == 1 and y2 - y1 == 0):
            check = True
    else:
        # Проверка на возможность сделать первый ход на 2 клетки черной пешкой
        if (x1 == 7 and y1 <= 8) and ((x2 == 6 or x2 == 5) and y1 <= 8):
            check = True
        # Проверка на перемещение на одну клетку вперед черной пешкой
        elif (x1 < 7 and y1 <= 8) and (abs(x2 - x1) == 1 and y2 - y1 == 0):
            check = True
else:
    pass
print("Ход возможен." if check else "Ход не возможен.")
