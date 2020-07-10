def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here   
    cache ={}
    #loop through the weights
    for i in range(len(weights)):
        #store the values
        cache[weights[i]] = i
    for i in range(len(weights)):
        diff = limit-weights[i]
        if diff in cache:
            return (max(i,cache[diff]), min(i, cache[diff]))       
    return None

#get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40],6,7)