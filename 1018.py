
value = int(input())
val = value
cem = cinq = vinte = dez = cinc = dois = um = 0

if int(value/100) >= 1:
    cem = int(value/100)
    value -= cem*100

if int(value/50) >= 1:
    cinq = int(value/50)
    value -= cinq*50

if int(value/20) >= 1:
    vinte = int(value/20)
    value -= vinte*20

if int(value/10) >= 1:
    dez = int(value/10)
    value -= dez*10

if int(value/5) >= 1:
    cinc = int(value/5)
    value -= cinc*5    

if int(value/2) >= 1:
    dois = int(value/2)
    value -= dois*2

if int(value/1) >= 1:
    um = int(value/1)
    value -= um*1

print("%d" % val)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinq)
print("%d nota(s) de R$ 20,00" % vinte)
print("%d nota(s) de R$ 10,00" % dez)
print("%d nota(s) de R$ 5,00" % cinc)
print("%d nota(s) de R$ 2,00" % dois)
print("%d nota(s) de R$ 1,00" % um)
