inputlist=[]
l1=[]
outputlist=[]
print("Enter Elements of array")
numbers = input().split()
for num in numbers:
    l1.append(int(num))
    if len(l1)==2:
        inputlist.append(l1)
        l1=[]

for pair in inputlist:
    a=pair[0]
    b=pair[1]
    if 1.8<=(a/b)<=1.9:
        outputlist.append(pair)

if len(outputlist)!=0: 
    print("output:")
    print("Eureka",end=" ")
    for pair in outputlist:
        print(pair,end=" ")