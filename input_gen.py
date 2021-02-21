import random as rand
import matplotlib.pyplot as plt

num_lists=8
list_len=10
with open('input.txt','w') as f:
    for l in range(num_lists):
        s=[rand.randint(2,10)]
        i=0
        while(s[i]<=10**9):
            rstart=rand.randint(0,s[i])+2
            rend=rand.randint(rstart,rstart*10 + s[i])
            s.append(s[i]+rand.randint(rstart,rend))
            i+=1
        f.write(','.join([str(elem) for elem in s]) )
        f.write('\n')
    plt.plot(range(len(s)),s)
    plt.show()