shape=['A','B','C']
center=[(10,10),(50,50),(100,100)]
for i in range(0,len(shape)):
    print(shape[i],center[i])

for shape,center in zip(shape,center):
    print(shape,center)