import random as rand
import matplotlib.pyplot as plt
import numpy as np

def addUp(s, diff):
    for element in s:
        x = binary_search_boolean(s, diff-element)
        if x:
            return (s[x],element)
    return False
    # Complexity works out to O(nlog(n)) + O(nlog(n)), so just O(nlog(n))

def binary_search_boolean(arr, x):
    # Binary search
    # Modified code from GeeksForGeeks.
    # Source: https://www.geeksforgeeks.org/python-program-for-binary-search/
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return False

def primes2(N):
    isprime = [True] * N
    prime = []
    SPF = [None] * N
    # 0 and 1 are not prime
    isprime[0] = isprime[1] = False

    # Fill rest of the entries
    for i in range(2, N):
        if isprime[i] == True:
            prime.append(i)
            SPF[i] = i
        j = 0
        while (j < len(prime) and
               i * prime[j] < N and
                   prime[j] <= SPF[i]):
            isprime[i * prime[j]] = False
            # put smallest prime factor of i*prime[j]
            SPF[i * prime[j]] = prime[j]
            j += 1
    return prime

def digits(string):
    sum=0
    for i in string:
        sum=sum+int(i)
    return sum

with open('input.txt','w') as f:

    ### BEST SO FAR 3005
    primes = primes2(int(1e6))
    rand.shuffle(primes)
    s=[2]
    i=0
    while len(s) < 1000:
        n = s[i] + primes[i] * digits(str(s[i]))
        if addUp(s, n) or addUp(s, n+s[rand.randint(0,len(s)-1)]):
            print("caught one!")
        else:
            print("n")
            s.append(n)
        i+=1
    s=list(dict.fromkeys([int(e/22)+2 for e in s]))
    s.sort()
    #
    # o3 = [1,2]
    # n=3
    # s = []
    # while len(s)<10000:
    #     if n in o3:
    #         n+=1
    #     else:
    #         s.append(n+max(o3))
    #         o3.append(n+max(o3))
    #         o3.append(n)
    #         n+=1
    # s = [rand.randint(1,5)*s[20*i] for i in range(100)]+[rand.randint(1, 1e9) for i in range(900)]
    # s.sort()


    f.write(str(len(s)))
    f.write('\n')
    f.write(' '.join([str(elem) for elem in s]) )
    f.write('\n')
    plt.plot(range(len(s)),s)
    plt.show()