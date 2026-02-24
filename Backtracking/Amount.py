def amount(nums_list, target_sum):
    result = []

    # sort list first
    nums_list.sort()

    def backtrack(initial, curr_list, remainder):

        # add to result if target hits
        if remainder == 0:
            result.append(curr_list[:])
            return

        for i in range(initial, len(nums_list)):

            # ensure no duplicates
            if i > initial and nums_list[i] == nums_list[i - 1]:
                continue

            # add to list and move to next element
            curr_list.append(nums_list[i])
            backtrack(i + 1, curr_list, remainder - nums_list[i])

            curr_list.pop()

    backtrack(0, [], target_sum)
    return result
