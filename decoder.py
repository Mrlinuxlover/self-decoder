a=str(input("Enter Your text to Decode: "))
#110-444
#230-A
#chr()
dt,cache='',''
chars=[]
i=0
while i<len(a):
    if a[i]>'4':
        if cache!='':
            chars.append(str(cache)+",n")
            cache=''
        chars.append(str(a[i:i+4])+",c")
        i+=4
    else:
        if a[i]<'5':
            cache=str(cache)+a[i]
            i+=1
            if i==len(a):
                chars.append(str(cache)+",n")
for i in chars:
    if i[-1]=='c':
        char=0
        num=i[1:-2]
        for i in range(1,4):
            char=char+int(num[-i])*5**(i-1)
        dt=dt+str(chr(char))
    else:
        if i[-1]=='n':
            char=0
            num=i[:-2]
            for i in range(1,len(num)+1):
                char=char+int(num[-i])*5**(i-1)
            dt=dt+str(char)
print(dt)
