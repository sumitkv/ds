a=list(input())
d='0'
c=0
for i in a:
    #if i=='-':
        #c+=1
    if i!='-' and i!=',':
        d=d+i
e=d.lstrip('0')
c=a.count('-')
if c%2==0:
    print(e)
else:
    print('-'+e)
