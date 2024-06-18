imagePixel=[
    [0,0],[1,0],[2,0],[3,0],
    [0,1],[1,1],[2,1],[3,1],
    [0,2],[1,2],[2,2],[3,2],
    [0,3],[1,3],[2,3],[2,3],
]
#shift X axis 3 pixel to the right
for i in range(0,len(imagePixel)):
    imagePixel[i][0]+=3
print(imagePixel)
#shift Y axis 2 pixels downward
for i in range(0,len(imagePixel)):
    imagePixel[i][1]+=2
print(imagePixel)