class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # ans = []
        # zero = 0
        # zeroProduct = 1
        # for num in nums:
        #     if num == 0:
        #         zero += 1
        #         product = 0
        #         continue
        #     product *= num
        #     zeroProduct *= num
        # if zero>1:
        #     return [0]*len(nums)
        # for num in nums:
        #     if num == 0:
        #         ans.append(zeroProduct)
        #     else:
        #         ans.append(product//num)
        # return ans
        front = [1]
        zero = 0
        zeroProduct = 1
        ans = []
        for num in nums:
            if num==0:
                zero += 1
                continue
            zeroProduct *= num
        if zero > 2:
            return [0]*len(nums)
        if zero == 1:
            for num in nums:
                if num == 0:
                    ans.append(zeroProduct)
                else:
                    ans.append(0)
            return ans
        length = len(nums)
        back = [1]*length
        for i in range(length-1):
            front.append(nums[i]*front[-1])
            back[length-2-i] = back[length-1-i]*nums[length-1-i]
        for i in range(length):
            ans.append(front[i]*back[i])
        return ans


