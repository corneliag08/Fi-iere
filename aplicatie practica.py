with open('C:\Users\User\Py\.txt','r') as f:
    lista_clasei=f.readlines()
print('Nr.   Numele  Prenumele	Nota     Grupa\n',*list1)
with open('C:\Users\User\Py\.txt', 'w') as f:
    for i in lista_clasei:
        f.write(i)
for i in lista_clasei:
    lista=i.split()
    x=lista[0]+' '+lista[1]+' '+lista[2]
    media=str((float(lista[3])+float(lista[4])+float(lista[5]))/3)
    z=x+' '+media+'\n'
    with open('C:\Users\User\Py\.txt','a') as f:
        f.write(z)
with open('C:\Users\User\Py\.txt','r') as f:
    listaf=f.readlines()
print('Nr.	Numele	Prenumele	media',*listaf)
