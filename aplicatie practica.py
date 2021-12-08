with open('C:\Users\User\Py\Lista_clasei.txt','r') as f:
   l=list(f)
   f.close()
print('         Nume','Prenume','Nota','Grupa 1/2',sep='\t')
for i,linie  in enumerate(l):
    print(i+1,':\t',linie,end='')
z=media=0   
for linie in x:
    campuri=linie.split()
    nota=int(campuri[2])
    z+=1
    media+=nota
s1=s2=0
print(nota,sep='\t')
print('Media a ',z, "elevi este :",media/float(z))

