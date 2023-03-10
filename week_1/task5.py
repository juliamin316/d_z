def find_result(strs_list):
    result = {}
    for strs in strs_list:
        sorted_strs = ''.join(sorted(strs))
        if sorted_strs in result:
            result[sorted_strs].append(strs)
        else:
            result[sorted_strs] = [strs]

    result_list = list(map(lambda x: sorted(x), list(result.values())))
    result_list = sorted(result_list)
    return result_list
print(find_result(["eat","tea","tan","ate","nat","bat"]))
