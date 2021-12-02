with open('C:\Users\Statie-13-C100\Desktop\Lista clasei 11D.txt',encoding='utf-8-sig') as f :
    linii=f.read()
with open('C:\Users\Statie-13-C100\Desktop\Lista clasei 11D.txt',mode='rt',encoding='utf-8-sig') as f :
    linii2=list(linii)
import statistics
print ("Numele Prenumele Nota")
print(linii)
linii2=str(linii)
notele=[]
for i in linii :
    if i.isnumeric() and i!="1" and i!="0":
        notele.append(i)
    if i=="1":
        notele.append("10")
x=[int(u) for u in notele]
med=statistics.mean(x)
print("Nota medie este :",med)
with open('C:\Users\Statie-13-C100\Desktop\Limba engleza grupa 1.txt','w',encoding='utf-8-sig') as f :
    for linie in l:
        m=linie.split()
        if m[3]=='Engl1'
        f.write(linie)
    f.close()
with open('C:\Users\Statie-13-C100\Desktop\Limba engleza grupa 2.txt','w',encoding='utf-8-sig') as f :
    for linie in l:
        m=linie.split()
        if m[3]=='Engl2':
            f.write(linie)
        f.close