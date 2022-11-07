from zipfile import *
f=ZipFile('test.zip', 'w', ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
print('test.zip file created..')
f.close()
