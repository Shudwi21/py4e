fname = input('Enter the name of file: ')
if len(fname)<1: fname = 'financial aid.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0)+1
#print(di)
temp = list()
for k,v in di.items():
    #print(k,v)
    newt=(v,k)
    temp.append(newt)

#print('Flipped:',temp)
temp = sorted(temp,reverse=True)
#print('Sorted',temp[:5])

for v,k in temp[:7]:
    print(v,k)
