#Leetcode Longest Substring without repeating characters
# Given a string s, find the length of the longest substring
# without repeating characters

def longestWithHash(s):
    stringList = {}
    n = len(s)
    substringlength = 0
    iterationValue = 0
    for j in range(n):
        if s[j] in stringList:
            iterationValue=max(stringList[s[j]], iterationValue)
        substringlength = max(substringlength, j - iterationValue + 1)
        stringList[s[j]] = j + 1
    return substringlength
    


s = "abcabcbb"     
print(longestWithHash(s))