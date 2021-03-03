import random
from time import time
import os

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


def fixit(n, o1, o2, o3):
    """
    Turns o3 into a list in which you can add two of the elements together to get n
    :param n: The value you want to be able to add to
    :param o1: out1
    :param o2: out2
    :param o3: out3
    :return: Updated versions of all three lists
    """
    while o3[-1]*2 <= n:
        o1.append(o3[-1])
        o2.append(o3[-1])
        o3.append(o3[-1]*2)
    # Doubles until it gets to biggest value. O(lg n)
    i = -1

    while True: #O(n)
        diff = n - o3[i]
        if diff < 0:
            i -= 1
        else:
            break

    if diff!=0:
        x = binary_search_boolean(o3,diff)
        if not x:
            temp_tup = addUp(o3, diff)  # O(n lg n)
        else:
             temp_tup = (o3[x],o3[i])
        if not temp_tup:
            o1, o2, o3 = fixit(diff, o1, o2, o3)
            temp_tup = addUp(o3, diff)
        if not addUp(o3, n):
            o1.append(temp_tup[0])
            o2.append(temp_tup[1])
            o3.append(diff)
    o3sorted = list(zip(o3[2:], o2, o1))
    o3sorted.sort(key=lambda x: x[0])
    o3, o2, o1 = zip(*o3sorted)
    o1 = list(o1)
    o2 = list(o2)
    o3 = [0,1]+ list(o3)
    return [o1, o2, o3]


def get_input(file):
    inputs=[]
    with open(file,'r') as f:
        i=0
        for line in f:
            if(i!=0):
                inputs=[int(elem) for elem in list(line.split(' '))]
            i+=1
    return inputs


def write_out(fname, o1,o2):
    with open(fname,'w') as f:
        l = len(o1)
        f.write(f"{l}\n")
        for i in range(l):
            f.write(f"{o1[i]} {o2[i]}\n")


def run():
    for infile in os.listdir("files"):
        t1 = time()
        file = 'files/'+infile
        print(file)
        inputs = get_input(file)
        out1 = [1]
        out2 = [1]
        out3 = [0, 1, 2]
        # inputs = [random.randint(2, 10**9) for i in range(0,1000)]
        # inputs = [2,4,19,200,6000,8000000]
        inputs = sorted(list(dict.fromkeys(inputs)))
        for n in inputs: # n
            if not binary_search_boolean(out3, n): # lg n
                tup = addUp(out3, n) # nlogn
                if not tup:
                    out1, out2, out3 = fixit(n, out1, out2, out3) # n^2 lg n
                    tup = addUp(out3, n) # n lg n
                out1.append(tup[0])
                out2.append(tup[1])
                out3.append(n)
        print(out3)
        fname = "outputs/"+infile
        write_out(fname,out1,out2)
        print(f"time to run with sort() is {time() - t1}")

t1=time()
run()


