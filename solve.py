with open('input.txt','r') as f:
    i=0
    for line in f:
        if(i!=0):
            inputs=list(line)
        i+=1

print(inputs)