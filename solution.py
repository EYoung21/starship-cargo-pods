# Read input from stdin
# Example: n = int(input())
# Example: arr = list(map(int, input().split()))

# m groups
# each group has pods of numbers

# m arrays of same size 

def findlargestindex(dictionary):
    largest_index = None
    largest = -float("inf")
    for i, arr in dictionary.items():
        # print(type(largest))
        if int(arr[1]) > largest:
            largest = int(arr[1])
            largest_index = i

    return largest_index



nmarr = input().split(" ")

# print(nmarr)

n = int(nmarr[0])
m = int(nmarr[1])

# print("n: " + str(n))
# print("m: " + str(m))

# next m lines contains ai and bi
# ai is how many pods, bi is how many crustas 

# n is how many individual ones you can take

indexto_quant_value = dict()

for i in range(m): #because m cargo groups
    indexto_quant_value[i] = input().split(" ")
    indexto_quant_value[i][0] = int(indexto_quant_value[i][0])
    indexto_quant_value[i][1] = int(indexto_quant_value[i][1])

# first is count

# second is amount
    

total = 0

while n > 0:
    # print(n)
    largest_index = findlargestindex(indexto_quant_value)
    if largest_index == None:
        break
    elif indexto_quant_value[largest_index][0] == 0:
        del indexto_quant_value[largest_index]
    else:
        howmany = min(int(indexto_quant_value[largest_index][0]), n)
        total += howmany * int(indexto_quant_value[largest_index][1])
        indexto_quant_value[largest_index][0] -= howmany
        n -= howmany

print(total)

