import  os
reclen=20
size=os.path.getsize('cities.bin')
print('size of file={} bytes'.format(size))
n=int(size/reclen)
print('No.of records={}'.format(n))
with open('cities.bin','rb')as f:
    name = input('enter city name:')
    name=name.encode()
    newname=input('enter new name:')
    ln=len(newname)
    newname=newname+ (20-ln)*' '
    newname=newname.encode()
    position=0
    found=False
    for i in range(n):
        f.seek(position)
        str=f.read(20)
        if name in str:
            print('updated record no:',(i+1))
            found = True
            f.seek(-20,1)
            f.write(newname)
        position+=reclen
    if not found:
        print('city not found')
            
        
