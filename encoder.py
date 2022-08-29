import random as rn
import datetime as dt
import base64
text=str(input('\nEnter your text: '))
text = base64.b64encode(text.encode("ascii")).decode("ascii")
code=''
for i in range(0,len(text)):
    a=ord(text[i])
    b=''
    while a//5>=0:
        b=str(a%5)+b
        if a//5==0:
            break
        a=a//5
    b=int(b)
    code=code+str(rn.randint(5,9))+str(b)
print()
how=str(input('[0] - save in file\n[1] - show as text\nYour chioce: '))
if how=='0':
	sure=str(input('\n[Y/N] - Are you sure you want save it?: '))
	if sure=='Y' or sure=='y':
		f=open('encoded.txt','w')
		f.write(code)
		f.close()
		print('\nSaved!\n')
	else:
		print('\nCanceled!\n')
if how=='1':
	print('\nEncoded text: '+code+'\n')
