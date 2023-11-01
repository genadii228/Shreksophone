def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = int(input("Введите длину первого отрезка: "))
b = int(input("Введите длину второго отрезка: "))
c = int(input("Введите длину третьего отрезка: "))

if is_triangle(a, b, c):
    print("Можно составить треугольник")
else:
    print("Нельзя составить треугольник")