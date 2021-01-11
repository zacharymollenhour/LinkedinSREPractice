#Leetcode Reverse Integer
#Given a 32-bit signed int, reverse digits of an int
#Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:

def reverseInt(x):
    xlist = [int(item) for item in reversed(str(x))]
    return xlist

x = 123
print(reverseInt(x))