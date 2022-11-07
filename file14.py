reclen=20
with open('cities.bin','rb') as f:
          n=int(input('enter record number:'))
          f.seek(reclen * (n-1))
          str = f.read(reclen)
          print(str.decode())
