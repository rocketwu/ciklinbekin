# 将八音字表转为一行一字的csv

outputs = []

def outputChar(s,initial,final,tone):
    #print(s,' ',initial,' ',final, ' ',tone)
    outputs.append([s,initial,final,tone])

with open('../CikLinBekIn.md','r',encoding="utf8") as f:
    lines = f.readlines()
    lines = lines[7:] # 忽略首 6 行
    final = ''
    initial = ''
    tone = ''
    for i in range(0,len(lines)):
        currentLine = lines[i].strip()
        
        if (len(currentLine)==0):
            continue
        if (currentLine.find("##")!=-1 and (currentLine.find('###')==-1)):
            # e.g. ##春公
            final = currentLine[2:]
        elif (currentLine.find("###")!=-1):
            # e.g. ###柳
            initial = currentLine[3:]
        elif (currentLine[0] in ['0','1','2','3','4','5','6','7','8','9']):
            tone = currentLine[0]
            inQuote = False
            quoteString = ''
            for j in range(0,len(currentLine)):
                if inQuote:
                    if currentLine[j]=='`':
                        inQuote = False
                        outputChar(quoteString,initial,final,tone)
                        quoteString = ''
                    else:
                        quoteString = quoteString + currentLine[j]
                else:
                    if currentLine[j] in ['0','1','2','3','4','5','6','7','8','9','.',' ']:
                        continue
                    elif currentLine[j]=='`':
                        inQuote = True
                    else:
                        outputChar(currentLine[j],initial,final,tone)


        
            
import csv
with open('output.csv', 'w',newline='',encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(["#","漢字","聲母","韻母","調"])
    for i in range(0,len(outputs)):
        writer.writerow([i+1]+outputs[i])