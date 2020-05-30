value = input().split()
a,b,c = value

a = float(a)
b = float(b)
c = float(c)


if (b+c)>a and (a+c)>b and (a+b)>c :
    perimiter = a+b+c
    print("Perimetro = %0.1f" %perimiter)
else:
    area = (a+b)*c/2
    print("Area = %0.1f" %area)
    

