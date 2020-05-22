def media(value, peso):
    nota = (value/10)*peso
    return nota


notas = input().split(" ")
n1,n2,n3,n4 = notas

n1 = float(n1) 
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media_total = media(n1,2)+media(n2,3)+media(n3,4)+media(n4,1)
print("Media: %0.1f" %media_total)

if media_total >= 7:
    print("Aluno aprovado.")

elif media_total<5:
    print("Aluno reprovado.")

elif media_total >= 5 and media_total<=6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame %0.1f" %exame)
    media_nova = (media_total + exame)/2
    if media_nova > 5:
        print("Aluno aprovado.")
        print("Media final: %0.1f" %media_nova)
    else:
        print("Aluno reprovado.")
        print("Media final: %0.1f" %media_nova)








