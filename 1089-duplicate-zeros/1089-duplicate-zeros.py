class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)
        i = n - 1
        j = n + zeros - 1

        while i != j:
            if j < n:
                arr[j] = arr[i]
            j -= 1

            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1

            i -= 1
