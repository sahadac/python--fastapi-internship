mark=[] 
print("enter 5 students:")
for i in range(5):
    num=int(input(f"enter a number{i+1}:"))
    mark.append(num)
highest=max(mark)
print(f"highest mark:",highest)
lowest=min(mark)
print(f"lowest mark:",lowest)
average=sum(mark)/len(mark)
print(f"Average mark:",average)
passed=0
for num in mark:
    if num >= 40:
        passed +=1
print("number of students passed:",passed)

    


