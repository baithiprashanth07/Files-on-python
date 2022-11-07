import emp, pickle
f=open('emp.dat','wb')
n=int(input('how many emplyees?'))
for i in range(n):
    id=int(input('enter id :'))
    name=input('enter name:')
    sal=float(input('enter salary:'))
    e=emp.emp(id,name,sal)
    pickle.dump(e,f)
f.close()
