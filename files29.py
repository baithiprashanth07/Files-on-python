import os
for dirpath,dirnames,filenames in os.walk('.'):
    print('current path:',dirpath)
    print('Directories:',dirnames)
    print('Files:',filenames)
    print()
