def f(x):
    f = 1
    for step in range (1, x + 1):
        f = f * step
    return f

def s(x,n):
    s = 1
    for _ in range (1, n + 1):
        s *= x
    return s

x,presigion = float(input('Введите x: ')),float(input('Введите точность: '))
summ,stolb,j = 0,0,0

while abs(s(-1,j) * (s(x, j * 2) / f(2 * j))) > presigion:
    stolb = s(-1,j) * (s(x, j * 2) / f(2 * j))
    summ += stolb
    j += 1
print ('Сумма ряда =',summ)