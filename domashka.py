a = int(input('Введите a =>'))
b = int(input('Введите b =>'))
c = int(input('Введите c =>'))
d = b**2 - 4*a*c
if d < 0:
    print('net korney')
else:
    if d > 0:
        x1 = (-b - d**0.5)/2*a
        x2 = (-b + d**0.5)/2*a
        print(int(x1), int(x2))
    elif d == 0:
        x = (-b - d ** 0.5)/2*a
        print(int(x))