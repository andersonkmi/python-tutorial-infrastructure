def pair_sum_sorted_brute_force(nums, target):
    array_len = len(nums)
    for i in range(array_len):
        for j in range(i + 1, array_len):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []