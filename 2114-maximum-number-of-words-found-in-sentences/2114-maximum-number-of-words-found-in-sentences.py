class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_count = 0
        for sentence in sentences:
            count = len(sentence.split())

            if count > max_count:
                max_count = count
        return max_count        