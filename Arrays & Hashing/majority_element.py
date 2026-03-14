class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        record = {}
        highest_copies = 0
        majority = 0

        for i in range(len(nums)):
            if nums[i] in record:
                record[nums[i]] += 1
            if nums[i] not in record:
                record[nums[i]] = 1

        for key in record:
            if record[key] > highest_copies:
                highest_copies = record[key]
                majority = key
        return highest_copies

s = [3,2,3]
hello = Solution()
print(hello.majorityElement(s))