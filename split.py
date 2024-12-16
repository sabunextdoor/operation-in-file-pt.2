with open('sample txt','w') as f:
    f.write("This is a replaced line")
f.close()

with open('sample txt','r') as f:
    lines=f.readlines()
    for x in lines:
        data=x.split()
        print(data)
f.close()