def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    #traverse the array
    result = []
    for i in a:
        cache[i] = i
        #print(cache[i])
        #i is positive and -1 is in the table we got a pair
        if i != 0 and -i in cache:
            #print(i)
            #add that to the result - only absolute/positve nums
            result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
