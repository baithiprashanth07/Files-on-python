import mmap, sys
print('1 to display all the entries')
print('2 to display phone number')
print('3 to modify an entry')
print('4 exit')
ch=input('enter your choice:')
if ch=='4':
    sys.exit()
with open("phonebook.dat","r+b") as f:
    mm=mmap.mmap(f.fileno(),0)
    if(ch== '1'):
        print(mm.read().decode())
    if(ch=='2'):
        name=input('enter name:')
        n=mm.find(name.encode())
        n1=n+len(name)
        ph=mm[n1:n1+10]
        print('phone no:',ph.decode())
    if(ch=='3'):
        name=input('enter name')
        n=mm.find(name.encode())
        n1=n+len(name)
        ph1=input('enter new phone number:')
        mm[n1:n1+10]=ph1.encode()
    mm.close()
