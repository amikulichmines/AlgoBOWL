import random

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
    while o3[-1]*2 < n:
        o1.append(o3[-1])
        o2.append(o3[-1])
        o3.append(o3[-1]*2)
    i = -1
    while True:
        diff = n - o3[i]
        if diff < 0:
            i-=1
        else:
            break
    temp_tup = addUp(o3, n)
    if not temp_tup:
        o1, o2, o3 = fixit(diff, o1, o2, o3)
        temp_tup = addUp(o3, diff)
    o1.append(temp_tup[0])
    o2.append(temp_tup[1])
    o3.append(diff)
    o1 = sorted(o1)
    o2 = sorted(o2)
    o3 = sorted(o3)
    return [o1, o2, o3]

def get_input():
    with open('input.txt','r') as f:
        i=0
        for line in f:
            if(i!=0):
                inputs=[int(elem) for elem in list(line.split(','))]
            i+=1
    return inputs


def run():
    # inputs = get_input()
    out1 = [1]
    out2 = [1]
    out3 = [1, 2]
    # inputs = [random.randint(2, 999999999) for i in range(0,500)]
    inputs = [2,4,19,200,6000,8000000]
    inputs = sorted(list(dict.fromkeys(inputs)))
    print(inputs)
    for n in inputs: # n
        if not binary_search_boolean(out3, n): # lg n
            tup = addUp(out3, n) # nlogn
            if not tup:
                out1, out2, out3 = fixit(n, out1, out2, out3) # n^2 lg n
                tup = addUp(out3, n) # n lg n
            out1.append(tup[0])
            out2.append(tup[1])
            out3.append(n)

    out3 = out3[2:]
    for line in zip(out1, out2, out3):
        print(line)


run()
