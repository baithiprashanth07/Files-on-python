f=open('myfile.txt','w')
print('enter the text(@ at end):')
while str != '@':
    str=input()
    if (str !='@'):
        f.write(str+"\n")
f.close()
