def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    #traverse the array
    pairs = set()
    #indicator to see if we found pair
    found_pair = False
    #store positive numbers
    for i in range(len(a)):
        #print(a[i])
        #if num is > 0 store it in set
        if a[i] == None:
            return
        if a[i] > 0:
            pairs.add(a[i])
            #print(pairs)
    #go through the array
    for i in range(len(a)):
        #check to see if val of curr is in set
        if a[i] < 0:
            #then if that - value is in set
            if(-a[i]) in pairs:
                #we return the pair
                print("{}, {}".format(a[i], -a[i]))




    return pairs


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
