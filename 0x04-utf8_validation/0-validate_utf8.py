#!/usr/bin/python3
"""
This code creates a validUTF8(data) function that validates whether a string of ints could be a valid UTF-8 encoding.
"""



from itertools import takewhile



def int_to_bits(nums):
    """
    This converts integers to bitds
    """
    for num in nums:
        bits = []
        mask = 1 << 8
        while mask:
            mask >>= 1
            bits.append(bool(num & mask))
        yield bits

def validUTF8(data):
    """
    Takes in a list of intsif the list is a valid UTF-8 encoding, it returns true, else returns false
    Args:
        data : list of ints possibly representing UTF-8 encoding
    Return:
        bool : True or False
    """
    bits = int_to_bits(data)
    for byte in bits:
        # if a single byte char is valid. continue
        if byte[0] == 0:
            continue

        # if the byte is a multi-byte char
        ones = sum(takewhile(bool, byte))
        if ones <= 1:
            return False
        if ones >= 4:
            return False

        for _ in range(ones - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True