import numpy as np

def verify():
    # initialize array  of [1]
    available_values = np.ones(1)

    # output file stream
    fout = open('outputs/input_group244.txt', 'r')
    # check if file is empty, return error if so

    # verified input file stream
    with open('input.txt', 'r') as f:
        i = 0
        for line in f:
            if (i != 0):
                inputs = [int(elem) for elem in list(line.split(' '))]
            i += 1
    f.close()


    # store first input number as integer
    num_lines = fout.readline()
    num_lines.strip('\n')
    num_lines = int(num_lines)  # change num_lines to integer

    # create counter to verify above
    counter = 0

    # 2D list of all input values. Each contained array has 2 values
    input_values = [[None for _ in range(2)] for _ in range(num_lines)]

    # insert values from file into 2D array
    it = 0
    for line in fout:
        if (line == '\n'):
            continue
        if (it == num_lines):
            return False
        line.strip('\n')
        input_values[it] = line.split(' ')
        input_values[it][0] = int(input_values[it][0])
        input_values[it][1] = int(input_values[it][1])
        it += 1

    if (it != num_lines):
        return False

    for line in input_values:
        available_values = np.append(available_values, (line[0] + line[1]))


    for line in input_values:
        # check each line to make sure it is part of available_values array
        if (line[0] in available_values and line[1] in available_values):
            # if value is in inputs, remove from inputs
            if (line[0] + line[1] in inputs):
                inputs.remove(line[0]+line[1])
            # append sum of integers to array
        else:
            return False


    fout.close()


    if (len(inputs) > 0):
        return False

    return True

print(verify())
