# Algorithm 1: Connecting Pairs of Persons 
# Matthew Amora
# Algorithm implementation using python


# This algorithm returns the minimum number of swaps to seat n couples
# row parameter is a list of numbers, each number representing an individual 
# row must be less than or equal to 60 elements and it must contain an even amount of elements
def connecting_pairs (row): 

    # Calculating number of couples (n) and checks that n <= 30
    n = len(row) // 2
    if n > 30:
        return

    # Initialize swaps variable to be returned at the end of this function
    swaps = 0

    # Create an empty dictionary to map a persons ID to their seat
    # The key would be the persons ID or row[index number] 
    # The value would be the index in row or seat number
    # using a dictionary for easy lookups
    id_map = {}  

    # Populate id_map using row with a for loop
    # row[i] is the key and i is the value
    for i in range(len(row)):
        id_map[row[i]] = i

    # Looping through row in increments two to find the pairs of each person
    # also check if the pair is already sitting next to each other
    for i in range(0, len(row), 2):

        if row[i] % 2 == 0:
            pair = row[i] + 1
        else:
            pair = row[i] - 1

        if row[i+1] != pair:
            pair_seat = id_map[pair]  # find the index of the persons actual pair
            row[i+1], row[pair_seat] = row[pair_seat], row[i+1]  # swaps seats 
            swaps += 1  # adds to number of swaps 
            id_map[row[i+1]] = i+1 # update the dictionary with the swaps 
            id_map[row[pair_seat]] = pair_seat # update the dictionary with the swaps

    return swaps 

# tests with input
print(connecting_pairs([0,2,1,3]))  # returns 1
print(connecting_pairs([3,2,0,1]))  # returns 0
print(connecting_pairs([3,2,0,1,4,10,6,5,9,7,8,11])) # returns 3





