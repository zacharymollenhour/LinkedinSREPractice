from collections import defaultdict
class WordDistance(object):
    
    def __init__(self,words):
        self.words = words
        self.locations = defaultdict(list)

        #Map words to their locations (can be multiple)
        for i,w in enumerate(words):
            self.locations[w].append(i)
        
    def shortestDistance(self, word1, word2):
        #Get the occurances of the given words
        word1locations = self.locations[word1]
        word2locations = self.locations[word2]
      
        #Pointer Variables
        wL1 = 0
        wL2 = 0
        distance = 0
        #Set a variable with an infinitely large value
        distance = float('inf')
        while wL1 < len(word1locations) and wL2 < len(word2locations):
            distance = min(distance, abs(word1locations[wL1] - word2locations[wL2]))
            if word1locations[wL1] < word2locations[wL2]:
                wL1 += 1
            else:
                wL2 += 1
        return distance
        

        

wordsList = ["practice", "makes", "perfect", "coding", "makes"]
wordDistanceObject = WordDistance(wordsList)
word1 = "makes"
word2 = "coding"
testanswer = wordDistanceObject.shortestDistance(word1, word2)
print(testanswer)