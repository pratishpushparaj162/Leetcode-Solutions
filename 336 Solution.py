from typing import List

class TrieNode:
    """Node of a Trie structure."""
    def __init__(self):
        self.word_id = None  # Stores the ID of the word ending at this node
        self.children = {}   # Maps character to next TrieNode

    def __str__(self):
        return f"{self.word_id}: {self.children}"

    __repr__ = __str__


class Trie:
    """Trie data structure for storing words and checking prefix-based palindrome pairs."""
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str, word_id: int):
        """Adds a word to the Trie, associating it with a word ID."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_id = word_id

    def get_palindrome_matches(self, word: str, flags: List[bool]) -> List[int]:
        """
        Checks for words in the Trie that form palindrome pairs with `word`.
        `flags[i]` indicates whether the suffix starting at i can form a palindrome.
        """
        matches = []
        node = self.root
        for i, char in enumerate(word):
            # If we reached a word in the trie, check if the remaining suffix forms a palindrome
            if node.word_id is not None and flags[i]:
                matches.append(node.word_id)
            if char in node.children:
                node = node.children[char]
            else:
                return matches
        # Check at the end of traversal
        if node.word_id is not None:
            matches.append(node.word_id)
        return matches

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Finds all pairs of word indices (i, j) such that words[i] + words[j] forms a palindrome.
        """
        def flags_from_manacher(p):
            """Convert Manacher output to flags indicating which suffixes form palindromes."""
            if len(p) <= 0:
                return []
            flags = []
            for i in range(0, len(p), 2):
                center = i // 2
                flags.append(p[center] >= center)
            return flags[::-1] # Reverse to match suffix indexing
        
        def manacher_helper(line, idx, offset):
            l = idx - offset
            r = idx + offset
            while l >= 0 and r < len(line) and line[l] == line[r]:
                    l -= 1
                    r += 1
            return l + 1, r - 1

        def manacher(string):
            """Manacher's algorithm to find longest palindromic substring lengths centered at each character."""
            if len(string) == 0:
                return []
            # Transform string to insert separators to handle even-length palindromes
            line = []
            for c in string:
                line.append(c)
                line.append("*")
            line.pop() # Remove last extra separator

            p = [0] * len(line)
            left = right = center = 0
            for i in range(len(line)):
                offset = 0
                if right > i:
                    mirror = center - (i - center)
                    border = i + p[mirror]
                    if border < right:
                        p[i] = p[mirror]
                        continue
                    offset = right - i
                center = i
                left, right = manacher_helper(line, i, offset)
                p[i] = (right - left) // 2
            return p
        
        # Set to store resulting palindrome pairs
        pairs = set()

        # Initialize Tries for direct and reversed words
        direct_trie = Trie()
        reversed_trie = Trie()
        for id, word in enumerate(words):
            direct_trie.add_word(word, id)
            reversed_trie.add_word(word[::-1], id)

        # Check each word against both tries
        for id, word in enumerate(words):
            p = manacher(word)
            flags_direct = flags_from_manacher(p[::-1])
            res = reversed_trie.get_palindrome_matches(word, flags_direct)
            if len(res) > 0:
                for r in res:
                    if r != id:
                        pairs.add((id, r))

            flags_reversed = flags_from_manacher(p)
            res = direct_trie.get_palindrome_matches(word[::-1], flags_reversed)
            if len(res) > 0:
                for r in res:
                    if r != id:
                        pairs.add((r, id))
        res = [[a, b] for a, b in pairs]
        return res
