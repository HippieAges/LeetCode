def fillPrefixSum(arr : list[int]) -> list[int]:
    prefixSum = [0 for _ in range(len(arr))]

    for index, elem in enumerate(arr):
        if index == 0:
            prefixSum[0] = elem
        else:
            prefixSum[index] = prefixSum[index - 1] + elem

    return prefixSum

print(fillPrefixSum([10, 20, 10, 5, 15]))