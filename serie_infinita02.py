n = int(input())

# Inicialize as variáveis
a, b, c = 2, 7, 3

# Imprima os primeiros 'n' termos da série
for i in range(n):
    if i % 3 == 0:
        print(f'{a}, ', end='')
        a *= 2
    elif i % 3 == 1:
        print(f'{b}, ', end='')
        b *= 3
    else:
        print(f'{c}, ', end='')
        c *= 4

# Pule uma linha após a série
print()
