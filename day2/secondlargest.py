n=[1,2,3,4,5]
larg=n[0]
slarg=n[0]
for i in n:
    if i>larg:
        slarge=larg
        larg=i
    elif i !=larg and slarge:
        slarg=i
print("largest is:",larg)
print("second largest:",slarg)             