n=input()
count=0
for i in range(len(n)):
    if n.isdigit():
        count+=1
print(count)