class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        result = []

        
        for i in range(word_len):
            left = i
            current_count = {}
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1

                   
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    
                    if count == len(words):
                        result.append(left)

                else:
                   
                    current_count.clear()
                    count = 0
                    left = j + word_len

        return result
