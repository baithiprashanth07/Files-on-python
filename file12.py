import emp,pickle
f=open('emp.dat','rb')
print('employees details:')
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print('end of file reached...')
        break
f.close()
