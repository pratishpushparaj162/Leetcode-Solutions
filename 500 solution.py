class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letters = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]

        return [word for word in words if any(set(word.lower()) <= letter for letter in letters)]
        
