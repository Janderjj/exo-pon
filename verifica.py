import csv

i=0
aux = ""
lista = ' ID -------- NOME ----------- CTO ----------- SN -----------BAIRRO \n'
with open('pon.txt', "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if i == 21:
            i = 0  
            lista = lista + '\n'
        if (i == 0) or (i == 1) or (i == 5) or (i == 9) or (i == 16) :
            aux = str(linha)
            aux = aux.replace('\n'+"", '')

            lista = lista + aux + '-'
            print(i," = ",aux)
       
        i+=1
f = open("pon-1-6.txt", "w")
f.write(lista)
f.close()
#