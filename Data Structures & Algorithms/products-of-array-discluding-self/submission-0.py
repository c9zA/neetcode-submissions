class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = []
        zero = 0
        zeroProduct = 1
        for num in nums:
            if num == 0:
                zero += 1
                product = 0
                continue
            product *= num
            zeroProduct *= num
        if zero>1:
            return [0]*len(nums)
        for num in nums:
            if num == 0:
                ans.append(zeroProduct)
            else:
                ans.append(product//num)
        return ans