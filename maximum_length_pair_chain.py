class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        list=sorted(pairs, key=lambda x:x[1])

        prev=list[0][1]
        i=1
        c=1
        while i<len(list):
            if list[i][0]>prev:
                c+=1
                prev=list[i][1]
            i+=1
        return c
