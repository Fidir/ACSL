import string

sortedlist=[]

strinp=str(input('input here:'))
watcharryindex=int(strinp[0])-1
prev=None
countodcindex=0
for onlyletleft in strinp:
    if onlyletleft.isalpha() == False:
        strinp=strinp.replace(onlyletleft,'')

sortedlist.append(strinp[0])
dictwithindexs = {}
for makedict in strinp:
    if makedict not in dictwithindexs.keys():
        if makedict.isupper() == True:
            dictwithindexs[makedict] = string.ascii_uppercase.index(makedict)
        else:
            dictwithindexs[makedict] = string.ascii_lowercase.index(makedict)
strinp=strinp.replace(strinp[0],'',1)

for sort in strinp:
    watcharry=sortedlist[0]
    if dictwithindexs[sort] > dictwithindexs[watcharry]:
        if sortedlist.index(watcharry)+1 > len(sortedlist)-1:
            sortedlist.append(sort)
        else:
            while len(sortedlist) >= sortedlist.index(watcharry)+1:
                if dictwithindexs[sort] <= dictwithindexs[watcharry]:
                    sortedlist.insert(sortedlist.index(watcharry),sort)
                    break
                if watcharry == sortedlist[len(sortedlist)-1]:
                    sortedlist.append(sort)
                    break
                if sortedlist[sortedlist.index(watcharry)+1]==sortedlist[sortedlist.index(watcharry)]:
                    for findnextdif in range(sortedlist.index(watcharry),len(sortedlist)):
                        if sortedlist[findnextdif] != sortedlist[sortedlist.index(watcharry)]:
                            watcharry=sortedlist[findnextdif]
                            break
                else:
                    watcharry=sortedlist[sortedlist.index(watcharry)+1]
    elif dictwithindexs[sort] <= dictwithindexs[watcharry]:
        if sortedlist.index(watcharry) == 0:
            sortedlist.insert(0,sort)
        else:
            while sortedlist.index(watcharry)-1 >= 0:
                if dictwithindexs[sort] <= dictwithindexs[sortedlist[sortedlist.index(watcharry)-1]]:
                    sortedlist.insert(sortedlist.index(watcharry)-1,sort)
                    break
                if watcharry == sortedlist[0]:
                    sortedlist.insert(0,sort)
                    break
                watcharry=sortedlist[sortedlist.index(watcharry)-1]
    if len(sortedlist)-1 >= watcharryindex and sortedlist[watcharryindex] != prev:
        countodcindex+=1
        prev=sortedlist[watcharryindex]
print (countodcindex)