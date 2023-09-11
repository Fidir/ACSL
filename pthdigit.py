n=int(input("Input int"))
digs = {}
lgdig=len(str(n))-1
for placeholder in str(n):
    digs[lgdig] = placeholder
    lgdig-=1
p=int(input("Input pth digit"))-1
pasb = int(digs[p])
p2 = p
while p < len(str(n))-1 or p2 > 0:
    if p < len(str(n))-1:
        p+=1
        if int(digs[p]) + pasb > 9:
            digs[p] = str(int(digs[p]) + pasb - 10)
        else:
            digs[p] = str(int(digs[p]) + pasb)
    if p2 > 0:
        p2-=1
        digs[p2] = str(abs(int(digs[p2])-pasb))

whnum=''
for cwn in digs.values():
    whnum+=cwn
print ("Final num:",whnum)