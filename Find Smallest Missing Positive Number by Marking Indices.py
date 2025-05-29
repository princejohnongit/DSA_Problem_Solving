# Python program to find the smallest positive missing number
# by marking indices

# Function for finding the first missing positive number
def missingNumber(arr):
    n = len(arr)
    flag = False

    # Pass 1: Check if 1 is present in array
    for i in range(n):
        if arr[i] == 1:
            flag = True
            break

    # If 1 is not present, it's the smallest missing positive
    if not flag:
        return 1

    # Pass 2: Change out-of-range (<=0 or >n) values to 1
    # This prepares the array so all relevant elements are within [1, n]
    # (after processing, 1 will stand for itself or original out-of-range numbers)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1

    # Pass 3: Mark the occurrence of numbers
    # For each number 'x' (which is now guaranteed to be in [1, n]),
    # go to index (x-1) and add 'n' to the element there.
    # We use (arr[i] - 1) % n to handle cases where arr[i] might have
    # already been incremented by 'n' in a previous step,
    # effectively getting its original "true" index.
    for i in range(n):
        arr[(arr[i] - 1) % n] += n

    # Pass 4: Find the first index where the value is <= n
    # If arr[i] is still <= n, it means 'i+1' was never encountered
    # (because its corresponding index was never incremented by 'n').
    for i in range(n):
        if arr[i] <= n:
            return i + 1

    # If all numbers from 1 to n are present (all elements are > n)
    # then the missing number is n + 1
    return n + 1
        
        
