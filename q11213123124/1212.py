file=open('file.txt','r')
f=file.readline()
t=file.readline()
file.close()
a=int(f)+int(t)
print(a)