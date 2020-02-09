s=input()
d=len(s)
if d%2!=0:
    s=s+' '
i=0
for j in range(0,d):
    print(s[i:i+3])
    i=i+3
    
