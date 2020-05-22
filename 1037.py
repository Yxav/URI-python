v = float(input())
if 0<= v <=25:
    print('Intervalo [0,25]')
if 25< v <=50:
    print('Intervalo (25,50]')
if 50< v <=75:
    print('Intervalo (50,75]')
if 75< v <=100:
    print('Intervalo (75,100]')
if 0>v or v>100:
    print('Fora de intervalo')

