def addUp(s, x):
    for element in s:
        x = binary_search_boolean(s, x-element)
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

with open('input.txt','r') as f:
    i=0
    for line in f:
        if(i!=0):
            inputs=[int(elem) for elem in list(line.split(','))]
        i+=1


out1 = [1]
out2 = [1]
out3 = [2]
i=0 #outputIdx
inputIdx=0
while inputIdx!=len(inputs):
    n = inputs[inputIdx]
    if out3[i]==n:
        inputIdx+=1

    elif 2*out3[i]>n:
        dif=2*out3[i]-n
        x=binary_search_boolean([1]+out3,dif)
        if x:
            i+=1
            out3.append(out3[x]+out3[i])
            out2.append(out3[i])
            out1.append(out3[x])
        else:
            while not addUp([1]+out3,dif):


    elif 2*out3[i]<n:
        out3.append(2*out3[i])
        out1.append(out3[i])
        out2.append(out3[i])
        i+=1
        inputIdx+=1

