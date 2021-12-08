with open('C:\Users\User\Py\.txt','r') as f:
    list1=f.readlines()
print('Nr.   Numele  Prenumele	Nota     Grupa\n',*list1)
with open('C:\Users\User\Py\.txt', 'w') as f:
    for i in list1:
        f.write(i)
for i in list1:
    list2=i.split()
    x=list2[0]+' '+list2[1]+' '+list2[2]
    media=str((float(list2[3])+float(list2[4])+float(list2[5]))/3)
    y=x+' '+media+'\n'
    with open('C:\Users\User\Py\.txt','a') as f:
        f.write(y)
with open('C:\Users\User\Py\.txt','r') as f:
    list3=f.readlines()
print('Nr.	Numele	Prenumele	media',*list3)
