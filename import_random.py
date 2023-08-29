

N=4386709
P=len(str(N))-1
D=2

lint=[]
lint[:0]=str(N)
dig = (lint[P])

if int(dig) < 5:
  resp=str(int(dig)+D)
  (lint[P])=resp[len(resp)-1]
elif int(dig) > 4:
  (lint[P])=str(abs(int(dig)-D))[0]
if P<(len(str(N))-1):
  for eachdigbe in range(P+1,len(str(N))):
    lint[eachdigbe]='0'
print(lint)
