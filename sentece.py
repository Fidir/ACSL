gs="The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog."
for cicinal in gs:
  if cicinal == "-":
    gs=gs.replace(cicinal," ")
  if cicinal.isalpha() == False and cicinal != " ":
    gs=gs.replace(cicinal,"")
differentchars=[]

vowamount=0

Uchar=0

numotla={}
gscil=list(gs.split(" "))

lw=gscil[0]
lolw=len(lw)

#1
for findcharnum in gs:
  if findcharnum.upper() not in differentchars and findcharnum.lower() not in differentchars and findcharnum != " ":
    differentchars+=findcharnum
print("Character amount:",len(differentchars))

#2
for findvownum in gs:
  if findvownum == 'a' or findvownum == 'e' or findvownum == 'i' or findvownum == 'o' or findvownum == 'u' or findvownum == 'A' or findvownum == 'E' or findvownum == 'I' or  findvownum == 'O' or findvownum == 'U':
    vowamount+=1
print("Amount of vowels:",vowamount)

#3
for findUchar in gs:
  if findUchar.isupper():
    Uchar+=1
print("Amount of Uppercase Letters:",Uchar)

#4
for findnumol in gs:
  if findnumol.isalpha() == True:
    if (findnumol.lower() not in numotla and findnumol.upper() not in numotla):
      numotla[findnumol]=1
    elif findnumol.lower() in numotla:
      numotla[findnumol.lower()]+=1
    elif findnumol.upper() in numotla:
      numotla[findnumol.upper()]+=1
    else:
      numotla[findnumol]+=1
keylist = (list(numotla.keys()))
gcfa=keylist[0]
ga=numotla[gcfa]
for fgaoc in range(1,len(numotla)):
  cc=keylist[fgaoc]
  if numotla[cc] > ga:
    ga = numotla[cc]
    gcfa = cc
print ("Most common character:",gcfa,"Amount of times appeared:",ga)

#5
for flw in range(1,len(gscil)):
  if len(gscil[flw]) > lolw:
    lolw = len(gscil[flw])
    lw = gscil[flw]
print ("Longest word:",lw)
