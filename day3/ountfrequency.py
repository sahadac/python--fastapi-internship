sentence=("Sahad is a handsome boy")
frequency=sentence.split()
count={}
for i in frequency:
    count[i] = count.get(i, 0)+1
print(count)