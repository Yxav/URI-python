'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
    e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
556

0:9:16'''


seconds = int(input())

minutes =  int (seconds/60)
seconds -= minutes * 60


hours =  int (minutes/60)
minutes -= hours * 60

print(repr(hours)+":"+repr(minutes)+":"+repr(seconds))


