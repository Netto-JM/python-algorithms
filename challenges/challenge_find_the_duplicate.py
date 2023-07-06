def find_duplicate(nums):
    if nums is None or len(nums) == 0:
        return False
    if any((not isinstance(num, int) or num < 0) for num in nums):
        return False
    nums.sort()
    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1]:
            return nums[num]
    return False
