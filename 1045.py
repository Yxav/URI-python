x = input().split()
x = list(map(float,x))
a, b, c = sorted(x)[::-1]

go = True

if a>=b+c:
    print("NAO FORMA TRIANGULO")
    go = False


if a**2 == ((b**2)+(c**2)) and go:
    print("TRIANGULO RETANGULO")

if a**2 > ((b**2)+(c**2)) and go:
    print("TRIANGULO OBTUSANGULO")

if a**2 < ((b**2)+(c**2)) and go:
    print("TRIANGULO ACUTANGULO")

if a==b and a==c and b==c and go:
    print("TRIANGULO EQUILATERO")

if (a==b or b==c) and not (a==b and b==c) and go :
    print("TRIANGULO ISOSCELES")

