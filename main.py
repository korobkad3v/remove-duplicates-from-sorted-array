import random


def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the pointer for the position of unique elements
        k = 1

        # Iterate through the array with the pointer `i`
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Found a unique element, place it at the position `k`
                nums[k] = nums[i]
                k += 1

        return k

if __name__ == "__main__":
    # arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(20)]
    # print (arr)
    k = removeDuplicates([1,1,2])

    print(k)

    