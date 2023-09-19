def shared_bits(a, b):
    # Convert integers a and b to binary strings
    n1_b = "{0:b}".format(a)
    n2_b = "{0:b}".format(b)
    
    # Find the length of the longest binary string
    longest_length = max(len(n1_b), len(n2_b))
    
    # Pad both binary strings with leading zeros to make them equal in length
    n1_b = n1_b.rjust(longest_length, '0')
    n2_b = n2_b.rjust(longest_length, '0')
    
    # Initialize a counter to keep track of shared '1' bits
    shared_count = 0
    
    # Iterate through each bit position and check for shared '1' bits
    for i in range(longest_length):
        if n1_b[i] == '1' and n2_b[i] == '1':
            shared_count += 1
    
    # Check if there are at least 2 shared '1' bits
    return shared_count >= 2
