class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # make a hash map to count common letters of first word
        # compare first word with others
        # find minimum frequency of lettes

        common = Counter(words[0]) #count frequency of each letter in first word

        # compare first word frequencies to the rest
        for word in words: #loop through words
            w = Counter(word) #track letter frequency in word
            for char in common:
                common[char] = min(common[char], w[char])
        
        res = []
        for char in common:
            for c in range(common[char]):
                res.append(char) #add the common char depending on its frequency to result

        return res
