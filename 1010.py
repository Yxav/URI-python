

line1 = input().split(" ")
line2 = input().split(" ")

cod1, qtde1, val1 = line1
cod2, qtde2, val2 = line2

total = (int(qtde1) * float(val1)) + (int(qtde2) * float(val2))

print("VALOR A PAGAR: R$ %0.2f" %total)
