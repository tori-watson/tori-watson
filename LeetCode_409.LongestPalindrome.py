class Solution:
    def longestPalindrome(self, s: str) -> int:
        #track each letters number of occurences in dictionary 
        #loop through dictionary values  (occurences) and add value to lenght
        #if even, add full value to length
        #if odd, add full value - 1
        #return result
        
        #dictionary of letter occurence
        dict = {}
        length = 0 #result of s length

        #input occurence count into dictionary
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        
        odd = 0
        #find length of palindrome
        for occur in dict.values():
            if (occur > 1) and (occur % 2 == 0): #if occurence value is greater than 1 and even
                length += occur
            else: #if occurence value is odd
                length += occur - 1 #add odd occurence value minus 1 because there can only be 1 odd letter in palindrome
                odd += 1
        if odd:#if odd occurence value > 1, add 1 to result --> "length"
            length += 1

        return length
