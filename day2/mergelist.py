List1=["sahad","rahees","saad","sasil"]
List2=["rahees","karthik","refai","sahad"]
merged=[]
for name in List1 + List2:
    if name not in merged:
        merged.append(name)
merged.sort()
print(merged)