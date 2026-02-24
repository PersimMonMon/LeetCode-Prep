def powerset(input_set):
    output = [[]]

    # loop through all existing subsets
    for i in input_set:
        new_subsets = []
        for set in output:
            new_subsets.append(set + [i])

        # add all subsets to main output list
        output.extend(new_subsets)

    return output
