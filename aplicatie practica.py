with open('C:\Users\User\Py\Lista clasei.txt','r') as f:
   l=list(f)
   f.close()
print('         Nume','Prenume','Nota','Grupa 1/2',sep='\t')
for i,linie  in enumerate(l):
    print(i+1,':\t',linie,end='')
z=media=0   
a=open('C:\Users\User\Py\Lista clasei 11 D grupa1.txt', 'w')
b=open('C:\Users\User\Py\Lista clasei 11 D grupa2.txt', 'w')
for linie in l:
    campuri=linie.split()
    nota=int(campuri[2])
    z+=1
    media+=nota
    if campuri[3]=='grupa1':
        a.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        a.write('\n')
    else:
        b.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        b.write('\n')
a.close()
b.close()
s1=s2=0
print(nota,sep='\t')
print('Media a ',z, "elevi este :",media/float(z))