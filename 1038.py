v = input().split(" ")
cod, price = v

if int(cod) == 1:
    total = float(price)*4.00
    print('Total: R$ %0.2f' %total)
    
if int(cod) == 2:
    total = float(price)*4.50
    print('Total: R$ %0.2f' %total)
    
if int(cod) == 3:
    total = float(price)*5.00
    print('Total: R$ %0.2f' %total)

if int(cod) == 4:
    total = float(price)*2.00
    print('Total: R$ %0.2f' %total)
    
if int(cod) == 5:
    total = float(price)*1.50
    print('Total: R$ %0.2f' %total)
    