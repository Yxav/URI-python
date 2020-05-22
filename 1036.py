import math
num = input().split(" ")
a,b,c = num

x=(float(b)**2)-(4*float(a)*float(c))

if x<0 or float(a)==0:
    print("Impossível calcular")
else:
    x=math.sqrt(x)
    x1=(-float(b)+x)/(2*float(a))
    x2=(-float(b)-x)/(2*float(a))
    print("R1 = %0.5f" %x1)
    print("R2 = %0.5f" %x2)

# Don't accepted by the URI, but it's works