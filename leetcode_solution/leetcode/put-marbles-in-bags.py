class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        _min=_max=weights[0]+weights[-1]
        consecative=[]
        for i in range(1,len(weights)):
            consecative.append(weights[i]+weights[i-1])
        consecative.sort()
        for i in range(k-1):
            _min+=consecative[i]
        consecative.reverse()
        for i in range(k-1):
            _max+=consecative[i]
        return _max-_min

        