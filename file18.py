with open("phonebook.dat","wb")as f:
    n= int(input('how many entries?'))
    for i in range(n):
        name=input('enter name:')
        phone=input('enter phone no:')
        name=name.encode()
        phone=phone.encode()
        f.write(name+phone)
