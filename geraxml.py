import xlsxwriter

i=0
aux = ""
xml = ''
with open('pon.txt', "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if i == 21:
            i = 0  
        if (i == 0) or (i == 1) or (i == 5) or (i == 9) or (i == 16) :
            if i==1:
                xml += ' 0.00\n'
            aux = str(linha)
            aux = aux[1:-2]
            #aux = aux.replace('\n'+"", '')
            xml += aux+"\n"
        
        i+=1
f = open("ponxml.txt", "w")
f.write(xml)
f.close()


workbook = xlsxwriter.Workbook('PON-8.xlsx')
worksheet = workbook.add_worksheet("Minha Planilha")
worksheet.write('A1', 'ID')
worksheet.write('B1', 'Potência')
worksheet.write('C1', 'Nome')
worksheet.write('D1', 'CTO')
worksheet.write('E1', 'Serial')
worksheet.write('F1', 'Bairro')
j=['A','B','C','D','E','F']
i=0
cont=0
texto = []
linhas = 2
with open('ponxml.txt', "r") as arquivo:
    for linha in arquivo:
        if cont == 6:
            cont=0
            linhas +=1
        linha = linha.replace('\n'+"", '')
        print("linhas : "+str(linha))
        worksheet.write(j[cont]+str(linhas), linha)
        i+=1
        cont +=1
    
workbook.close()