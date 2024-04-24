class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(i) for i in str(num)]
        di={}
        for i,j in enumerate(nums):
            di[j]=i
        for i in range(len(nums)):
            for d in range(9,nums[i],-1):
                if d in di and di[d]>i:
                    nums[i],nums[di[d]]=nums[di[d]],nums[i]
                    return int("".join(map(str,nums)))
        return num
