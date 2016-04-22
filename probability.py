from random import randint

def binary(key):
    count = 0
    low = 1
    high = 10
    while (low<= high):
        mid = int((low+high)/2)
        count = count +1
        if (mid == key):
            return count
        if (mid < key):
            low = mid +1
        else:
            high = mid - 1
        

count = 0

for num in range (1,11):
    count = binary(num)
    print ("Key " + str(num) +": "+ str(count))




