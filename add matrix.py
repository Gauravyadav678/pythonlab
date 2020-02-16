a=[[1,2,5],
   [2,3,5],
   [1,2,8]]
b=[[2,3,5],
   [2,3,5],
   [3,4,5]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]+b[i][j]
for r in c:
    print(r)

