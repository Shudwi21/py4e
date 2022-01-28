fname = input('Enter the name of file: ')
if len(fname)<1: fname = 'financial aid.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)     # to find lines in file to make prog robust
    wds = lin.split()
    #print(wds)
    for w in wds:
    #    print('**',w,di.get(w,-999))
    # if the key is not there then count is zero
        #oldcount = di.get(w,0)
        #print(w,'old',oldcount)      This is SLIGHT NEW Way to add dict
        #newcount = oldcount+1
        #di[w]=newcount
        #print(w,'new',newcount)
        #if w in di:                 OLD WAY TO ADD DICT
        #    di[w] = di[w]+1
        #else:
        #    di[w]=1

        # idiom to retrive create and update counter of DICT
        di[w] = di.get(w,0)+1
        #print(w,di[w])
#print(di)

# now we want to find most common words
largest = -4
word = None
for k,v in di.items():
    #print(k,v)
    if v>largest:
        largest=v
        word = k # capture remember the key that was largest
print('Largest word is:',word)
print('Largest count of that word is:',largest)
