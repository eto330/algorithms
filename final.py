x=[-100,89,45,68,90,29,-1,45]
###### THIS IS THE MAI FUCTION OF THE ALGORITHMS
def finding(j,item):
    while True:
        if x[j]> item:
            x.pop(j+1)
            x.insert(j+1,x[j])
            j= j-1
        if j == -1:
            x.pop(j+1)
            x.insert(j+1,item)
            break
        elif x[j]<= item:
             x.pop(j+1)
             x.insert(j+1,item)
             break
         
for i in range(1,len(x)):
    j = i-1
    item = x[i]
    if x[j] > item:
        finding(j,item)
    elif x[j] <= item:
       finding(j,item)
print(x)
