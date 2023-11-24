import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_dict = {k: True for k in banned}
        counter = collections.defaultdict(int)
        for word in [x for x in re.sub('[^\w]', ' ', paragraph).lower().split() if x not in banned_dict]:
            counter[word] = counter[word] + 1
        return sorted(counter.items(), key=lambda item: item[1])[-1][0]
        