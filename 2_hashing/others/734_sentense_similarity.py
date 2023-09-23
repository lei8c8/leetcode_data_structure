from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False
        
        if not similarPairs:
            return sentence1 == sentence2
        
        lookup = defaultdict(set)
        for x, y in similarPairs:
            lookup[x].add(y)
            lookup[y].add(x)

        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and sentence2[i] not in lookup[sentence1[i]]:
                return False

        return True