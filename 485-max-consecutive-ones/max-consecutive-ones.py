class Solutions:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maximum = 0
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count += 1
                maximum = max(count,maximum)
            else:
                count = 0
        return maximum 



        
