class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        print(words)
        result=set()
        for i,s in enumerate(words):
            for word in words[i+1:]:
                if s in word :
                    result.add(s)
                    break
        return list(result)