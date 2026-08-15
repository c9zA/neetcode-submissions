class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums)==1:
            return [[nums[0]]]
        def recurse(idx):
            if idx+2==len(nums):
                return [[nums[idx], nums[idx+1]], [nums[idx+1], nums[idx]]]
            old = recurse(idx+1)
            ans = []
            for p in old:
                for i in range(len(p)+1):
                    temp = []
                    j = 0
                    added = False
                    while len(temp)<len(p)+1:
                        if j==i and not added:
                            temp.append(nums[idx])
                            added = True
                        else:
                            temp.append(p[j])
                            j+=1
                    ans.append(temp)
            return ans
        ans = recurse(0)
        return ans