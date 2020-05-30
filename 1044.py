value = input().split()
a, b = value

a = int(a)
b = int(b)

if a>b:
    if a%b == 0:
        print("Sao Multiplos")
    else:
        print("Nao Sao Multiplos")
if b>a:
    if b%a == 0:
        print("Sao Multiplos")
    else:
        print("Nao Sao Multiplos")
        

if a==b:
    print("Sao multiplos")


    