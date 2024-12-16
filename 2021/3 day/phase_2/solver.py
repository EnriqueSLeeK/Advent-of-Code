with open("input", "r") as f:
    codes = f.readlines()

#Copies of the codes
oxygen = codes.copy()
carbon = codes.copy()

#Return a tuple with the least and the
#most frequent digit
def find_most_freq(arr, index):
    count = [0, 0]
    for line in arr:
        count[int(line[index])] += 1
    print(count)
    if (count[0] < count[1]):
        return ("1", "0")
    elif (count[0] > count[1]):
        return ("0", "1")
    else:
        return ("2", "2")

#Filter func
def filter(arr, index, default_code, mode):
    common, rare = find_most_freq(arr, index)
    if (common == rare):
        common = default_code
        rare = default_code
    for line in arr:
        if (mode == 1):
            for l in arr:
                if (l[index] != common):
                    arr.remove(l)

        elif (mode == 0):
            for l in arr:
                if (l[index] != rare):
                    arr.remove(l)

#loop to pass indexes of elements
def filter_loop(arr, default_code, mode):
        for i in range(len(arr[0].replace("\n", ""))):
            if (len(arr) == 1):
                break
            filter(arr, i, default_code, mode)
            print(i)

#Oxygen
filter_loop(oxygen, "1", 1)

#Cargon
filter_loop(carbon, "0", 0)

#Result
print(int(oxygen[0], 2) * int(carbon[0], 2))
