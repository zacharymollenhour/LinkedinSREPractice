# caesar.py
""" Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.
"""
import json
import string

def cipherFunction(message, shift_num=4):
    #Get all lowercase alphabet letters
    lowerAlphabet = string.ascii_lowercase

    #Create copy but with the letters shifted by given amount
    #Must put the shift_num: first so it wraps around in the correct order
    shiftAlphabet = lowerAlphabet[shift_num:] + lowerAlphabet[:shift_num]
    
    #Translate Table from string package
    translatetable = str.maketrans(lowerAlphabet, shiftAlphabet)
    return message.translate(translatetable)

message = "abcd xyz"
shift_num = 4
answer = ""
answer = cipherFunction(message, shift_num)
print(answer)